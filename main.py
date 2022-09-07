from pprint import pprint
from rocketchat_API.APIExceptions import RocketExceptions
import ldap3.core.exceptions
from requests import sessions
from connections import Connections
from func import json_read, json_write, log_append
from general_message import general_message
from user_sort import user_sort
import os


def main():
    with sessions.Session() as session:
        try:
            rocket = Connections.rocketchat
            users = rocket.users_list().json()
            json_path = f"{str(os.path.dirname(os.path.realpath(__file__)))}/txtData.json"
            json_data = json_read(json_path)
            
            if users['total'] > json_data['totalUsers']:
                json_data['totalUsers'] = users['total']
                new_users = list(filter(lambda x: ('guest' not in x['roles']), users['users']))
                    
                if len(new_users) == 0:
                    msg_log = f'{general_message(rocket)} - Total user data updated, no users added to groups'
                else:
                    for user in new_users:
                        user_sort(rocket, user)
                    msg_log = general_message(rocket)
                    
                pprint(msg_log)
                log_append(msg_log)
                json_write(json_path, json_data)
            else:
                msg_log = general_message(rocket)
                pprint(f'No new users - {msg_log}')
                
            session.close()
            
        except (ConnectionError,
                OSError,
                ConnectionResetError,
                TypeError,
                RocketExceptions.RocketException,
                RocketExceptions.RocketConnectionException,
                RocketExceptions.RocketAuthenticationException,
                ldap3.core.exceptions.LDAPSocketSendError) as err:
            log = err
            pprint(log)
            log_append(log)
            session.close()


main()


# def run():
#     with sessions.Session() as session:
#         while 1:
#             try:
#                 main()
#                 time.sleep(30.0)
#             except (ConnectionError,
#                     OSError,
#                     ConnectionResetError,
#                     TypeError,
#                     RocketExceptions.RocketException,
#                     RocketExceptions.RocketConnectionException,
#                     RocketExceptions.RocketAuthenticationException,
#                     ldap3.core.exceptions.LDAPSocketSendError) as err:
#                 log = err + ' - Restarting in 30s...'
#                 pprint(log)
#                 log_append(log)
#                 session.close()
#                 time.sleep(30.0)
#                 run()


# run()
