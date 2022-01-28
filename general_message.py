from classes import ITMsg, Teams
from config import Rchat


def general_msg_block(team, header, rocket):  # single block of one team
    block = []
    members_unformatted = rocket.groups_members(room_id=team.getId()).json()
    members = members_unformatted['members']
    all_members = 0
    members_present = 0
    for member in members:
        if member['name'] != 'Rocket Bot' and member['name'] != 'Super Admin':
            match member['status']:
                case 'offline':
                    all_members += 1
                #     handle = '- @' + member['username'] + ' :black_circle:'
                #     block.append(handle)
                case 'online':
                    handle = '- @' + member['username']  # + ' :tennis:'
                    block.append(handle)
                    members_present += 1
                    all_members += 1
                case 'away':
                    handle = '- @' + member['username'] + ' - zaraz wracam'  # ' :hourglass:'
                    block.append(handle)
                    members_present += 1
                    all_members += 1
                case 'busy':
                    handle = '- @' + member['username'] + ' - zajęty'  # ' :red_circle:'
                    block.append(handle)
                    members_present += 1
                    all_members += 1
    sorted_block = sorted(block)
    if sorted_block.count('- @' + team.getKier()) > 0:
        sorted_block.insert(0, sorted_block.pop(sorted_block.index('- @' + team.getKier())))
    present_str = str(members_present) + '/' + str(all_members)
    block_str = '*' + header + '* ' + present_str + '\n' + '\n'.join(sorted_block)
    return block_str


def general_it_block(rocket):  # only for IT in general message, since IT is sectioned
    wsparcie = []
    systemy = []
    wsparcie_members = ITMsg.wsparcie
    systemy_members = ITMsg.systemy
    wsparcie_present = 0
    systemy_present = 0
    for member in wsparcie_members:
        presence = rocket.users_get_presence(username=member).json()
        match presence['presence']:
            # case 'offline':
            #     handle = '- - @' + member + ' :black_circle:'
            #     wsparcie.append(handle)
            case 'online':
                handle = '- - @' + member  # + ' :tennis:'
                wsparcie.append(handle)
                wsparcie_present += 1
            case 'away':
                handle = '- - @' + member + ' - zaraz wracam'  # ' :hourglass:'
                wsparcie.append(handle)
                wsparcie_present += 1
            case 'busy':
                handle = '- - @' + member + ' - zajęty'  # ' :red_circle:'
                wsparcie.append(handle)
                wsparcie_present += 1
    wsparcie_header = '- *SEKCJA WSPARCIA UŻYTKOWNIKÓW* ' + str(wsparcie_present) + '/' + str(len(wsparcie_members))
    wsparcie_str = wsparcie_header + '\n' + '\n'.join(wsparcie)
    for member in systemy_members:
        presence = rocket.users_get_presence(username=member).json()
        match presence['presence']:
            # case 'offline':
            #     handle = '- - @' + member + ' :black_circle:'
            #     systemy.append(handle)
            case 'online':
                handle = '- - @' + member  # + ' :tennis:'
                systemy.append(handle)
                systemy_present += 1
            case 'away':
                handle = '- - @' + member + ' - zaraz wracam'  # ' :hourglass:'
                systemy.append(handle)
                systemy_present += 1
            case 'busy':
                handle = '- - @' + member + ' - zajęty'  # ' :red_circle:'
                systemy.append(handle)
                systemy_present += 1
    systemy_header = '- *SEKCJA SYSTEMÓW INFORMATYCZNYCH* ' + str(systemy_present) + '/' + str(len(systemy_members))
    systemy_str = systemy_header + '\n' + '\n'.join(systemy)
    mpresence = rocket.users_get_presence(username='mdomanski').json()
    match mpresence['presence']:
        # case 'offline':
        #     mhandle = '- - @mdomanski' + ' :black_circle:'
        case 'online':
            mhandle = '- - @mdomanski'  # + ' :tennis:'
        case 'away':
            mhandle = '- - @mdomanski' + ' - zaraz wracam'  # ' :hourglass:'
        case 'busy':
            mhandle = '- - @mdomanski' + ' - zajęty'  # ' :red_circle:'
    block = '\n*INFORMATYKA*\n' + mhandle + '\n' + wsparcie_str + '\n' + systemy_str
    return block


def general_message(rocket):  # in ListaUzytkownikow
    groupsobj = rocket.groups_list_all().json()
    groups = groupsobj['groups']
    administracja = []
    oddzialy = []
    for group in groups:
        match group['name']:
            case Teams.it.name:
                block = general_it_block(rocket)
                administracja.append(block)
            case Teams.place.name:
                header = 'PŁACE'
                block = general_msg_block(Teams.place, header, rocket)
                administracja.append(block)
            case Teams.kadry.name:
                header = 'KADRY'
                block = general_msg_block(Teams.kadry, header, rocket)
                administracja.append(block)
            case Teams.ksiegowosc.name:
                header = 'KSIĘGOWOŚĆ'
                block = general_msg_block(Teams.ksiegowosc, header, rocket)
                administracja.append(block)
            case Teams.dnm.name:
                header = 'NADZÓR MEDYCZNY'
                block = general_msg_block(Teams.dnm, header, rocket)
                administracja.append(block)
            case Teams.dla.name:
                header = 'LOGISTYCZNO ADMINISTRACYJNY'
                block = general_msg_block(Teams.dla, header, rocket)
                administracja.append(block)
            case Teams.inwentaryzacja.name:
                header = 'INWENTARYZACJA'
                block = general_msg_block(Teams.inwentaryzacja, header, rocket)
                administracja.append(block)
            case Teams.zaopatrzenie.name:
                header = 'ZAOPATRZENIE'
                block = general_msg_block(Teams.zaopatrzenie, header, rocket)
                administracja.append(block)
            case Teams.orgprawny.name:
                header = 'ORGANIZACYJNO-PRAWNY'
                block = general_msg_block(Teams.orgprawny, header, rocket)
                administracja.append(block)
            case Teams.wew.name:
                header = 'ODDZIAŁ CHORÓB WEWNĘTRZNYCH'
                block = general_msg_block(Teams.wew, header, rocket)
                oddzialy.append(block)
    sorted_users = '\n\n'.join(sorted(administracja)) + '\n\n\n' + '\n\n'.join(sorted(oddzialy))
    rocket.chat_update(room_id='GENERAL', msg_id=Rchat.welcome_message_id, text=sorted_users)
    msg = "User list updated"
    return msg
