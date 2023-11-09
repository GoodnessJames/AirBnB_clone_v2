#!/usr/bin/python3
"""
Fabric script to generate a .tgz archive from the contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """
    Packs the contents of the web_static folder into a .tgz archive.
    """
    try:
        if not os.path.exists("versions"):
            local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_name = "web_static_{}.tgz".format(timestamp)
        local("tar -cvzf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except Exception as e:
        return None

