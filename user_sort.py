from pprint import pprint
from ldap3 import SUBTREE
from func import system_time, log_append
from classes import Teams
from connections import Connections


def user_sort(rocket, user):
    conn = Connections.conn
    search_filter = '(&(objectclass=user)(sAMAccountName=' + user['username'] + '))'
    status, result, response, _ = conn.search(
        search_base='OU=Szwajcarska,DC=szpitalsm,DC=local',
        search_filter=search_filter,
        attributes=['sAMAccountName'],
        search_scope=SUBTREE)
    for ldapUser in response:
        dn_it = ldapUser['dn'].rfind(Teams.it.getDn())
        dn_place = ldapUser['dn'].rfind(Teams.place.getDn())
        dn_wew = ldapUser['dn'].rfind(Teams.wew.getDn())
        dn_kadry = ldapUser['dn'].rfind(Teams.kadry.getDn())
        dn_ksiegowosc = ldapUser['dn'].rfind(Teams.ksiegowosc.getDn())
        dn_dnm = ldapUser['dn'].rfind(Teams.dnm.getDn())
        dn_dla = ldapUser['dn'].rfind(Teams.dla.getDn())
        dn_inwentaryzacja = ldapUser['dn'].rfind(Teams.inwentaryzacja.getDn())
        dn_zaopatrzenie = ldapUser['dn'].rfind(Teams.zaopatrzenie.getDn())
        dn_orgprawny = ldapUser['dn'].rfind(Teams.orgprawny.getDn())
        dn_zamowienia = ldapUser['dn'].rfind(Teams.zamowienia.getDn())
        if dn_it != -1:
            rocket.groups_invite(Teams.it.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to IT'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='IT')
        if dn_place != -1:
            rocket.groups_invite(Teams.place.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Place'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Płace')
        if dn_wew != -1:
            rocket.groups_invite(Teams.wew.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Wewnetrzny'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Oddział Wewnętrzny')
        if dn_kadry != -1:
            rocket.groups_invite(Teams.kadry.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Kadry'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Kadry')
        if dn_ksiegowosc != -1:
            rocket.groups_invite(Teams.ksiegowosc.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Ksiegowosc'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Ksiegowosc')
        if dn_dnm != -1:
            rocket.groups_invite(Teams.dnm.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to NadzorMedyczny'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='NadzorMedyczny')
        if dn_dla != -1:
            rocket.groups_invite(Teams.dla.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to LogistycznoAdministracyjny'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='LogistycznoAdministracyjny')
        if dn_inwentaryzacja != -1:
            rocket.groups_invite(Teams.inwentaryzacja.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Inwentaryzacja'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Inwentaryzacja')
        if dn_zaopatrzenie != -1:
            rocket.groups_invite(Teams.zaopatrzenie.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Zaopatrzenie'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Zaopatrzenie')
        if dn_orgprawny != -1:
            rocket.groups_invite(Teams.orgprawny.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to OrganizacyjnoPrawny'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='OrganizacyjnoPrawny')
        if dn_zamowienia != -1:
            rocket.groups_invite(Teams.zamowienia.getId(), user['_id'])
            log = system_time() + ' - Added ' + user['username'] + ' to Zamówienia'
            pprint(log)
            log_append('log.txt', log)
            # rocket.users_update(user['_id'], nickname='Zamówienia')
    rocket.users_update(user['_id'], roles=['user', 'guest'])
    rocket.channels_invite('KwWXAxZp9E7tEzygt', user['_id'])
    return
