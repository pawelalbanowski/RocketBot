from requests import sessions
from connections import Connections
from main import main

with sessions.Session() as session:
    rocket = Connections.rocket
    main(rocket)
