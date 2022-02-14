from classes import ITMsg, Teams
from config import Rchat


def general_msg_block(team, rocket):  # single block of one team
    block = []
    members = (rocket.groups_members(room_id=team.getId()).json())['members']
    all_members = 0
    members_present = 0
    for member in members:
        if member['name'] != 'Rocket Bot' and member['name'] != 'Super Admin':
            all_members += 1
            match member['status']:
                case 'online':
                    block.append(member['username'])
                    members_present += 1
                case 'away':
                    block.append(member['username'] + ' - zaraz wracam')
                    members_present += 1
                case 'busy':
                    block.append(member['username'] + ' - zajęty')
                    members_present += 1
    sorted_block = sorted(list(map(lambda x: ('- @' + x), block)))
    if sorted_block.count('- @' + team.getKier()) > 0:
        sorted_block.insert(0, sorted_block.pop(sorted_block.index('- @' + team.getKier())))
    present_str = str(members_present) + '/' + str(all_members)
    block_str = '*' + team.header + '* ' + present_str + '\n' + '\n'.join(sorted_block)
    return block_str


def general_it_block(rocket):  # only for IT in general message, since IT is sectioned
    wsparcie = []
    systemy = []
    wsparcie_present = 0
    systemy_present = 0
    for member in ITMsg.wsparcie:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        match presence:
            case 'online':
                wsparcie.append(member)
                wsparcie_present += 1
            case 'away':
                wsparcie.append(member + ' - zaraz wracam')
                wsparcie_present += 1
            case 'busy':
                wsparcie.append(member + ' - zajęty')
                wsparcie_present += 1
    wsparcie_header = '- *SEKCJA WSPARCIA UŻYTKOWNIKÓW* ' + str(wsparcie_present) + '/' + str(len(ITMsg.wsparcie))
    wsparcie_handlers = list(map(lambda x: ('- - @' + x), wsparcie))
    wsparcie_str = wsparcie_header + '\n' + '\n'.join(wsparcie_handlers)
    for member in ITMsg.systemy:
        presence = (rocket.users_get_presence(username=member).json())['presence']
        match presence:
            case 'online':
                systemy.append(member)
                systemy_present += 1
            case 'away':
                systemy.append(member + ' - zaraz wracam')
                systemy_present += 1
            case 'busy':
                systemy.append(member + ' - zajęty')
                systemy_present += 1
    systemy_header = '- *SEKCJA SYSTEMÓW INFORMATYCZNYCH* ' + str(systemy_present) + '/' + str(len(ITMsg.systemy))
    systemy_handlers = list(map(lambda x: ('- - @' + x), systemy))
    systemy_str = systemy_header + '\n' + '\n'.join(systemy_handlers)
    mhandle = ''
    match (rocket.users_get_presence(username=Teams.it.getKier()).json())['presence']:
        case 'online':
            mhandle = '- @' + Teams.it.getKier()
        case 'away':
            mhandle = '- @' + Teams.it.getKier() + ' - zaraz wracam'
        case 'busy':
            mhandle = '- @' + Teams.it.getKier() + ' - zajęty'
    block = '\n*' + Teams.it.getHeader() + '*\n' + mhandle + '\n' + wsparcie_str + '\n' + systemy_str
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
