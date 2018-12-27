from .base import *


def make_id(name, color=None):
    color = color.capitalize() if color else ""
    id = "{}{}CssStyle".format(color, name.capitalize())
    return id


def make_id_from_path(path):
    nc = path.split('/')
    name = nc[0]
    color = None
    if len(nc) > 1:
        color = 2
    return make_id(name, color)


def generate(data_dir="geoserver/data"):
    """
    gen geoserver style .xml files
    will loop thru .css files, and generate .xml based on css formats, etc...
    assumes .css files are either in a type dir (xxx/stuff.css) or type/color dir (yyy/gray/stuff.css)
    """
    # step 1: loop thru all the css style directories
    for css_dir in ['ott', 'osm/gray', 'osm/color']:
        dir = os.path.join(data_dir, 'styles', css_dir)

        # step 2: figure out the color of the style from the dir path
        sep = color = ''
        if '/' in css_dir:
            sep = '_'
            color = css_dir.split('/')[1]

        # step 3: loop thru all the .css files in each dir
        for s in file_utils.listdir(dir):
            if s.endswith(".css"):
                name = s[:-4]
                css_path = os.path.join(dir, s)  # build path to .css file

                # step 4: write out the .xml GS config file
                cfg_path = os.path.join(data_dir, 'styles', color + sep + name + ".xml")
                with open(cfg_path, 'w+') as f:
                    data = {
                        'id': make_id(name, color),
                        'name': name,
                        'path': css_path,
                        'type': 'css'
                    }
                    content = style_config_template(data)
                    f.write(content)
