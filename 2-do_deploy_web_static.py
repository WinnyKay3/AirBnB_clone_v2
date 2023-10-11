#!/usr/bin/python3
""" Fabric script to distribute an archive to remote web servers"""

from fabric.api import *
import os
from os import path
from datetime import datetime

env.hosts = ["34.204.95.214", "100.26.121.224"]
env.user = "ubuntu"


def do_pack():
    """generate a .tgz archive from the contents of web_static
    folder into a .tgz archive.
    Archive path if successful none upon failure"""
    try:
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        archive_name = "versions/web_static_" + timestamp + ".tgz"
        print("Packing web_static to {}".format(archive_name))
        local("mkdir -p versions")
        local("tar -czvf {} web_static".format(archive_name))
        print(
            "web_static packed: {} -> {}Bytes".format(
                archive_name, path.getsize(archive_name)
            )
        )
        return archive_name
    except Exception:
        return None


def do_deploy(archive_path):
    """distributes an archive file to 2-web servers
    Args:
        archive_path (str): path of archive to distribute
    Returns:
          if file doesnt exist at archive_path or an error occurs - false
          otherwise - true"""
    if os.path.isfile(archive_path) is False:
        return False
    file = os.path.basename(archive_path)
    name = os.path.splitext(file)[0]
    if put(archive_path, "/tmp/{}".format(file), capture=True).failed is True:
        return False
    if (
        run(
            "mkdir -p /data/web_static/releases/{}/".format(name), capture=True
        ).failed
        is True
    ):
        return False
    if (
        run(
            "tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(
                file, name
            ),
            capture=True,
        ).failed
        is True
    ):
        return False
    if run("rm /tmp/{}".format(file), capture=True).failed is True:
        return False
    if (
        run(
            "mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name),
            capture=True,
        ).failed
        is True
    ):
        return False
    if (
        run(
            "rm -rf /data/web_static/releases/{}/web_static".format(name),
            capture=True,
        ).failed
        is True
    ):
        return False
    if run("rm -rf /data/web_static/current", capture=True).failed is True:
        return False
    if (
        run(
            "ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
                name
            ),
            capture=True,
        ).failed
        is True
    ):
        return False
    print("New version deployed!")
    return True
