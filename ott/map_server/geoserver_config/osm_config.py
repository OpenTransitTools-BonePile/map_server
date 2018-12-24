from .base import *


def generate(workspace="geoserver/data/workspaces/osm"):
    """ gen geoserver stuff
    """
    osm_layers = [
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
        {'layer': '', 'style': ''},
    ]


    for l in osm_layers:
        # step 1: make the datastore config for the OSM source
        ds_path = os.path.join(workspace, 'datastore.xml')
        with open(ds_path, 'w+') as f:
            content = datastore_template(data)
            f.write(content)

        # step 4: make stop and route feature layers
        r = make_feature(dir_path, data, 'routes', 'RoutesCssStyle')
        s = make_feature(dir_path, data, 'stops',  'StopsCssStyle')


    # step 5: make inclusive layergroups
    make_layergroup(geo_workspace, data, routes_layers, type='routes')
    make_layergroup(geo_workspace, data, stops_layers, type='stops')

    all_layers = []
    all_layers.extend(routes_layers)
    all_layers.extend(stops_layers)
    make_layergroup(geo_workspace, data, all_layers, type='all')
