from classes import Teams
from pprint import pprint

teams = Teams()
for attr, value in teams.__dict__.items():
    pprint(attr, )
teams = [a for a in dir(teams) if not a.startswith('__')]

