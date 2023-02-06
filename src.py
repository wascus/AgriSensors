import os
import json
import pickle
from datetime import datetime
with open("folder_path", "r", encoding="utf-8") as f:
    FOLDER_PATH = os.path.join("data", f.read().strip())

DICT_AVG_COLOR = {
    0: "white",
    0.5: "red",
    1: "orange",
    1.5: "yellow",
    2: "lightgreen",
    2.5: "darkgreen",
    3: "purple",
}


class Period:
  pass
class Edge:
  pass

def convert_time_to_epoch(time: str) -> int:
    return int(datetime.strptime(time, "%a %d %b %H:%M:%S %Z %Y").timestamp())

def convert_epoch_to_date(epoch: float):
    return datetime.fromtimestamp(float(epoch)).strftime('%d-%m-%Y %H:%M:%S.%f')

def add_to_cache(res):
    with open("folder_path", "r", encoding="utf-8") as f:
        FOLDER_PATH = os.path.join("data", f.read().strip())
    if os.path.exists(os.path.join(FOLDER_PATH, "cache.pkl")):
        return
    else:
        with open(os.path.join(FOLDER_PATH, "cache.pkl"), "wb") as f:
            pickle.dump(res, f)

def check_cache():
    with open("folder_path", "r", encoding="utf-8") as f:
        FOLDER_PATH = os.path.join("data", f.read().strip())
    if os.path.exists(os.path.join(FOLDER_PATH, "cache.pkl")):
        with open(os.path.join(FOLDER_PATH, "cache.pkl"), "rb") as f:
            return pickle.load(f)
    else:
        return None


def prepare_for_template(m):
    res = []
    ii = 1
    for time, matrix in m:
        period = Period()
        period.time = time
        period.nodes = sorted(matrix.sensors.list, key=lambda x: (x.gridPos[0], x.gridPos[1]))
        period.edges = get_edges(matrix)
        period.index = ii
        ii += 1
        res.append(period)
    return res

def get_edges(matrix):
  res = []
  for i in range(len(matrix.matrix)):
    for j in range(len(matrix.matrix[i])):
      edge = Edge()
      if i <= j and matrix.matrix[i][j][0] != 0:
        id1 = matrix.sensors.list[i].id
        id2 = matrix.sensors.list[j].id
        edge.id = f"{id1}{id2}"
        edge.source = id1
        edge.target = id2
        edge.color = DICT_AVG_COLOR[matrix.matrix[i][j][0]]
        edge.width = matrix.matrix[i][j][1]
        res.append(edge)
  return res

def prepare_json_for_node_info(node_id, time, date):
    res = {}

    cache = check_cache()
    if cache == None:
        return "error1"
 
    # node data
    period_obj = [x for x in cache if x.time.split(" ")[3] == time][0]
    time = period_obj.time
    node_obj = [x for x in period_obj.nodes if x.id == node_id][0]
    res["node_info"] = {"id": node_obj.id, "ip": node_obj.ip, "rloc16": node_obj.rloc}

    # measurements data
    with open(os.path.join("data", date, "polled.csv"), "r", encoding="utf-8") as f:
        polled_list = f.read().split("\n")[1:-1]
    # remove from list all measurements made by other nodes
    for i in range(len(polled_list) - 1, -1, -1):
        polled = polled_list[i].split(",")
        if polled[1] != node_obj.ip:
            polled_list.pop(i)
    # remove from list all incorrect measurements
    for i in range(len(polled_list) - 1, -1, -1):
        polled = polled_list[i].split(",")
        if polled[3] in ["IR", "Vis", "Humidity"] and polled[4] != "nan" and float(polled[4]) == 0.0:
            polled_list.pop(i)
        elif polled[3] in ["Temperature"] and polled[4] != "nan" and float(polled[4]) == -45.0:
            polled_list.pop(i)
    # remove from list all measurements made after the time we are looking for
    for i in range(len(polled_list) - 1, -1, -1):
        polled = polled_list[i].split(",")
        if convert_time_to_epoch(time) < float(polled[0]):
            polled_list.pop(i)
    polled_list.sort(key=lambda x: float(x.split(",")[0]))
    # divide measurements into groups
    groups = {"Temperature": [], "Humidity": [], "IR": [], "Vis": [], "Batt": []}
    for measure in polled_list:
        measure = measure.split(",")
        groups[measure[3]].append([measure[0], measure[4]]) # timestamp, value
    res["measurement"] = groups
    # adjust vis values
    C = 13.14
    for m in res["measurement"]["Vis"]:
        m[1] = str(round(float(m[1]) / C, 2))
    return res
         
def get_avg_data():
    with open("folder_path", "r", encoding="utf-8") as f:
        FOLDER_PATH = os.path.join("data", f.read().strip())
    with open(os.path.join(FOLDER_PATH, "polled.csv"), "r", encoding="utf-8") as f:
        polled_list = f.read().split("\n")[1:-1]

    res = {"Temperature": None, "Humidity": None, "IR": None, "Vis": None, "Batt": None}
    
    nodes = set()
    for measure in polled_list:
        measure = measure.split(",")
        nodes.add(measure[2])
    
    for value in ["Temperature", "Humidity", "IR", "Vis", "Batt"]:
        summed = 0
        temp_list = [x for x in polled_list if x.split(",")[3] == value]
        if value == "Vis":
            C = 13.14
            temp_list = [x for x in temp_list if float(x.split(",")[4]) != 0.0]
            temp_list = [f"{x.split(',')[0]},{x.split(',')[1]},{x.split(',')[2]},{x.split(',')[3]},{round(float(x.split(',')[4]) / C, 2)}" for x in temp_list]
        for node in nodes:
            temp = [x for x in temp_list if x.split(",")[2] == node]
            temp = [x for x in temp if x.split(",")[4] != "nan"]
            m = float(max(temp, key=lambda x: float(x.split(",")[0])).split(",")[4])
            summed += m
        avg = summed / len(nodes)
        res[value] = round(avg, 2)
    return res