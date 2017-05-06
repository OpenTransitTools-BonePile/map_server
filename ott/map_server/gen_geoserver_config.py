import os
from mustache import template
from ott.utils import gtfs_utils
from ott.utils import file_utils


template_dir = 'ott/map_server/templates/'

@template(template_dir + 'stores.mustache')
def datastore_template(data):
    """ call the stores template"""
    return data

@template(template_dir + 'featuretype.mustache')
def featuretype_template(data):
    """ call the featuretype template"""
    return data

@template(template_dir + 'layer.mustache')
def layer_template(data):
    """ call the featuretype template"""
    return data


def get_data(db_name='ott', schema='TRIMET', user='geoserve'):
    v = {
        'db_name': db_name,
        'schema': schema,
        'user':  user,
        'minx': -123.1,
        'maxx': -121.1,
        'miny': 44.0,
        'maxy': 47.0,
    }
    return v


def make_feature(base_dir, data, type='routes', style_id='RoutesStyle'):
    """ make routes feature folder
    """
    # step 1: make feature dir
    feature_path = os.path.join(base_dir, type)
    file_utils.mkdir(feature_path)

    # step 2: content
    data['type'] = type
    data['style_id'] = style_id

    # step 3: add layer.xml for this feature
    layer_path = os.path.join(feature_path, 'layer.xml')
    with open(layer_path, 'w+') as f:
        content = layer_template(data)
        f.write(content)

    # step 4: add featuretype.xml for this feature
    type_path = os.path.join(feature_path, 'featuretype.xml')
    with open(type_path, 'w+') as f:
        content = featuretype_template(data)
        f.write(content)


def generate_all(geo_workspace="geoserver/data/workspaces/ott"):
    """ gen geoserver stuff
    """
    feed_list = gtfs_utils.get_feeds_from_config()
    for feed in feed_list:
        # step 1: get meta data and name for this feed
        schema_name = gtfs_utils.get_schema_name_from_feed(feed)
        data = get_data(schema=schema_name)

        # step 2: make datasource folder for each schema
        dir_path = os.path.join(geo_workspace, schema_name)
        file_utils.mkdir(dir_path)

        # step 3: make the datastore config for the source
        ds_path = os.path.join(dir_path, 'datastore.xml')
        with open(ds_path, 'w+') as f:
            content = datastore_template(data)
            f.write(content)

        # step 4: make stop and route feature layers
        make_feature(dir_path, data, 'routes', 'RoutesStyle')
        make_feature(dir_path, data, 'stops',  'StopsStyle')
