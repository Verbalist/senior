# coding: utf-8
import os
from fabric.api import run, env, cd, roles

# Списком можно перечислить несколько серверов, которые у вас считаются "продакшеном"
env.roledefs['test'] = ['www-date@192.168.0.199']


def production_env():
    """Окружение для продакшена"""
    # Локальный путь до файла с ключами
    env.key_filename = [os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')]
    env.user = ''  # На сервере будем работать из под пользователя "git"
    env.project_root = '/var/www/Projects/vtiger'  # Путь до каталога проекта (на сервере)
    env.shell = '/usr/local/bin/bash -c'  # Используем шелл отличный от умолчательного (на сервере)
    env.python = '/usr/bin/python3'  # Путь до python (на сервере)


@roles('test')
def deploy():
    production_env()  # Инициализация окружения
    with cd(env.project_root):  # Заходим в директорию с проектом на сервере
        run('git pull origin master')  # Пуляемся из репозитория

        # run('find . -name "*.mo" -print -delete')  # Чистим старые скомпиленные файлы gettext'а
        # run('{} manage.py compilemessages'.format(env.python))  # Собираем новые файлы gettext'а
        # run('{} manage.py collectstatic --noinput'.format(env.python))  # Собираем статику


@roles('test')
def pip_install():
    production_env()
    run('{pip} install --upgrade -r {filepath}'.format(pip=env.pip,
        filepath=os.path.join(env.project_root, 'requirements.txt')))
