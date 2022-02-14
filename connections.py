from rocketchat_API.rocketchat import RocketChat
from ldap3 import Connection, SAFE_SYNC
from config import Rchat, Ldap


class Connections:
    rocketchat = RocketChat(Rchat.user, Rchat.passw, server_url=Rchat.url)
    ldap = Connection(Ldap.server,
                      Ldap.user,
                      Ldap.passw,
                      read_only=True,
                      client_strategy=SAFE_SYNC,
                      auto_bind=True)
