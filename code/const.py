import os

with open("folder_path", "r", encoding="utf-8") as f:
    FOLDER_PATH = os.path.join("data", f.read().strip())
# FOLDER_PATH = "/Users/wascus/Documents/Università/tesi/state-Thu_29_Sep_14-02-05_UTC_2022"
# FOLDER_PATH = "/Users/wascus/Documents/Università/tesi/state-Oct-07-2022"
# FOLDER_PATH = "/Users/wascus/Documents/Università/tesi/state-Wed_Sep_28_11-07-22_2022"

with open(os.path.join(FOLDER_PATH, "MLP"), "r") as f:
    txt = f.read()
MLP = ":".join(txt.split(":")[1:-2]).strip()

# check if folder exists
if not os.path.exists(os.path.join(FOLDER_PATH, "graphs")):
    os.mkdir(os.path.join(FOLDER_PATH, "graphs"))

# DICT_AVG_COLOR = {
#     0: [0 , 0, 0],
#     0.5: [199/255, 0, 57/255],
#     1: [255/255, 87/255, 51/255],
#     1.5: [255/255, 195/255, 0],
#     2: [184/255, 255/255, 51/255],
#     2.5: [31/255, 164/255, 33/255],
#     3: [87/255, 26/255, 117/255],
# }
