from classes import ITMsg, Teams
from config import Rchat
from func import presence_translate, present


def general_msg_block(team, rocket):  # single block of one team
    block = []
    all_members = 0
    members_present = 0
    members = (rocket.groups_members(room_id=team.getId()).json())['members']
    for member in members:
        if member['name'] != 'Rocket Bot' and member['name'] != 'Super Admin':
            all_members += 1
            if present(member['status']):
                block.append(presence_translate(member['username'] + ' - ' + member['status']))
                members_present += 1
    sorted_block = sorted(list(map(lambda x: ('- @' + x), block)))
    if sorted_block.count('- @' + team.getKier()) > 0:
        sorted_block.insert(0, sorted_block.pop(sorted_block.index('- @' + team.getKier())))
    present_str = str(members_present) + '/' + str(all_members)
    block = '*{}* {}\n{}'.format(team.header, present_str, '\n'.join(sorted_block))
    return block


def it_block(rocket, team, header):
    block = []
    members_present = 0
    for member in team:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        if present(presence):
            block.append(presence_translate(member + ' - ' + presence))
            members_present += 1
    full_header = '- *' + header + '* ' + str(members_present) + '/' + str(len(team))
    handles = list(map(lambda x: ('- - @' + x), block))
    block = '{}\n{}'.format(full_header, '\n'.join(handles))
    return block


def full_it_block(rocket):  # only for IT in general message, since IT is sectioned
    wsparcie_str = it_block(rocket, ITMsg.wsparcie, 'SEKCJA WSPARCIA UŻYTKOWNIKÓW')
    systemy_str = it_block(rocket, ITMsg.systemy, 'SEKCJA SYSTEMÓW INFORMATYCZNYCH')

    # kierownik
    presence = (rocket.users_get_presence(username=Teams.it.getKier()).json())['presence']
    mhandle = presence_translate('- @{} - {}'.format(Teams.it.getKier(), presence))

    # całość
    block = '\n*{}*\n{}\n{}\n{}'.format(Teams.it.getHeader(), mhandle, wsparcie_str, systemy_str)
    return block


def general_message(rocket):  # in ListaUzytkownikow
    groups = (rocket.groups_list_all().json())['groups']
    administracja = []
    szpital = []
    ignore = [Teams.akredytacja.getHeader()]
    for group in groups:
        for team in Teams().teams:
            if team.getHeader() not in ignore:
                if group['name'] == team.getName() and team.getName() == 'IT':
                    block = full_it_block(rocket)
                    administracja.append(block)
                elif group['name'] == team.getName():
                    block = general_msg_block(team, rocket)
                    match team.getCategory():
                        case 'administracja':
                            administracja.append(block)
                        case 'szpital':
                            szpital.append(block)
    sorted_users = '\n\n'.join(sorted(administracja)) + '\n\n\n' + '\n\n'.join(sorted(szpital))
    rocket.chat_update(room_id='GENERAL', msg_id=Rchat.welcome_message_id, text=sorted_users)
    msg = "User list updated"
    return msg
