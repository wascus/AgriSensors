#!/usr/bin/python3 -u
import pandas as pd
routers = set()
folder = "/home/pi/"
with open(folder+'MLP', 'r') as file_mlp:
    line = file_mlp.readline()
    mlp = line.split("::")[0].split(": ")[1]
myip = None
with open(folder+'myip', 'r') as ipfile:
    line = ipfile.readline().rstrip()
    while line:
        if (mlp in line) and (not "0:ff:fe00" in line):
            myip = line
            break
        line = ipfile.readline().rstrip()
with open(folder+'toparse.txt', 'r') as file_object:
    line = file_object.readline()
    while line:
        if line == 'IP6 Address List:\n':
            line = file_object.readline()
            while line and line.startswith("    -"):
                if (mlp in line) and (not "0:ff:fe00" in line) and (not myip in line):
                    routers.add(line.split("- ")[1].rstrip())
                    break
                line = file_object.readline()
        else:
            line = file_object.readline()
routers = list(routers)
pd.Series(routers,dtype="string").to_csv(folder+'routersANDchildren.csv', index=False, header=False)

