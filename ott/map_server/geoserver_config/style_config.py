from .base import *


def make_id(name, color=None):
    color = color.capitalize() if color else ""
    id = "{}{}CssStyle".format(name.capitalize(), color)
    return id


def make_id_from_path(path):
    nc = path.split('/')
    name = nc[0]
    color = None
    if len(nc) > 1:
        color = 2
    return make_id(name, color)


def generate(data_dir="geoserver/data"):
    """ gen geoserver stuff
    """

    # import pdb; pdb.set_trace()
    for type in ['ott', 'osm/gray', 'osm/color']:
        dir = os.path.join(data_dir, 'styles', type)
        for s in file_utils.listdir(dir):
            if s.endswith(".css"):
                path = s[:-4]
                name = path.replace('/', '_')
                cfg_path = os.path.join(data_dir, 'styles', name + ".xml")
                with open(cfg_path, 'w+') as f:
                    data = {
                        'id': make_id_from_path(path),
                        'name': name,
                        'path': cfg_path,
                        'type': 'css'
                    }
                    content = style_config_template(data)
                    f.write(content)
