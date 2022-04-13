import time
from pprint import pprint

import ldap3.core.exceptions
from requests import sessions
from connections import Connections
from func import system_time, json_read, json_write, log_append
from general_message import general_message
from user_sort import user_sort


def main():
    rocket = Connections.rocketchat
    users = rocket.users_list().json()
    json_data = json_read('txtData.json')
    if users['total'] > json_data['totalUsers']:
        json_data['totalUsers'] = users['total']
        new_users = list(filter(lambda x: ('guest' not in x['roles']), users['users']))
        for user in new_users:
            user_sort(rocket, user)
        msg_log = general_message(rocket)
        pprint(msg_log)
        log_append('log.txt', msg_log)
        json_write('txtData.json', json_data)
    else:
        msg_log = general_message(rocket)
        pprint(system_time() + ' - No new users' + ', ' + msg_log)


def run():
    with sessions.Session() as session:
        while 1:
            try:
                main()
                time.sleep(30.0)
            except (ConnectionError,
                    OSError,
                    ConnectionResetError,
                    TypeError,
                    ldap3.core.exceptions.LDAPSocketSendError) as err:
                log = err + ' - Restarting in 30s...'
                pprint(log)
                log_append('log.txt', log)
                session.close()
                time.sleep(30.0)
                run()


run()
