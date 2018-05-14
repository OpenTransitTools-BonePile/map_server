from pyramid.response import Response
from pyramid.view import view_config

from ott.utils.parse.url.geo_param_parser import SimpleGeoParamParser
from ott.utils.dao import base

import logging
log = logging.getLogger(__file__)


cache_long = 500
system_err_msg = base.ServerError()


def do_view_config(cfg):
    cfg.add_route('map_via_stopid', '/map_via_stopid')
    cfg.add_route('map_via_stopid_url', '/map_via_stopid_url')


@view_config(route_name='map_via_stopid', renderer='string', http_cache=cache_long)
def map_via_stopid(request):
    return "HI"


@view_config(route_name='map_via_stopid_url', renderer='string', http_cache=cache_long)
def map_via_stopid_url(request):
    return "MY"

