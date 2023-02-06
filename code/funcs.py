from const import *
from datetime import datetime
import math
import networkx as nx
import matplotlib.pyplot as plt
from copy import deepcopy

INF = float("inf")



class ConnectionMatrix:
    def __init__(self, sensors):
        self.matrix = []
        self.sensors = sensors
        self.create_matrix()

    def create_matrix(self):
        for sensor in self.sensors:
            self.matrix.append([[0, INF] for _ in range(len(self.sensors))]) # (LinkQual, age)

    def update(self, s1, s2, q):
        if q != 0:
            i1 = self.sensors.index(s1)
            i2 = self.sensors.index(s2)
            self.matrix[i1][i2][0] = q
            self.matrix[i1][i2][1] = -1

    def update_all(self):
        for i in range(len(self.matrix[0])):
            for j in range(len(self.matrix)):
                self.matrix[i][j][1] += 1

    def print(self):
        printMatrix(self.matrix)



class Sensor:
    def __init__(self, id=None, eui=None, ip=None, rloc=None, local_id=None):
        # immutable
        self.ip = ip
        self.eui = eui
        self.id = id
        self.coordinates = None
        self.gridPos = None
        # mutable
        self.rloc = rloc
        self.local_id = local_id

    def isIt(self, ip=None, eui=None, id=None, rloc=None, local_id=None):
        if ip is not None and self.ip == ip:
            return self.ip == ip
        elif eui is not None and self.eui == eui:
            return self.eui == eui
        elif id is not None and self.id == id:
            return self.id == id
        elif rloc is not None and self.rloc == rloc:
            return self.rloc == rloc
        elif local_id is not None and self.local_id == local_id:
            return self.local_id == local_id
        else:
            return False

    def __repr__(self) -> str:
        if self.id is not None:
            return f"Sensor {self.id}"
        elif self.eui is not None:
            return f"Sensor {self.eui}"
        elif self.ip is not None:
            return f"Sensor {self.ip}"
        elif self.rloc is not None:
            return f"Sensor {self.rloc}"
        elif self.local_id is not None:
            return f"Sensor {self.local_id}"
        else:
            return "Sensor: None"
    
    def __str__(self) -> str:
        return self.__repr__()


class Coords:
    def __init__(self, x, y):
        self.lat = x
        self.lon = y

class SensorList:
    def __init__(self):
        self.list = []

    def add(self, sensor):
        if not self.has(ip=sensor.ip, eui=sensor.eui, id=sensor.id):
            self.list.append(sensor)

    def has(self, ip=None, eui=None, id=None, rloc=None, local_id=None):
        for sensor in self.list:
            if sensor.isIt(ip, eui, id, rloc, local_id):
                return sensor
        return False

    def get(self, ip=None, eui=None, id=None, rloc=None, local_id=None):
        for sensor in self.list:
            if sensor.isIt(ip, eui, id, rloc, local_id):
                return sensor
        return None

    def index(self, s):
        for i in range(len(self.list)):
            if self.list[i] == s:
                return i
        
    
    def __repr__(self) -> str:
        return str(self.list)

    def __str__(self) -> str:
        return self.__repr__()

    def __len__(self) -> int:
        return len(self.list)

    def __iter__(self):
        return iter(self.list)

def printMatrix(matrix):
    """
    prints a matrix with right spacing
    """
    for row in matrix:
        for i in range(len(row)):
            if i == 0:
                if row[i] == None:
                    print("    ", end="")
                else:
                    print(str(row[i]).ljust(4), end="")
            else:
                print(str(row[i]).ljust(10), end="")
        print()

def get_IP_EUI_from_polled(polled_path, sensors):
    with open(polled_path, "r", encoding="utf-8") as f:
        txt = f.read()
    lines = txt.split("\n")[1:]
    for line in lines:
        if line == "":  continue
        line = line.split(",")
        ip = line[1]
        eui = line[2]
        sensors.add(Sensor(ip=ip, eui=eui))
    return sensors

def get_ID_EUI_mapping(mapping_path, sensors):
    with open(mapping_path, "r", encoding="utf-8") as f:
        txt = f.read()
    lines = txt.split("\n")[1:]
    for line in lines:
        if line == "":  continue
        line = line.split(",")
        id = line[1]
        eui = line[0]
        if sensors.has(eui=eui):
            sensors.get(eui=eui).id = id
    return sensors

