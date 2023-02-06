from flask import Flask, render_template, request
import datetime
import sys, os
sys.path.append(os.path.abspath("code"))
sys.path.append(os.path.abspath("./"))
import main
from src import *
import subprocess
import tarfile
import configparser



app = Flask(__name__)




@app.route("/")
@app.route("/home")
def home():
  with open('folder_path', 'r') as f:
    folder_path = f.read()
  config = configparser.ConfigParser()
  config.read('config.ini')
  auto_poll = config.get('user', 'auto_poll')
  poll_interval = config.getint('user', 'poll_interval')
  return render_template('home.html', folder_path=folder_path, dirs = [file for file in os.listdir("data") if not file.startswith(".")], settings = {"auto_poll": auto_poll, "poll_interval": poll_interval})


@app.route("/test")
def about():
    return render_template('test.html')

@app.route('/get_time', methods=['POST'])
def get_time():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return current_time

@app.route('/get_latest_polled', methods=['POST'])
def get_latest_polled():
    # get latest polled via scp
    print("getting .tar file_name via ssh")
    file_name = subprocess.run(["ssh", "-p2222", "pi@140.238.65.67", "/home/pi/save_state.sh"], capture_output=True, text=True)
    if file_name.returncode != 0:
      return "error"
    subprocess.run(["scp", "-P2222", f"pi@140.238.65.67:{file_name}", "data"])
    # extract tar file
    with tarfile.open(os.path.join("data", file_name), 'r:gz') as tar:
      # Extract the contents of the tarfile to the current directory
      tar.extractall(path='data')
      # delete tar file
      os.remove(os.path.join("data", file_name))
    new_folder_name = file_name[:-4]
    with open('folder_path', 'w') as f:
      f.write(new_folder_name)
    return "ok"

@app.route('/set_page_for_data', methods=['POST'])
def set_page_for_data():
  folder_path = request.json.get('folder_path')
  with open('folder_path', 'w') as f:
    f.write(folder_path)
    print("directory changed")
  return "ok"

@app.route('/node_clicked', methods=['POST'])
def node_clicked():
  node_id = request.json.get('node')
  time = request.json.get('time')
  date = request.json.get('date')
  response = prepare_json_for_node_info(node_id, time, date)
  return response

@app.route('/code.js')
def code():
  cache_status = check_cache()
  if cache_status != None:
    avg = get_avg_data()
    return render_template('code.js', periods=cache_status, avg_data=avg)
  m = prepare_for_template(main.main())
  add_to_cache(m)
  avg = get_avg_data()
  return render_template('code.js', periods=m, avg_data=avg)

@app.route('/change_settings', methods=['POST'])
def change_settings():
  try:
    options = request.json.get('options')
    config = configparser.ConfigParser()
    config.read('config.ini')
    for key, value in options.items():
      config.set('user', key, str(value).lower())
    with open('config.ini', 'w') as configfile:
      config.write(configfile)
    return "success"
  except:
    return "error"




if __name__ == '__main__':
    app.run(debug=True)