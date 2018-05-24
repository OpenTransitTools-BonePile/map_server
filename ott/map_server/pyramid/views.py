from pyramid.response import Response
from pyramid.view import view_config

from ott.utils.parse.url.geo_param_parser import SimpleGeoParamParser
from ott.utils.parse.url.stop_param_parser import StopParamParser
from ott.utils.dao import base
from ott.utils import web_utils
from ott.utils import pyramid_utils

import logging
log = logging.getLogger(__file__)


cache_long = 500
system_err_msg = base.ServerError()
session = None
stop_svc_url = "https://maps.trimet.org/ride_ws/stop?stop_id={}"


def do_view_config(cfg):
    cfg.add_route('map_url_via_stopid', '/map_url_via_stopid')
    cfg.add_route('map_via_stopid', '/map_via_stopid')


@view_config(route_name='map_url_via_stopid', renderer='string', http_cache=cache_long)
def map_url_via_stopid(request):
    """
    https://maps.trimet.org/ride_ws/stop?id=2&agency=TRIMET
    """
    return get_stop_from_url(request)


@view_config(route_name='map_via_stopid', renderer='string', http_cache=cache_long)
def map_via_stopid(request):
    ret_val = get_stop(request)
    # import pdb; pdb.set_trace()
    #return pyramid_utils.dao_response(ret_val)
    return ret_val


def get_stop(request):
    ret_val = get_stop_from_url(request)
    return ret_val


def get_stop_from_url(request):
    ret_val = None
    params = StopParamParser(request)
    if params.stop_id:
        ret_val = stop_svc_url.format(params.stop_id)
        #ret_val = web_utils.get(stop_svc_url.format(params.stop_id))
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

