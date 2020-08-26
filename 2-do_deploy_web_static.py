#!/usr/bin/python3
"""Script that generates a .tgz archive from web_static folder"""
import time
import os
from os import path
from fabric.api import *

env.user = "ubuntu"
env.hosts = ['34.75.231.107', '35.243.154.138']


def do_pack():
    """Method that generate a .tgz archive"""
    time_str = time.strftime('%Y%m%d%H%M%S')
    new_file = 'versions/web_static_' + time_str + '.tgz'
    if not os.path.isdir('versions'):
        local("mkdir -p versions")
    local('tar -czvf ' + new_file + ' web_static')
    if os.path.exists(new_file):
        return new_file
    else:
        return None


def do_deploy(archive_path):
    """Method that distributes to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        list_file = archive_path.split("/")
        name_ext = list_file[1].split(".")
        put(archive_path, "/tmp/" + list_file[1])
        run("sudo mkdir -p /data/web_static/releases/" + name_ext[0] + "/")
        run("sudo tar -xzf /tmp/" +
            list_file[1] +
            "-C /data/web_static/releases/" +
            name_ext[0] +
            "/")
        run("sudo rm /tmp/" + list_file[1])
        run("sudo mv /data/web_static/releases/" +
            name_ext[0] +
            "/web_static/* /data/web_static/releases/" +
            name_ext[0] +
            "/")
        run("sudo rm -rf /data/web_static/releases/" +
            name_ext[0] + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s /data/web_static/releases/" +
            name_ext[0] + "/ /data/web_static/current")
        put("versions/" + list_file[1], "/tmp/" + list_file[1])
        run("sudo mkdir -p /data/web_static/releases/" + name_ext[0] + "/")
        run("sudo tar -xzf /tmp/" +
            list_file[1] +
            " -C /data/web_static/releases/" +
            name_ext[0] +
            "/")
        run("sudo rm /tmp/" + list_file[1])
        run("sudo mv /data/web_static/releases/" +
            name_ext[0] +
            "/web_static/* /data/web_static/releases/" +
            name_ext[0] +
            "/")
        run("sudo rm -rf /data/web_static/releases/" +
            name_ext[0] + "/web_static")
        run("sudo rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/" +
            name_ext[0] + "/ /data/web_static/current")
        return True
    except:
        return False
