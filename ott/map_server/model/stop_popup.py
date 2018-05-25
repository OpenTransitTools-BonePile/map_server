
s = {
    "name": "{stop_name}",
    "id": "{stop_id}",
    "details": [
        {
            "title": "Info",
            "html": "<h3>{stop_name}<span class='subh5'><br/> Stop ID {stop_id}</span></h3><p>&nbsp;</p><p><h4>Served by</h4><ul>{route_stops}</ul></p>"
        },
        {
            "title": "Trip Planning",
            "html": "<span class='tabTripPlan'><a onclick=\"trimet.map.AppControls.setFrom('{stop_name}', '{lon}', '{lat}, '{lon}', '{lat}');\" href='#set-from' target=''>Plan a trip from here</a><br/><a onclick=\"trimet.map.AppControls.setTo  ('A Ave & Chandler', '7643542.9', '646962.2', '-122.6756705529', '45.420609122');\" href='#set-to'   target=''>Plan a trip to here</a><br/><a href='/html/map/ve.html?lat=45.420609122&amp;lon=-122.6756705529&amp;title=A Ave & Chandler&amp;description=Lake Oswego' target='_blank'>Bird's Eye View from Microsoft Bing</a><br/><a href='javascript: window.open(\"http://trimet.org/arrivals/trackerpopup.html?locationID=2&amp;x=13&amp;y=13\", \"TransitTracker\",\"toolbar=no,location=no,directories=no,status=no,menubar=no,scrollbars=yes,resizable=yes,width=442,left=10,top=10,height=330\").focus()'>Next Arrivals from TransitTracker</a><br/></span>"
        },
        {
            "title": "Street View",
            "html": geo_utils.sv_iframe(lat, lon)
        },
        {
            "title": "Amenities",
            "html": "<p><ul>{}/ul></p>"
        }
    ]
}

attributes_tmpl = "<li>{}</li>"
route_stop_tmpl = "<li><a href='#' onClick='trimet.widget.feature.RouteGridStatic.singleton.find(37, null, true);'>37-Lake Grove</a> </li><li><a href='#' onClick='trimet.widget.feature.RouteGridStatic.singleton.find({route_id}, null, true);'>{route_name}</a></li>"