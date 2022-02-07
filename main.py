from requests import sessions
from pprint import pprint
import time
from func import system_time, json_read, json_write, log_append
from general_message import general_message
from connections import Connections
from user_sort import user_sort

with sessions.Session() as session:
    rocket = Connections.rocket
    while 1:
        users = rocket.users_list().json()
        total = users['total']
        userList = users['users']
        jsonData = json_read('txtData.json')
        if total > jsonData['totalUsers']:
            jsonData['totalUsers'] = total
            for user in userList:
                if user['roles'] == ['user']:
                    user_sort(rocket, user)
            msg_log = general_message(rocket)
            pprint(msg_log)
            log_append('log.txt', msg_log)
            json_write('txtData.json', jsonData)
        else:
            msg_log = general_message(rocket)
            pprint(system_time() + ' - No new users' + ', ' + msg_log)
        time.sleep(30.0)
