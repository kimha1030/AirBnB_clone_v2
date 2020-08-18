#!/usr/bin/python3
"""Script that generates a .tgz archive from web_static folder"""
import time
import os
from os import path
from fabric.api import *


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
