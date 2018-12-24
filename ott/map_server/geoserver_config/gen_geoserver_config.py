import os
from mustache import template
from ott.utils import gtfs_utils
from ott.utils import file_utils


template_dir = 'ott/map_server/geoserver_config/templates/'


@template(template_dir + 'stores.mustache')
def datastore_template(data):
    """ call the stores template"""
    return data


@template(template_dir + 'style_config.mustache')
def style_config_template(data):
    """ call the style config template"""
    return data


@template(template_dir + 'featuretype.mustache')
def featuretype_template(data):
    """ call the featuretype template"""
    return data


@template(template_dir + 'layer.mustache')
def layer_template(data):
    """ call the layer template"""
    return data


@template(template_dir + 'layergroup.mustache')
def layergroup_template(data):
    """ call the layergroup template"""
    return data


def get_data(db_name='ott', schema='TRIMET', user='ott'):
    v = {
        'db_name': db_name,
        'schema': schema,
        'user':  user,
        'store_id': "{}-{}-datastore".format(db_name, schema),
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
    data['style'] = style_id

    # step 3: add featuretype.xml for this feature
    data['featuretype_id'] = "{}-{}-{}-featuretype".format(data['db_name'], data['schema'], type)
    type_path = os.path.join(feature_path, 'featuretype.xml')
    with open(type_path, 'w+') as f:
        content = featuretype_template(data)
        f.write(content)

    # step 4: add layer.xml for this feature
    data['layer_id'] = "{}-{}-{}-layer".format(data['db_name'], data['schema'], type)
    layer_path = os.path.join(feature_path, 'layer.xml')
    with open(layer_path, 'w+') as f:
        content = layer_template(data)
        f.write(content)

    return {'layer_id': data['layer_id'], 'style_id': style_id}


def make_layergroup(base_dir, data, layers, type='routes'):
    """ make routes feature folder
    """
    # step 1: make feature dir
    layergroup_path = os.path.join(base_dir, 'layergroups')
    file_utils.mkdir(layergroup_path)

    # step 2: content
    data['type'] = type
    data['layers'] = layers

    # step 3: add layer.xml for this feature
    xml_path = os.path.join(layergroup_path, type + '.xml')
    with open(xml_path, 'w+') as f:
        content = layergroup_template(data)
        f.write(content)


def generate_all(geo_workspace="geoserver/data/workspaces/ott"):
    """ gen geoserver stuff
    """
    # lists for the layergroups.xml config
    routes_layers = []
    stops_layers = []

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
        r = make_feature(dir_path, data, 'routes', 'RoutesCssStyle')
        s = make_feature(dir_path, data, 'stops',  'StopsCssStyle')
        routes_layers.append(r)
        stops_layers.append(s)


    # step 5: make inclusive layergroups
    make_layergroup(geo_workspace, data, routes_layers, type='routes')
    make_layergroup(geo_workspace, data, stops_layers, type='stops')

    all_layers = []
    all_layers.extend(routes_layers)
    all_layers.extend(stops_layers)
    make_layergroup(geo_workspace, data, all_layers, type='all')
