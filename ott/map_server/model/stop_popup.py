
from ott.utils import geo_utils
from ott.utils.parse.cmdline import gtfs_cmdline

from ott.map_server.model import stop_data

import logging
log = logging.getLogger(__file__)


# todo: get ths from config
stop_svc_url = "https://maps.trimet.org/ride_ws/stop?stop_id={}"


def make_legacy_stop_popup_json(stop):
    """
    make the json for stop popups on old ride.trimet.org
    """

    # step 1: make amenities html string
    amenities = ""
    if stop['has_amenities'] is True:
        amenity_tmpl = "<li>{}</li>"
        for a in stop['amenities']:
            amenities = amenities + amenity_tmpl.format(a)

    # step 2: make route stops html string
    route_stops = ""
    route_stop_tmpl = "<li><a href='#' onClick='trimet.widget.feature.RouteGridStatic.singleton.find({route_id}, null, true);'>{name}</a></li>"
    for r in stop['routes']:
        route_stops = route_stops + route_stop_tmpl.format(**r)

    # step 3: break out some basic stop vars
    stop_name = stop['name']
    stop_id = stop['stop_id']
    lat = stop['lat']
    lon = stop['lon']

    # step 4: couple of html templates
    info_tmpl = "<h3>{stop_name}<span class='subh5'><br/> Stop ID {stop_id}</span></h3><p>&nbsp;</p><p><h4>Served by</h4><ul>{route_stops}</ul></p>"
    trip_tmpl = "<span class='tabTripPlan'><a onclick=\"trimet.map.AppControls.setFrom('{stop_name}', '{lon}', '{lat}, '{lon}', '{lat}');\" href='#set-from' target=''>Plan a trip from here</a><br/><a onclick=\"trimet.map.AppControls.setTo ('{stop_name}', '{lon}', '{lat}', '{lon}', '{lat}');\" href='#set-to' target=''>Plan a trip to here</a><br/><a href='javascript: window.open(\"https://trimet.org/arrivals/trackerpopup.html?locationID={stop_id}&amp;x=13&amp;y=13\", \"TransitTracker\",\"toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=442,left=10,top=10,height=330\").focus()'>Next Arrivals from TransitTracker</a><br/></span>"

    # step 5: make the json for the stop popup
    popup_json = {
        "name": stop_name,
        "id": stop_id,
        "details": [
            {
                "title": "Info",
                "html": info_tmpl.format(stop_name=stop_name, stop_id=stop_id, route_stops=route_stops)
            },
            {
                "title": "Trip Planning",
                "html": trip_tmpl.format(stop_name=stop_name, stop_id=stop_id, route_stops=route_stops, lat=lat, lon=lon)
            },
            {
                "title": "Street View",
                "html": geo_utils.sv_iframe(lat, lon)
            },
            {
                "title": "Amenities",
                "html": "<p><ul>{}/ul></p>".format(amenities)
            }
        ]
    }
    return popup_json


def main():
    parser = gtfs_cmdline.simple_stop_route_parser()
    cmd = parser.parse_args()
    stop = stop_data.get_stop(cmd.stop_id, cmd.agency_id)
    json = make_legacy_stop_popup_json(stop)
    print json


if __name__ == '__main__':
    main()