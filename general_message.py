from classes import ITMsg, Teams
from config import Rchat
from func import presence_translate, present, system_time
from ldap3 import Connection, SAFE_SYNC, SUBTREE, AUTO_BIND_NO_TLS
from connections import Ldap


def general_msg_block(team, rocket, sekretarki, oddzialowe):  # single block of one team
    block = []
    all_members = 0
    members = (rocket.groups_members(room_id=team.get_id()).json())['members']

    for member in members:
        if member['name'] != 'Rocket Bot' and member['name'] != 'Super Admin':
            all_members += 1
            if present(member['status']):
                active_member = member['username']
                if member['name'] in sekretarki:
                    active_member += ' (sekretariat)'
                if member['name'] in oddzialowe:
                    active_member += ' (oddziałowa)'
                active_member = presence_translate(active_member + ' - ' + member['status'])
                block.append(active_member)

    sorted_block = sorted(list(map(lambda x: ('- @' + x), block)))
    if sorted_block.count('- @' + team.get_kier()) > 0:
        sorted_block.insert(0, sorted_block.pop(sorted_block.index('- @' + team.get_kier())))

    present_str = str(len(sorted_block)) + '/' + str(all_members)
    block = '*{}* {}\n{}'.format(team.header, present_str, '\n'.join(sorted_block))
    return block


def it_block(rocket, team, header):
    block = []
    
    for member in team:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        if present(presence):
            block.append(presence_translate(member + ' - ' + presence))

    full_header = '- *' + header + '* ' + str(len(block)) + '/' + str(len(team))
    handles = list(map(lambda x: ('- - @' + x), block))
    block = '{}\n{}'.format(full_header, '\n'.join(handles))
    return block


def full_it_block(rocket):  # only for IT in general message, since IT is sectioned
    wsparcie_str = it_block(rocket, ITMsg.wsparcie, 'SEKCJA WSPARCIA UŻYTKOWNIKÓW')
    systemy_str = it_block(rocket, ITMsg.systemy, 'SEKCJA SYSTEMÓW INFORMATYCZNYCH')

    # kierownik
    presence = (rocket.users_get_presence(username=Teams.it.get_kier()).json())['presence']
    it_kier_handle = presence_translate('- @{} - {}'.format(Teams.it.get_kier(), presence))

    # całość
    block = '\n*{}*\n{}\n{}\n{}'.format(Teams.it.get_header(), it_kier_handle, wsparcie_str, systemy_str)
    return block


def sekrodd_list(choice):
    match choice:
        case 'sekr':
            searchbase = 'CN=DL_SekretarkiOddzialow,OU=SzpPracownicy,OU=Medyczni,OU=Pracownicy,OU=Szwajcarska,' \
                         'DC=szpitalsm,DC=local '
        case 'oddz':
            searchbase = 'CN=DL_PielegniarkiOddzialowe,OU=SzpPracownicy,OU=Medyczni,OU=Pracownicy,OU=Szwajcarska,' \
                         'DC=szpitalsm,DC=local '
        case _:
            return False
    conn = Connection(Ldap.server,
                      Ldap.user,
                      Ldap.passw,
                      read_only=True,
                      client_strategy=SAFE_SYNC,
                      auto_bind=AUTO_BIND_NO_TLS)

    search_filter = '(objectclass=group)'
    _, _, response, _ = conn.search(
        search_base=searchbase,
        search_filter=search_filter,
        attributes=['member'],
        search_scope=SUBTREE)

    members = response[0]['attributes']['member']
    members = list(map(lambda a: a.split(',', 1)[0].split('=', 1)[1], members))
    return members


def general_message(rocket):  # in ListaUzytkownikow
    groups = (rocket.groups_list_all().json())['groups']
    administracja = []
    szpital = []
    ignore = [Teams.akredytacja]
    sekretarki = sekrodd_list('sekr')
    oddzialowe = sekrodd_list('oddz')
    
    for group in groups:
        for team in Teams().teams:
            if team not in ignore:
                if group['name'] == team.get_name() and team.get_name() == 'IT':
                    block = full_it_block(rocket)
                    administracja.append(block)
                elif group['name'].lower() == team.get_name().lower():
                    block = general_msg_block(team, rocket, sekretarki, oddzialowe)
                    match team.get_category():
                        case 'administracja':
                            administracja.append(block)
                        case 'szpital':
                            szpital.append(block)
                            
    sorted_users = '\n\n'.join(sorted(administracja)) + '\n\n\n' + '\n\n'.join(sorted(szpital))
    rocket.chat_update(room_id='GENERAL', msg_id=Rchat.welcome_message_id, text=sorted_users)
    msg = system_time() + ' - User list updated'
    return msg
