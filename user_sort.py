from pprint import pprint
from ldap3 import SUBTREE
from func import system_time, log_append
from classes import Teams
from connections import Connections


def user_sort(rocket, user):
    conn = Connections.ldap
    if not conn.bind():
        return
    search_filter = f"(&(objectclass=user)(sAMAccountName={user['username']}))"
    _, _, response, _ = conn.search(
        search_base='OU=Szwajcarska,DC=szpitalsm,DC=local',
        search_filter=search_filter,
        attributes=['sAMAccountName'],
        search_scope=SUBTREE)

    for ldapUser in response:
        for team in Teams().teams:
            if ldapUser['dn'].rfind(team.get_dn()) != -1:
                rocket.groups_invite(team.get_id(), user['_id'])
                rocket.users_update(user['_id'], roles=['user', 'guest'])
                log = f"{system_time()} - Added {user['username']} to {team.get_name()}"
                pprint(log)
                log_append(log)
                break

    rocket.channels_invite('KwWXAxZp9E7tEzygt', user['_id'])
    conn.unbind()
    return
