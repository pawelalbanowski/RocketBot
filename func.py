from datetime import datetime
import json
from config import LOG_FILE


def system_time():
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    return 'System time: ' + date_time


def json_read(file):
    try:
        read_json_file = open(file, 'r')
        json_data = json.load(read_json_file)
        read_json_file.close()
        return json_data
    except FileNotFoundError as err:
        print(err)


def json_write(file, data):
    try:
        write_json = json.dumps(data, indent=4)
        write_file = open(file, 'w')
        write_file.write(write_json)
        write_file.close()
    except FileNotFoundError as err:
        print(err)


def log_append(data):  # append to log file
    try:
        f = open(LOG_FILE, 'a')
        f.write(data + '\n')
        f.close()
    except FileNotFoundError as err:
        print(err)


def presence_translate(data):
    return data.replace(' - online', '').replace('away', 'zaraz wracam').replace('busy', 'zajęty')


def present(data):
    return data == 'online' or data == 'away' or data == 'busy'
