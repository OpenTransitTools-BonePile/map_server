# WSGI module for use with Apache mod_wsgi or gunicorn

# # uncomment the following lines for logging
# # create a log.ini with `mapproxy-util create -t log-ini`
# from logging.config import fileConfig
# import os.path
# fileConfig(r'/mapproxy/log.ini', {'here': os.path.dirname(__file__)})


# docs: https://mapproxy.org/docs/nightly/deployment.html#apache-mod-wsgi

import argparse
from mapproxy.wsgiapp import make_wsgi_app


def make_app(port='', config=''):
    app = make_wsgi_app(config)  # Not sure how to specify port
    return app

def make_args():
    parser = argparse.ArgumentParser(description='Start the map proxy server')
    parser.add_argument('-p', '--port', help='server port')
    parser.add_argument('config', help='MapProxy .yaml config file')
    args = parser.parse_args()
    return args








