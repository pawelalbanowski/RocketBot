from rocketchat_API.rocketchat import RocketChat
from ldap3 import Connection, SAFE_SYNC
from classes import ITMsg, Teams
from config import Rchat, Ldap
from datetime import datetime
import json


conn = Connection(Ldap.server, Ldap.user, Ldap.passw, read_only=True, client_strategy=SAFE_SYNC, auto_bind=True)
rocket = RocketChat(Rchat.user, Rchat.passw, server_url=Rchat.url)


def system_time():
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y, %H:%M:%S')
    return 'System time: ' + date_time


def json_read(file):
    read_json_file = open(file, 'r')
    json_data = json.load(read_json_file)
    read_json_file.close()
    return json_data


def json_write(file, data):
    write_json = json.dumps(data, indent=4)
    write_file = open(file, 'w')
    write_file.write(write_json)
    write_file.close()
    return


def log_append(file, data):  # append to log file
    file = open(file, 'a')
    file.write(data + '\n')
    file.close()
    return


def general_msg_block(team, header):  # single block of one team
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


def general_it_block():  # only for IT in general message, since IT is sectioned
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


def general_message():  # in ListaUzytkownikow
    groupsobj = rocket.groups_list_all().json()
    groups = groupsobj['groups']
    sorted_users = []
    for group in groups:
        match group['name']:
            case Teams.it.name:
                block = general_it_block()
                sorted_users.insert(0, block)
            case Teams.place.name:
                header = 'PŁACE'
                block = general_msg_block(Teams.place, header)
                sorted_users.insert(3, block)
            case Teams.kadry.name:
                header = 'KADRY'
                block = general_msg_block(Teams.kadry, header)
                sorted_users.insert(2, block)
            case Teams.ksiegowosc.name:
                header = 'KSIĘGOWOŚĆ'
                block = general_msg_block(Teams.ksiegowosc, header)
                sorted_users.insert(1, block)
            case Teams.dnm.name:
                header = 'NADZÓR MEDYCZNY'
                block = general_msg_block(Teams.dnm, header)
                sorted_users.insert(4, block)
            case Teams.dla.name:
                header = 'LOGISTYCZNO ADMINISTRACYJNY'
                block = general_msg_block(Teams.dla, header)
                sorted_users.insert(5, block)
            case Teams.inwentaryzacja.name:
                header = 'INWENTARYZACJA'
                block = general_msg_block(Teams.inwentaryzacja, header)
                sorted_users.insert(6, block)
            case Teams.zaopatrzenie.name:
                header = 'ZAOPATRZENIE'
                block = general_msg_block(Teams.zaopatrzenie, header)
                sorted_users.insert(7, block)
            case Teams.orgprawny.name:
                header = 'ORGANIZACYJNO-PRAWNY'
                block = general_msg_block(Teams.orgprawny, header)
                sorted_users.insert(8, block)
            case Teams.wew.name:
                header = 'ODDZIAŁ CHORÓB WEWNĘTRZNYCH'
                block = general_msg_block(Teams.wew, header)
                sorted_users.insert(9, block)
    sorted_users = '\n\n'.join(sorted(sorted_users))
    rocket.chat_update(room_id='GENERAL', msg_id=Rchat.welcome_message_id, text=sorted_users)
    msg = "User list updated"
    return msg
