from datetime import datetime
import json


def system_time():
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    return 'System time: ' + date_time


def json_read(file):
    read_json_file = open(file, 'r')
    json_data = json.load(read_json_file)
    read_json_file.close()
    return json_data


def json_write(file, data):
    write_json = json.dumps(data, indent=4)
    write_file = open(file, 'w')
    write_file.write(write_json)
    write_file.close()
    return


def log_append(data):  # append to log file
    log_file = '/var/log/RocketBot.log'
    f = open(log_file, 'a')
    f.write(data + '\n')
    f.close()
    return


def presence_translate(data):
    return data.replace(' - online', '').replace('away', 'zaraz wracam').replace('busy', 'zajęty')


def present(data):
    return data == 'online' or data == 'away' or data == 'busy'
