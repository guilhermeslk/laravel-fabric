import os.path

from fabric.api import env, cd, sudo
from fabric.colors import green, red

# Apache Config
path = "/var/www"

def deploy(app, app_env):
    with cd("%s/%s/%s" % (path ,app, app_env)):
        sudo("php artisan down")
        sudo("git pull")
        sudo("/usr/local/bin/composer update")
        sudo("php artisan up")
        print green("Application Deployed Successfully.")

