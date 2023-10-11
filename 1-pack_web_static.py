#!/usr/bin/python3
# compress before sending it

from fabric.api import *
from datetime import datetime


def do_pack():
    ''' generate a .tgz archive from the contents of web_static 
       folder into a .tgz archive.
       Archive path if successful none upon failure'''
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_" + timestamp + ".tgz"
        print("Packing web_static to versions/{}".format(archive_name))
        local("mkdir -p versions")
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception:
        return None
