from pprint import pprint
from ldap3 import SUBTREE
from func import system_time, log_append
from classes import Teams
from connections import Connections


def user_sort(rocket, user):
    conn = Connections.ldap
    search_filter = '(&(objectclass=user)(sAMAccountName=' + user['username'] + '))'
    _, _, response, _ = conn.search(
        search_base='OU=Szwajcarska,DC=szpitalsm,DC=local',
        search_filter=search_filter,
        attributes=['sAMAccountName'],
        search_scope=SUBTREE)
    for ldapUser in response:
        for team in Teams().teams:
            if ldapUser['dn'].rfind(team.getDn()) != -1:
                rocket.groups_invite(team.getId(), user['_id'])
                log = system_time() + ' - Added ' + user['username'] + ' to ' + team.getName()
                pprint(log)
                log_append('/var/log/RocketBot.log', log)
                break
    rocket.users_update(user['_id'], roles=['user', 'guest'])
    rocket.channels_invite('KwWXAxZp9E7tEzygt', user['_id'])
    conn.unbind()
    return
