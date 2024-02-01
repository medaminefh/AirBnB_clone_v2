#!/usr/bin/python3
"""Fabric script that distributes an archive to your web
servers, using the function do_deploy."""
from fabric.api import local, put, run, env
from datetime import datetime
from os import path


env.hosts = ['54.82.132.211', '100.25.194.199']
env.user = 'ubuntu'
env.key_filename = "secret_key"

def do_pack():
    """Function to generate a .tgz archive from the contents of the web_static folder."""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    path = "versions/web_static_{}.tgz".format(date)
    try:
        local("tar -cvzf {} web_static".format(path))
        return path
    except:
        return None
    

def do_deploy(archive_path):
    """Function to distribute an archive to your web servers."""
    if not path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        name = archive_path.split("/")[-1]
        name2 = name.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}".format(name2))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(name, name2))
        run("rm /tmp/{}".format(name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name2, name2))
        run("rm -rf /data/web_static/releases/{}/web_static".format(name2))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name2))
        return True
    except:
        return False


def deploy():
    """Function to deploy"""
    path_pack = do_pack()
    if path_pack is None:
        return False
    return do_deploy(path)
