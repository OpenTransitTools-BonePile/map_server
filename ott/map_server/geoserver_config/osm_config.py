from .base import *


def generate(workspace="geoserver/data/workspaces/osm"):
    """ gen geoserver stuff
    """
    # step 1: make the datastore config for the OSM source
    ds_path = os.path.join(workspace, 'datastore.xml')
    data = get_data('osm', 'osm')
    with open(ds_path, 'w+') as f:
        content = datastore_template(data)
        f.write(content)

    # step 2: make layers
    osm_layers = [
        {'layer': 'amenity',       'style': 'amenity'},
        {'layer': 'boundary',      'style': 'boundary'},
        {'layer': 'buildings',     'style': 'buildings'},
        {'layer': 'country',       'style': 'country'},
        {'layer': 'county',        'style': 'county'},
        {'layer': 'district',      'style': 'district'},
        {'layer': 'forestpark',    'style': 'forestpark'},
        {'layer': 'lakes',         'style': 'lakes'},
        {'layer': 'minor_roads',   'style': 'minor_roads'},
        {'layer': 'motorway',      'style': 'motorway'},
        {'layer': 'pedestrian',    'style': 'pedestrian'},
        {'layer': 'rails',         'style': 'rails'},
        {'layer': 'roads',         'style': 'roads'},
        {'layer': 'settlements',   'style': 'settlements'},
        {'layer': 'subdistrict',   'style': 'subdistrict'},
        {'layer': 'trunk_primary', 'style': 'trunk_primary'},
        {'layer': 'water',         'style': 'water'},
        {'layer': 'waterway',      'style': 'waterway'},
    ]

    for l in osm_layers:
        r = make_feature(workspace, data, l['layer'], l['style'].capitalize() + 'CssStyle')
