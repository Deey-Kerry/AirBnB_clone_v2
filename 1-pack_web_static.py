#!usr/bin/python3
"""
sets up your web servers for the deployment of web_static
"""

from fabric.api import local
import time
from datetime import date


def do_pack():
    """Generates contents of folder"""
    filename = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz web_static/"
              .format(filename))

        return "versions/web_static_{}.tgz".format(filename)

    except Exception as e:
        return None
