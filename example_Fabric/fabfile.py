# coding: utf-8
# use fab get_file:/var/www/config_gofraud.txt
from fabric.api import get, env, roles, run, cd
import os
env.roledefs['test'] = ['www-data@192.168.0.199']


def production_env():
    """Окружение для продакшена"""
    # Локальный путь до файла с ключами
    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')]
    env.user = 'www-data'  # На сервере будем работать из под пользователя "git"
    env.project_root = '/var/www/Projects'  # Путь до каталога проекта (на сервере)
    # env.shell = '/usr/local/bin/bash -c'  # Используем шелл отличный от умолчательного (на сервере)
    env.python = '/usr/bin/python'  # Путь до python (на сервере)


@roles('test')
def get_file(f):
    production_env()
    get(f)
