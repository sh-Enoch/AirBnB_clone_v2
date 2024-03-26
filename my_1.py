#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """generate a .tgz archive from webstatic folder."""
    local("sudo mkdir -p versions")
    now_t = datetime.now()

    dt_format = now_t.strftime("%Y%m%d%H%M%S")

    local(f"tar -cvzf versions/web_static_{dt_format}.tgz web_static")
    path = f"versions/web_static_{dt_format}.tgz"
    
    path = f"versions/web_static_{dt_format}.tgz"
    size_f = os.path.getsize(path)

    print(f"web_static packed: versions/web_static_{dt_format}.tgz -> {size_f}Bytes")
    return  path
