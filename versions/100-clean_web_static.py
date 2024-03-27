#!/usr/bin/python3
"""Deletes an out of date archibe."""
impoer os
from fabric.api import *
env.hosts = ["3.80.18.107", "100.25.132.152"]


def do_clean(number=0):
    """Deletes an out_of_date archive."""
    #number number of archives
    #keep most recent if if 0 or 1
    #if 2 keep most recent.
    #delete unnecessary archives
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archive.pop() for i in range(number)]
    with lcd("versions"):
        local("rm./{}".format(a)) for a in archives

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
	archives = [a for a in archives if "web_atatic_" in a]
	archives.pop() for i in range(number)
	run("rm -rf ./{}".format(a)) for a in archives
