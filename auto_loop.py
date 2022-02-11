from requests import sessions
import time
from connections import Connections
from main import main

with sessions.Session() as session:
    rocket = Connections.rocket
    while 1:
        main(rocket)
        time.sleep(30.0)
