from classes import ITMsg, Teams
from config import Rchat
from func import presence_translate, present, system_time
from connections import Connections
from ldap3 import SUBTREE


def general_message(rocket):  # in ListaUzytkownikow
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
                        active_member += ' (oddziałowa/y)'
                    active_member = presence_translate(f"{active_member} - {member['status']}")
                    block.append(active_member)

        sorted_block = sorted(list(map(lambda x: f'- @{x}', block)))
        if sorted_block.count(f'- @{team.get_kier()}') > 0:
            sorted_block.insert(0, sorted_block.pop(sorted_block.index(f'- @{team.get_kier()}')))

        present_str = f'{str(len(sorted_block))}/{str(all_members)}'
        sorted_block = '\n'.join(sorted_block)
        block = f'*{team.get_header().lower().title()}* {present_str}\n{sorted_block}'
        return block

    def it_block(rocket, team, header):
        block = []

        for member in team:
            presence = (rocket.users_get_presence(username=member).json())['presence']
            if present(presence):
                block.append(presence_translate(f'{member} - {presence}'))

        full_header = f'- *{header}* {str(len(block))}/{str(len(team))}'
        handles = '\n'.join(list(map(lambda x: ('- - @' + x), block)))
        block = f'{full_header}\n{handles}'
        return block

    def full_it_block(rocket):  # only for IT in general message, since IT is sectioned
        wsparcie_str = it_block(rocket, ITMsg.wsparcie, 'Sekcja Wsparcia Użytkowników')
        systemy_str = it_block(rocket, ITMsg.systemy, 'Sekcja Systemów Informatycznych')

        # kierownik
        it_kier_presence = (rocket.users_get_presence(username=Teams.it.get_kier()).json())['presence']
        it_kier_handle = presence_translate(f'- @{Teams.it.get_kier()} - {it_kier_presence}')

        # całość
        block = f'\n*{Teams.it.get_header().lower().title()}*\n{it_kier_handle}\n{wsparcie_str}\n{systemy_str}'
        return block

    def sec_groups():
        def sec_group_list(searchbase):
            try:
                conn = Connections.ldap
                search_filter = '(objectclass=group)'
                _, _, response, _ = conn.search(
                    search_base=searchbase,
                    search_filter=search_filter,
                    attributes=['member'],
                    search_scope=SUBTREE)

                members = response[0]['attributes']['member']
                members = list(map(lambda a: a.split(',', 1)[0].split('=', 1)[1], members))
                return members
            except RecursionError:
                return []

        sekr_base = 'CN=DL_SekretarkiOddzialow,OU=SzpPracownicy,OU=Medyczni,OU=Pracownicy,OU=Szwajcarska,DC=szpitalsm,DC=local'
        oddz_base = 'CN=DL_PielegniarkiOddzialowe,OU=SzpPracownicy,OU=Medyczni,OU=Pracownicy,OU=Szwajcarska,DC=szpitalsm,DC=local'

        sec_groups_list = {
            'sekr': sec_group_list(sekr_base),
            'oddz': sec_group_list(oddz_base)
        }

        return sec_groups_list

    groups = (rocket.groups_list_all().json())['groups']
    administracja = []
    szpital = []
    ignore = [Teams.akredytacja]
    sec_groups = sec_groups()

    for group in groups:
        for team in Teams().teams:
            if team not in ignore:
                if group['name'] == team.get_name() and team.get_name() == 'IT':
                    full_block = full_it_block(rocket)
                    administracja.append(full_block)
                elif group['name'].lower() == team.get_name().lower():
                    full_block = general_msg_block(team, rocket, sec_groups['sekr'], sec_groups['oddz'])
                    match team.get_category():
                        case 'administracja':
                            administracja.append(full_block)
                        case 'szpital':
                            szpital.append(full_block)

    sorted_administracja = '\n\n'.join(sorted(administracja))
    sorted_szpital = '\n\n'.join(sorted(szpital))
    sorted_users = f"---*ADMINISTRACJA*---\n{sorted_administracja}\n\n\n---*SZPITAL*---\n\n{sorted_szpital}"
    rocket.chat_update(room_id='GENERAL', msg_id=Rchat.welcome_message_id, text=sorted_users)
    msg = f'{system_time()} - User list updated'
    return msg
