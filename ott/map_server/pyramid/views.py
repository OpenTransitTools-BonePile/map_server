from pyramid.response import Response
from pyramid.view import view_config

from ott.utils.parse.url.geo_param_parser import SimpleGeoParamParser
from ott.utils.parse.url.stop_param_parser import StopParamParser
from ott.utils.dao import base
from ott.utils import web_utils
from ott.utils import json_utils
from ott.utils import pyramid_utils

import logging
log = logging.getLogger(__file__)


cache_long = 500
system_err_msg = base.ServerError()
session = None
stop_svc_url = "https://maps.trimet.org/ride_ws/stop?stop_id={}"
stop_map_url = "https://maps.trimet.org/ride_ws/stop?stop_id={}"

# https://ride.trimet.org/eapi/ws/V1/    mapimage || stopimage
#   format/png/width/350/height/350/zoom/6/extraparams/format_options=layout:scale/id/2
#   format/png/width/800/height/600/zoom/9/coord/-122.675671,45.420609/extraparams/format_options=layout:place

# /geoserver/wms?service=WMS&version=1.1.0&request=GetMap&layers=hybridOSM&styles=&bbox=-13656617,5703496,-13655897,5703976&srs=EPSG:900913&format=application/openlayers&width=600&height=400

def do_view_config(cfg):
    cfg.add_route('map_url_via_stopid', '/map_url_via_stopid')
    cfg.add_route('map_via_stopid', '/map_via_stopid')


@view_config(route_name='map_url_via_stopid', renderer='string', http_cache=cache_long)
def map_url_via_stopid(request):
    """
    https://maps.trimet.org/ride_ws/stop?id=2&agency=TRIMET
    """
    stop = get_stop(request)
    map_url = ""
    return map_url


@view_config(route_name='map_via_stopid', renderer='string', http_cache=cache_long)
def map_via_stopid(request):
    # import pdb; pdb.set_trace()
    ret_val = get_stop(request)
    return ret_val


def get_stop(request):
    ret_val = get_stop_from_url(request)
    return ret_val


def get_stop_from_url(request):
    ret_val = None
    params = StopParamParser(request)
    if params.stop_id:
        stop_url = stop_svc_url.format(params.stop_id)
        ret_val = json_utils.stream_json(stop_url)
    return ret_val


def get_stop_from_db(session, stop_id, agency_id=None):
    try:
        params = StopParamParser(request)
        ret_val = StopDao.from_stop_params(session, params)
    except NoResultFound, e:
        log.warn(e)
        ret_val = data_not_found
    except Exception as e:
        log.warn(e)
        rollback_session(session)
        ret_val = system_err_msg
    finally:
        close_session(session)

