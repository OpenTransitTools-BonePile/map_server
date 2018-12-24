from .base import *


def generate(workspace="geoserver/data/workspaces/osm", db="osm"):
    """ gen geoserver stuff
    """
    layer_group = []

    # step 1: make the datastore directory
    dir_path = os.path.join(workspace, db)
    file_utils.mkdir(dir_path)

    # step 2: make the datastore config
    ds_path = os.path.join(dir_path, 'datastore.xml')
    data = get_data('osm', 'osm', is_LatLon=False)
    with open(ds_path, 'w+') as f:
        content = datastore_template(data)
        f.write(content)

    # step 3: make layers
    osm_layers = [
        "water",
        "waterway",
        "lakes",

        "forestpark",

        "boundary",
        "settlements",
        "subdistrict",
        "country",
        "county",
        "district",

        "rails",
        "minor_roads",
        "trunk_primary",
        "motorway",
        "roads",
        "pedestrian",

        "buildings",
        "amenity",
    ]
    for l in osm_layers:
        r = make_feature(dir_path, data, l, l.capitalize() + 'CssStyle')
        layer_group.append(r)

    make_layergroup(dir_path, data, layer_group, type_name='map')