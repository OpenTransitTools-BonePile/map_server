from ott.utils.parse.cmdline import gtfs_cmdline

import logging
log = logging.getLogger(__file__)


stop_svc_url = "https://maps.trimet.org/ride_ws/stop?stop_id={}"

stop_tmpl = {
    "name": "{stop_name}",
    "id": "{stop_id}",
    "details": [
        {
            "title": "Info",
            "html": "<h3>{stop_name}<span class='subh5'><br/> Stop ID {stop_id}</span></h3><p>&nbsp;</p><p><h4>Served by</h4><ul>{route_stops}</ul></p>"
        },
        {
            "title": "Trip Planning",
            "html": "<span class='tabTripPlan'><a onclick=\"trimet.map.AppControls.setFrom('{stop_name}', '{lon}', '{lat}, '{lon}', '{lat}');\" href='#set-from' target=''>Plan a trip from here</a><br/><a onclick=\"trimet.map.AppControls.setTo ('{stop_name}', '{lon}', '{lat}', '{lon}', '{lat}');\" href='#set-to' target=''>Plan a trip to here</a><br/><a href='javascript: window.open(\"https://trimet.org/arrivals/trackerpopup.html?locationID={stop_id}&amp;x=13&amp;y=13\", \"TransitTracker\",\"toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=442,left=10,top=10,height=330\").focus()'>Next Arrivals from TransitTracker</a><br/></span>"
        },
        {
            "title": "Street View",
            "html": "{sv_link}"
        },
        {
            "title": "Amenities",
            "html": "<p><ul>{amenities}/ul></p>"
        }
    ]
}

attributes_tmpl = "<li>{}</li>"
route_stop_tmpl = "<li><a href='#' onClick='trimet.widget.feature.RouteGridStatic.singleton.find({route_id}, null, true);'>{route_name}</a></li>"


def make_stop_popup_json(stop):
    sv_link = geo_utils.sv_iframe(stop.lat, stop.lon)



def main():
    parser = gtfs_cmdline.simple_stop_route_parser()
    cmd = parser.parse_args()

    print cmd


if __name__ == '__main__':
    main()