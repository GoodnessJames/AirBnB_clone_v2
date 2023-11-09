#!/usr/bin/python3
<<<<<<< HEAD
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

=======
# Fabfile to generates a .tgz archive from the contents of web_static.
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
>>>>>>> b75aba04b4265dd3a132b142f4d807ee35238dca
