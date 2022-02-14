import time
from pprint import pprint
from requests import sessions
from connections import Connections
from func import system_time, json_read, json_write, log_append
from general_message import general_message
from user_sort import user_sort


def main(rocket):
    users = rocket.users_list().json()
    total = users['total']
    user_list = users['users']
    json_data = json_read('txtData.json')
    if total > json_data['totalUsers']:
        json_data['totalUsers'] = total
        for user in user_list:
            if user['roles'] == ['user']:
                user_sort(rocket, user)
        msg_log = general_message(rocket)
        pprint(msg_log)
        log_append('log.txt', msg_log)
        json_write('txtData.json', json_data)
    else:
        msg_log = general_message(rocket)
        pprint(system_time() + ' - No new users' + ', ' + msg_log)


with sessions.Session() as session:
    rocketchat = Connections.rocketchat
    while 1:
        main(rocketchat)
        time.sleep(30.0)
