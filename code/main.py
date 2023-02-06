from const import *
from funcs import *
import os
from log_converter import get_diagnostic
from copy import deepcopy



def main():
    with open("folder_path", "r", encoding="utf-8") as f:
        FOLDER_PATH = os.path.join("data", f.read().strip())
    res = []
    sensor_list = SensorList()
    polled_path = os.path.join(FOLDER_PATH, "polled.csv")
    eui_path = os.path.join(FOLDER_PATH, "EUI_ID.csv")
    diagnostic_path = os.path.join(FOLDER_PATH, "diagnostics.log")
    coord_path = os.path.join(FOLDER_PATH, "nodePosition.csv")
    sensor_list = get_IP_EUI_from_polled(polled_path, sensor_list)
    sensor_list = get_ID_EUI_mapping(eui_path, sensor_list)
    # sensor_list = get_coord_ID_mapping(coord_path, sensor_list)
    for s in sensor_list:
        id = int(s.id)
        if id == 1:
            s.gridPos = (1,1)
        elif id == 2:
            s.gridPos = (1,2)
        elif id == 3:
            s.gridPos = (0,0)
        elif id == 4:
            s.gridPos = (2,2)
        elif id == 5:
            s.gridPos = (1,0)
        elif id == 6:
            s.gridPos = (0,1)
        elif id == 7:
            s.gridPos = (0,2)
        elif id == 8:
            s.gridPos = (2,1)
        elif id == 9:
            s.gridPos = (2,0)
    periods = get_diagnostic(diagnostic_path)
 
    matrix = ConnectionMatrix(sensor_list)
    time = 0
    for period in periods:
        oldtime = time
        time = period["time"]
        create_poll_file(oldtime, time, sensor_list)

        nodes = SensorList()
        for diag in period["responses"]:
            rloc = diag["Rloc16"]
            ip = getIPfromList(diag["IP6 Address List"], MLP)
            sensor = None
            for s in sensor_list:
                if s.ip == ip:
                    sensor = s
                    sensor.rloc = rloc
                    break
            if sensor == None:
                continue
            for mapping in period["routerTable"]:
                if mapping["Rloc16"] == rloc:
                    sensor.local_id = mapping["RouterId"]
                    break
            if sensor.local_id == None:
                continue
            else:
                nodes.add(sensor)
        
        for diag in period["responses"]:
            rloc = diag["Rloc16"]
            ip = getIPfromList(diag["IP6 Address List"], MLP)
            sensor = None
            for s in nodes:
                if s.ip == ip:
                    sensor = s
                    break
            if sensor == None:
                continue

            for conn in diag["Route"]["RouteData"]:
                loc_id = str(int(conn["RouteId"], base=16))
                lout = conn["LinkQualityOut"]
                lin = conn["LinkQualityIn"]
                node = nodes.has(local_id=loc_id)
                if node == False:
                    continue
                matrix.update(sensor, node, (int(lout)+int(lin))/2)
        

        matrix.update_all()
        
        print("Time: " + time)
        # print()
        # printMatrix(matrix.matrix)
        # print()
        # print()
        
        res.append(deepcopy([time, matrix]))

        # drawMatrix(matrix, period["time"])
    
    return res
    

if __name__ == "__main__":
    main()