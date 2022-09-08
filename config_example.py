from ldap3 import Server


class Ldap:  # constants for LDAP
    uri = ''
    user = ''
    passw = ''
    server = Server(uri)


class Rchat:  # constants for rocketchat
    user = ''
    passw = ''
    url = ''
    welcome_message_id = ''


LOG_FILE = ''
