from .gen_geoserver_config import *


def generate_all(data_dir="geoserver/data"):
    """ gen geoserver stuff
    """
    # import pdb; pdb.set_trace()
    for type in ['osm', 'ott']:
        dir = os.path.join(data_dir, 'styles', type)
        for s in file_utils.listdir(dir):
            if s.endswith(".css"):

                name = s[:-4]
                cfg_path = os.path.join(data_dir, 'styles', name + ".xml")
                with open(cfg_path, 'w+') as f:
                    data = {
                        'name': name,
                        'cap_name': name.capitalize(),
                        'type': type
                    }
                    content = style_config_template(data)
                    f.write(content)
