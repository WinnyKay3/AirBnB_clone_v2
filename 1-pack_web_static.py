#!/usr/bin/python3
# compress before sending it

from fabric.api import *
from datetime import datetime
from os import path

def do_pack():
    ''' generate a .tgz archive from the contents of web_static 
       folder into a .tgz archive.
       Archive path if successful none upon failure'''
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_" + timestamp + ".tgz"
        print("Packing web_static to {}".format(archive_name))
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        print("web_static packed: {} -> {}Bytes".format(archive_name, path.getsize(archive_name)))
        return archive_name
    except Exception:
        return None
