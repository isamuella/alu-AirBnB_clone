#!/usr/bin/python3
"""Fabric script that will distribute an archive to your web servers"""
from fabric.api import env, put, run
from os.path import exists

env.hosts = ["44.203.2.87", "3.83.161.239"]
env.user = "ubuntu"
env.key = "~/.ssh/school_rsa"


def do_deploy(archive_path):
    """Function to distribute an archive to your web servers"""
    if not exists(archive_path):
        return False
    try:
        file_name = archive_path.split("/")[-1]
        name = file_name.split(".")[0]
        path_name = "/data/web_static/releases/" + name
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(path_name))
        run('tar -xzf /tmp/{} -C {}/'.format(file_name, path_name))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(path_name, path_name))
        run("rm -rf {}/web_static".format(path_name))
        run('rm -rf /data/web_static/current')
        run('ln -s {}/ /data/web_static/current'.format(path_name))
        return True
    except Exception:
        return False