def get_coord_ID_mapping(coord_path, sensor_list):
    with open(coord_path, "r", encoding="utf-8") as f:
        txt = f.read()
    lines = txt.split("\n")[1:]
    for line in lines:
        if line == "":  continue
        line = line.split(",")
        id = line[0]
        x = float(line[1])
        y = float(line[2])
        sensor_list.get(id=id).coordinates = Coords(x, y)
    return sensor_list


def create_poll_file(t1, t2, sensor_list):
    if t1 != 0:
        t1 = convert_time_to_epoch(t1)
    t2 = convert_time_to_epoch(t2)

    with open(FOLDER_PATH + "/polled.csv", "r", encoding="utf-8") as f:
        txt = f.read()
    lines = txt.split("\n")
    all_sensor = {}
    for line in lines[1:]:
        if line == "":  continue
        line = line.split(",")
        time = line[0]
        if t1 <= float(time) < t2:
            all_sensor[sensor_list.get(eui=line[2])] = {}
    
    for line in lines[1:]:
        if line == "":  continue
        line = line.split(",")
        sensor = sensor_list.get(eui=line[2])
        endpoint = line[3]
        value = float(line[4])
        try:
            if endpoint in all_sensor[sensor]:
                all_sensor[sensor][endpoint].append(value)
            else:
                all_sensor[sensor][endpoint] = [value]
        except:
            pass

    newFile = f"{convert_epoch_to_date(t1)} - {convert_epoch_to_date(t2)}" + "\n"
    for sensor in all_sensor:
        newFile += f"{sensor}:" + "\n"
        for endpoint in all_sensor[sensor]:
            newFile += "\t" + f"{endpoint}: {avg(all_sensor[sensor][endpoint])}" + "\n"
    newFile += "\n"

    with open(FOLDER_PATH + "/polled_output.log", "a", encoding="utf-8") as f:
        f.write(newFile)


def convert_time_to_epoch(time: str) -> int:
    return int(datetime.strptime(time, "%a %d %b %H:%M:%S %Z %Y").timestamp())

def convert_epoch_to_date(epoch: float):
    return datetime.fromtimestamp(float(epoch)).strftime('%d-%m-%Y %H:%M:%S.%f')

def sum_list(lst):
    res = 0
    for l in lst:
        if not math.isnan(l):
            res += l
    return res

def avg(lst):
    s = sum_list(lst)
    l = len(lst)
    return s/l

def getIPfromList(list, mlp):
    for ip in list:
        if ip.startswith(mlp) and "0:ff:fe00" not in ip:
            return ip
    raise Exception("No IP found")

def drawMatrix(matrix, time):
    # coords = [s.coordinates for s in matrix.sensors]
    # maxLat = max([c.lat for c in coords])
    # minLat = min([c.lat for c in coords])
    # maxLon = max([c.lon for c in coords])
    # minLon = min([c.lon for c in coords])
    # gapLat = minLat - 1*10**-4 
    # gapLon = minLon - 1*10**-5
    # coords = list(map(lambda x: Coords((x.lat-gapLat)*10**4, (x.lon-gapLon)*10**5), coords))


    G=nx.Graph()

    for s in matrix.sensors:
        G.add_node(s.id, pos=(s.gridPos))

    for i in range(len(matrix.matrix)):
        for j in range(len(matrix.matrix[i])):
            if matrix.matrix[i][j] != None:
                c = deepcopy(DICT_AVG_COLOR[matrix.matrix[i][j][0]])
                transparency = 1/(matrix.matrix[i][j][1] + 1)
                c += [transparency]
                G.add_edge(matrix.sensors.list[i].id,matrix.sensors.list[j].id, weight=3, color=c)

    colors = nx.get_edge_attributes(G,'color').values()
    weights = nx.get_edge_attributes(G,'weight').values()
    pos = nx.get_node_attributes(G,'pos')
    nx.draw(
            G,
            pos,
            edge_color=colors,
            width=list(weights),
            with_labels=True,
            node_color="lightblue")
    plt.savefig(os.path.join(FOLDER_PATH, "graphs", f"{time}.png"))
    plt.clf()
    


