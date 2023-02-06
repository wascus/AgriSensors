from const import *
import os
import json


def getResponsesInfo(connection_info):
    res = []
    responses = connection_info.split('DIAG_GET.rsp/ans')[1:]
    for response in responses:
        responseDict = {}
        if response == '':  continue
        response = response.split('\n')
        i = 0
        while i < len(response):
            line = response[i].strip()
            if line.startswith("Ext Address:"):
                responseDict['Ext Address'] = line.split(':')[1].strip()
            elif line.startswith("Rloc16:"):
                responseDict['Rloc16'] = line.split(':')[1].strip()
            elif line.startswith("Mode:"):
                mode = {}
                for j in range(i+1, i+4):
                    mode[response[j].split(':')[0].strip()] = response[j].split(':')[1].strip()
                responseDict['Mode'] = mode
                i += 3
                continue
            elif line.startswith("Connectivity:"):
                connectivity = {}
                for j in range(i+1, i+10):
                    connectivity[response[j].split(':')[0].strip()] = response[j].split(':')[1].strip()
                responseDict['Connectivity'] = connectivity
                i += 9
                continue
            elif line.startswith("Route:"):
                route = {}
                i += 1
                route[response[i].split(':')[0].strip()] = response[i].split(':')[1].strip()
                i += 1
                routedata = []
                i += 1
                route["RouteData"] = get_connections(response, i, response.index("Leader Data:"))
                responseDict['Route'] = route
                i = response.index("Leader Data:")
                continue
            elif line.startswith("Leader Data:"):
                leaderData = {}
                for j in range(i+1, i+6):
                    leaderData[response[j].split(':')[0].strip()] = response[j].split(':')[1].strip()
                responseDict['Leader Data'] = leaderData
                i += 5
                continue
            elif line.startswith("Network Data:"):
                responseDict['Network Data'] = line.split(':')[1].strip()
            elif line.startswith("IP6 Address List:"):
                responseDict['IP6 Address List'] = getIPs(response, i, response.index("MAC Counters:"))
                i = response.index("MAC Counters:")
                continue
            elif line.startswith("MAC Counters:"):
                macCounters = {}
                for j in range(i+1, i+10):
                    macCounters[response[j].split(':')[0].strip()] = response[j].split(':')[1].strip()
                responseDict['MAC Counters'] = macCounters
                i += 9
                continue
            elif line.startswith("Child Table:"):
                responseDict['Child Table'] = getChildTable(response, i+1)
            i += 1

        res.append(responseDict)
    return res

def getChildTable(response, i):
    childTable = []
    children_text = "\n".join(response[i:])
    children = children_text.split('-')[1:]
    if len(children) == 0:  return []
    for child in children:
        childDict = {}
        child = child.split('\n')
        for line in child:
            i += 1
            line = line.strip()
            if line == '':  continue
            if line.startswith("Mode:"):
                childDict['Mode'] = {}
                for i in range(i, i+3):
                    childDict["Mode"][response[i].split(':')[0].strip()] = response[i].split(':')[1].strip()
                i += 1
                break
            else:
                childDict[line.split(':')[0].strip()] = line.split(':')[1].strip()
        childTable.append(childDict)
    return childTable


def getIPs(response, start, end):
    ips = []
    for i in range(start+1, end):
        ips.append(response[i].split("-")[1].strip())
    return ips

def get_connections(response, i1, i2):
    res = []
    connections = response[i1:i2]
    text = '\n'.join(connections)
    connections = text.split('-')
    for connection in connections:
        if connection.strip() == '': continue
        connection = connection.split('\n')
        conn = {}
        for line in connection:
            if line.strip() == '': continue
            conn[line.split(':')[0].strip()] = line.split(':')[1].strip()
        res.append(conn)
    return res

def getRouterTableInfo(routerTable_info):
    rt = []
    lines = routerTable_info.split('\n')
    for i in range(5, len(lines)):
        line = lines[i].strip()
        if line == '':  continue
        router = {}
        chunks = line.split("|")
        router['RouterId'] = chunks[1].strip()
        router['Rloc16'] = chunks[2].strip()
        router['NextHop'] = chunks[3].strip()
        router['PathCost'] = chunks[4].strip()
        router['LQIIn'] = chunks[5].strip()
        router['LQIOut'] = chunks[6].strip()
        router['Age'] = chunks[7].strip()
        router['Extended Mac'] = chunks[8].strip()
        router["Link"] = chunks[9].strip()
        rt.append(router)
    return rt

def getNeighborTableInfo(nb_info):
    nb = []
    lines = nb_info.split('\n')
    for i in range(4, len(lines)):
        line = lines[i].strip()
        if line == '':  continue
        router = {}
        chunks = line.split("|")
        router['Role'] = chunks[1].strip()
        router['Rloc16'] = chunks[2].strip()
        router['Age'] = chunks[3].strip()
        router['Avg RSSI'] = chunks[4].strip()
        router['Last RSSI'] = chunks[5].strip()
        router['R'] = chunks[6].strip()
        router['D'] = chunks[7].strip()
        router['N'] = chunks[8].strip()
        router["Extended MAC"] = chunks[9].strip()
        nb.append(router)
    return nb

def getTime(time_info):
    lines = time_info.split('\n')
    return lines[1].strip()

def get_diagnostic(diagnostic_path):
    res = []
    with open(diagnostic_path, "r") as f:
        diagnostics = f.read()

    periods = diagnostics.split("-"*38)[2:]

    for period in periods:
        doneSplits = period.split("Done")
        time = getTime(doneSplits[0])
        responses = getResponsesInfo(doneSplits[0])
        routerTable_info = getRouterTableInfo(doneSplits[1])
        neighborTable_info = getNeighborTableInfo(doneSplits[2])
        other = doneSplits[3]
        res.append({"time": time, "responses": responses, "routerTable": routerTable_info, "neighborTable": neighborTable_info, "other": other})
    return res

if __name__ == "__main__":
    diagnostic_path = os.path.join(FOLDER_PATH, 'diagnostics.log')
    res = get_diagnostic(diagnostic_path)
    with open(os.path.join(FOLDER_PATH, 'diagnostics.json'), 'w') as f:
        json.dump(res, f)

