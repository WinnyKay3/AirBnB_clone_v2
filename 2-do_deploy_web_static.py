#!/usr/bin/python3
""" Fabric script to distribute an archive to remote web servers"""

from fabric.api import *
import os
from os import path
from datetime import datetime

env.hosts = ['34.204.95.214', '100.26.121.224']
env.user = "ubuntu"


def do_deploy(archive_path):
    ''' distributes an archive file to 2-web servers
    Args:
        archive_path (str): path of archive to distribute
    Returns:
          if file doesnt exist at archive_path or an error occurs - false
          otherwise - true'''
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = os.path.splitext(file)[0]
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    print("New version deployed!")
    return True
