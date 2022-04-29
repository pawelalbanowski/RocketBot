# deprec

from subprocess import run
from time import sleep
from func import log_append, system_time
from pprint import pprint

file_path = "main.py"

restart_timer = 30


def start_script():
    try:
        run("python "+file_path, check=True)
    except:
        handle_crash()


def handle_crash():
    sleep(restart_timer)
    log = system_time() + ' - connection broken, restarting app...'
    pprint(log)
    log_append('log.txt', log)
    start_script()


start_script()
