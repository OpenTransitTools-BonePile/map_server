# WSGI module for use with Apache mod_wsgi or gunicorn

# # uncomment the following lines for logging
# # create a log.ini with `mapproxy-util create -t log-ini`
# from logging.config import fileConfig
# import os.path
# fileConfig(r'/mapproxy/log.ini', {'here': os.path.dirname(__file__)})


# docs: https://mapproxy.org/docs/nightly/deployment.html#apache-mod-wsgi

import argparse
from mapproxy.wsgiapp import make_wsgi_app
from ott.utils import file_utils
from ott.utils import template_utils
from ott.utils.config_util import ConfigUtil


def make_app(port='', config=''):
    app = make_wsgi_app(config)  # Not sure how to specify port
    return app

def make_args():
    parser = argparse.ArgumentParser(description='Start the map proxy server')
    parser.add_argument('-p', '--port', help='server port')
    parser.add_argument('config', help='MapProxy .yaml config file')
    args = parser.parse_args()
    return args


def set_tokens(name='token'):
    cfg = ConfigUtil(ini="mapproxy.ini")
    import pdb; pdb.set_trace()
    tok = cfg.get(name, section="metro")
    if tok:
        dir = file_utils.get_file_dir(__file__)
        template_utils.apply_kv_to_files(key=name, value=tok, dir_path=dir, ext=".yaml")


if __name__ == '__main__':
    set_tokens()