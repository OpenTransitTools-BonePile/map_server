from ott.utils import json_utils

import logging
log = logging.getLogger(__file__)


stop_svc_url = "https://maps.trimet.org/ride_ws/stop?detailed&stop_id={}"


def get_stop(stop_id, agency_id=None, session=None):
    if session:
        ret_val = get_stop_from_db(session, stop_id, agency_id)
    else:
        ret_val = get_stop_from_url(stop_id, agency_id)
    return ret_val


def get_stop_from_url(stop_id, agency_id):
    ret_val = None
    stop_url = stop_svc_url.format(stop_id)
    ret_val = json_utils.stream_json(stop_url)
    return ret_val


def get_stop_from_db(session, stop_id, agency_id=None):
    try:
        ret_val = StopDao.from_stop_id(session, stop_id)
    except NoResultFound as e:
        log.warn(e)
        ret_val = data_not_found
    except Exception as e:
        log.warn(e)
        rollback_session(session)
        ret_val = system_err_msg
    finally:
        close_session(session)
    return ret_val
