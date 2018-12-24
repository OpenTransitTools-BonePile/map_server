import os
from mustache import template
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


def make_feature(base_dir, data, type_name, style_id):
    """
    make routes feature folder
    """
    # step 1: make feature dir
    feature_path = os.path.join(base_dir, type_name)
    file_utils.mkdir(feature_path)

    # step 2: content
    data['type'] = type_name
    data['style'] = style_id

    # step 3: add featuretype.xml for this feature
    data['featuretype_id'] = "{}-{}-{}-featuretype".format(data['db_name'], data['schema'], type_name)
    type_path = os.path.join(feature_path, 'featuretype.xml')
    with open(type_path, 'w+') as f:
        content = featuretype_template(data)
        f.write(content)

    # step 4: add layer.xml for this feature
    data['layer_id'] = "{}-{}-{}-layer".format(data['db_name'], data['schema'], type_name)
    layer_path = os.path.join(feature_path, 'layer.xml')
    with open(layer_path, 'w+') as f:
        content = layer_template(data)
        f.write(content)

    return {'layer_id': data['layer_id'], 'style_id': style_id}


def make_layergroup(base_dir, data, layers, type_name):
    """
    make layergroup
    """
    # step 1: make feature dir
    layergroup_path = os.path.join(base_dir, 'layergroups')
    file_utils.mkdir(layergroup_path)

    # step 2: content
    data['type'] = type_name
    data['layers'] = layers

    # step 3: add layer.xml for this feature
    xml_path = os.path.join(layergroup_path, type_name + '.xml')
    with open(xml_path, 'w+') as f:
        content = layergroup_template(data)
        f.write(content)


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


def generate_geoserver_config():
    from . import osm_config
    from . import style_config
    from . import transit_config
    transit_config.generate()
    style_config.generate()
    osm_config.generate()
