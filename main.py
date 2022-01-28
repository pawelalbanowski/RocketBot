from requests import sessions
from pprint import pprint
from ldap3 import SUBTREE
import time
from func import system_time, json_read, json_write, log_append
from general_message import general_message
from classes import Teams
from connections import Connections


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
                if user['roles'] == ['user']:  # or user['roles'] == ['user', 'guest']:
                    conn = Connections.conn
                    searchFilter = '(&(objectclass=user)(sAMAccountName=' + user['username'] + '))'
                    status, result, response, _ = conn.search(
                        search_base='OU=Szwajcarska,DC=szpitalsm,DC=local',
                        search_filter=searchFilter,
                        attributes=['sAMAccountName'],
                        search_scope=SUBTREE)
                    for ldapUser in response:
                        dnIT = ldapUser['dn'].rfind(Teams.it.getDn())
                        dnPlace = ldapUser['dn'].rfind(Teams.place.getDn())
                        dnWew = ldapUser['dn'].rfind(Teams.wew.getDn())
                        dnKadry = ldapUser['dn'].rfind(Teams.kadry.getDn())
                        dnKsiegowosc = ldapUser['dn'].rfind(Teams.ksiegowosc.getDn())
                        dnDNM = ldapUser['dn'].rfind(Teams.dnm.getDn())
                        dnDLA = ldapUser['dn'].rfind(Teams.dla.getDn())
                        dnInwentaryzacja = ldapUser['dn'].rfind(Teams.inwentaryzacja.getDn())
                        dnZaopatrzenie = ldapUser['dn'].rfind(Teams.zaopatrzenie.getDn())
                        dnOrgPrawny = ldapUser['dn'].rfind(Teams.orgprawny.getDn())
                        if dnIT != -1:
                            rocket.groups_invite(Teams.it.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to IT'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='IT')
                        if dnPlace != -1:
                            rocket.groups_invite(Teams.place.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Place'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Płace')
                        if dnWew != -1:
                            rocket.groups_invite(Teams.wew.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Wewnetrzny'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Oddział Wewnętrzny')
                        if dnKadry != -1:
                            rocket.groups_invite(Teams.kadry.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Kadry'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Kadry')
                        if dnKsiegowosc != -1:
                            rocket.groups_invite(Teams.ksiegowosc.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Ksiegowosc'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Ksiegowosc')
                        if dnDNM != -1:
                            rocket.groups_invite(Teams.dnm.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to NadzorMedyczny'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='NadzorMedyczny')
                        if dnDLA != -1:
                            rocket.groups_invite(Teams.dla.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to LogistycznoAdministracyjny'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='LogistycznoAdministracyjny')
                        if dnInwentaryzacja != -1:
                            rocket.groups_invite(Teams.inwentaryzacja.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Inwentaryzacja'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Inwentaryzacja')
                        if dnZaopatrzenie != -1:
                            rocket.groups_invite(Teams.zaopatrzenie.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to Zaopatrzenie'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='Zaopatrzenie')
                        if dnOrgPrawny != -1:
                            rocket.groups_invite(Teams.orgprawny.getId(), user['_id'])
                            log = system_time() + ' - Added ' + user['username'] + ' to OrganizacyjnoPrawny'
                            pprint(log)
                            log_append('log.txt', log)
                            # rocket.users_update(user['_id'], nickname='OrganizacyjnoPrawny')
                    rocket.users_update(user['_id'], roles=['user', 'guest'])
                    rocket.channels_invite('KwWXAxZp9E7tEzygt', user['_id'])
            msg_log = general_message(rocket)
            pprint(msg_log)
            log_append('log.txt', msg_log)
            json_write('txtData.json', jsonData)
        else:
            msg_log = general_message(rocket)
            pprint(system_time() + ' - No new users' + ', ' + msg_log)
        time.sleep(30.0)
