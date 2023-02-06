# THIS FILE IS DEPRECATED
from const import *
from funcs import *

EUI_ID = {
    "0x00124b0021aa36ed": 3,
    "0x00124b0021aa36fe": 6,
    "0x00124b0021aa35d4": 2,
    "0x00124b0021aa35d5": 1,
    "0x00124b0021aa36e6": 5,
    "0x00124b0021aa378b": 7,
    "0x00124b0021aa35a4": 4,
    }

MLP = "fd30:93d7:9154:b7c2"

def get_router_table(period: str, sensor_list) -> list:
    """
        example of return: {Rloc16: [Router Local ID, IP, EUI, ID]}
        {
            0x0400: 1,
            0x0c00: 3,
            0x5000: 20,
            0x600: 24,
        }
    """

    # get rloc for sensor ip
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        rloc = getRloc(node)
        startIP = False
        lines = node.split("\n")
        for i in range(len(lines)):
            line = lines[i]
            if line.strip().startswith("IP6 Address List:"):
                startIP = True
                continue
            if startIP:
                ip = line.split("-")[1].strip()
                if ip.startswith(MLP) and not "0:ff:fe00" in ip:
                    startIP = False
                    continue
        if sensor_list.has(ip=ip):
            sensor_list.get(ip=ip).rloc = rloc
        else:
            pass#sensor_list.add(Sensor(ip=ip, rloc=rloc))


    

    router_table = {}
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        lines = node.split("\n")
        start = False
        for i in range(len(lines)):
            line = lines[i]

            # finding router table
            if "Router Table" in line:
                start = i
            elif start != False and "Done" in line:
                end = i
                break
        if start != False:
            for i in range(start, end):
                line = lines[i]
                if not line.startswith("|") or line.startswith("| ID |"): continue
                else:
                    line = line.split("|")
                    router_table[line[2].strip()] = [int(line[1])]
                    if sensor_list.has(rloc = line[2].strip()):
                        sensor_list.get(rloc = line[2].strip()).local_id = int(line[1])
                    else:
                        pass#sensor_list.add(Sensor(rloc = line[2].strip(), local_id = int(line[1])))

    
    # get router ip
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        rloc = getRloc(node)
        startIP = False
        lines = node.split("\n")
        for i in range(len(lines)):
            line = lines[i]
            if line.strip().startswith("IP6 Address List:"):
                startIP = True
                continue
            if startIP:
                ip = line.split("-")[1].strip()
                if ip.startswith(MLP) and not "0:ff:fe00" in ip:
                    startIP = False
                    continue
        try:
            router_table[rloc] += [ip]
        except KeyError:
            pass

    # get router eui and add to RT router ID
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        rloc = getRloc(node)
        startEUI = False
        lines = node.split("\n")
        for i in range(len(lines)):
            line = lines[i]
            if line.strip().startswith("ip,EUI"):
                startEUI = True
                continue
            if startEUI:
                if line.strip() == "":
                    startEUI = False
                    continue
                ip, eui = line.split(",")
                # add eui to RT
                for k, v in router_table.items():
                    if ip in v:
                        router_table[k] += [eui, EUI_ID[eui]]
                        break

    return router_table

def getRloc(node: str) -> str:
    """
    returns the rloc of the node
    """
    for line in node.split("\n"):
        if line.startswith("Rloc16:"):
            return line.split(":")[1].strip()


def create_matrix(sensor_list) -> list:
    """
    creates a matrix with (0,0) as default value
    """
    l = len(sensor_list)
    matrix = [[None]]
    for s in sensor_list:
        matrix[0].append(s)
    for s in sensor_list:
        matrix.append([s] + [(0,0)]*l)
    return matrix
    # l = len(router_table)
    # matrix = [[None]]
    # for k, v in router_table.items():
    #     matrix[0].append(v[0])
    # for k, v in router_table.items():
    #     matrix.append([v[0]] + [(0,0)]*l)
    # return matrix

def update_matrix(matrix, n1, n2, a, b):
    """
    M[i][j] = (a,b)
    """
    bp = 2
    if None in [n1, n2]: return
    i = matrix[0].index(n1)
    for j in range(len(matrix)):
        if matrix[j][0] == n2:
            break
    matrix[j][i] = (a,b)
    bp = 2

def fill_matrix(matrix, node, router_table, sensor_list):
    isIn = False
    for line in node.split("\n"):
        if line.startswith("Rloc16:"):
            rloc16 = line.split(":")[1].strip()
            if rloc16 not in router_table: break
        elif line.startswith("Route:"):
            isIn = True
        elif isIn:
            if line.strip().startswith("-"):
                routeId = line.split(":")[1].strip()
            elif line.strip().startswith("LinkQualityOut:"):
                lout = line.split(":")[1].strip()
            elif line.strip().startswith("LinkQualityIn:"):
                lin = line.split(":")[1].strip()
                lid = int(routeId, base=16)
                update_matrix(matrix, sensor_list.get(rloc=rloc16), sensor_list.get(local_id=lid), lout, lin)
        elif line.startswith("Leader Data:"):
            isIn = False

def find_leader(period: str) -> str:
    """
    returns the leader id
    """
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        lines = node.split("\n")
        for line in lines:
            if line.strip().startswith("LeaderRouterId:"):
                return line.split(":")[1].strip()
                
def find_children(period) -> dict:
    children = {}
    for node in period.split("DIAG_GET.rsp/ans")[1:]:
        node = "DIAG_GET.rsp/ans" + node
        lines = node.split("\n")
        for line in lines:
            if line.strip().startswith("Rloc16:"):
                rloc16 = line.split(":")[1].strip()
            elif line.strip().startswith("- ChildId:"):
                if rloc16 not in children:
                    children[rloc16] = [hex(int(rloc16, base=16)+int(line.split(":")[1].strip(), base=16))]
                else:
                    children[rloc16].append(hex(int(rloc16, base=16)+int(line.split(":")[1].strip(), base=16)))
    return children

def main(argv):
    diagnostic_file = FOLDER_PATH + "/diagnostic.log"
    with open(diagnostic_file, "r") as f:
        diagnostic = f.read()
    periods = diagnostic.split("-"*38)
    time = 0
    for period in periods[2:]:
        oldtime = time
        time = period.split("\n")[1]

        # getting leader
        leader = find_leader(period)

        # getting router table
        router_table = get_router_table(period)

        # creating matrix
        matrix = create_matrix(router_table)

        # find children
        children = find_children(period)

        for node in period.split("DIAG_GET.rsp/ans")[1:]:
            node = "DIAG_GET.rsp/ans" + node
            fill_matrix(matrix, node, router_table)

        # results
        print("-"*38)
        print(time)
        print()
        print("Mapping:" + str(router_table))
        print("Leader: " + str(int(leader, base=16)))
        print("Connections:")
        printMatrix(matrix)
        print()
        print("Children Table:" + str(children))
        print()

        # draw_graph(matrix, router_table, time)