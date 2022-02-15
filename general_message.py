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


def general_it_block(rocket):  # only for IT in general message, since IT is sectioned
    # wsparcie
    wsparcie = []
    wsparcie_present = 0
    for member in ITMsg.wsparcie:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        if present(presence):
            wsparcie.append(presence_translate(member + ' - ' + presence))
            wsparcie_present += 1
    wsparcie_header = '- *SEKCJA WSPARCIA UŻYTKOWNIKÓW* ' + str(wsparcie_present) + '/' + str(len(ITMsg.wsparcie))
    wsparcie_handles = list(map(lambda x: ('- - @' + x), wsparcie))
    wsparcie_str = '{}\n{}'.format(wsparcie_header, '\n'.join(wsparcie_handles))

    # systemy
    systemy = []
    systemy_present = 0
    for member in ITMsg.systemy:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        if present(presence):
            systemy.append(presence_translate(member + ' - ' + presence))
            systemy_present += 1
    systemy_header = '- *SEKCJA SYSTEMÓW INFORMATYCZNYCH* ' + str(systemy_present) + '/' + str(len(ITMsg.systemy))
    systemy_handles = list(map(lambda x: ('- - @' + x), systemy))
    systemy_str = '{}\n{}'.format(systemy_header, '\n'.join(systemy_handles))

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
                    block = general_it_block(rocket)
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
