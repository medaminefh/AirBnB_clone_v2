#!/usr/bin/python3
"""Fabric script that distributes an archive to your web servers, using the function do_deploy."""

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

def deploy():
    """Function to deploy"""
    path = do_pack()
    if path is None:
        return False
    return do_deploy(path)
