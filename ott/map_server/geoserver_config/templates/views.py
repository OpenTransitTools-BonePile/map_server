import pystache
import os


def render(template, content):
    renderer = pystache.Renderer()

    # import pdb; pdb.set_trace()
    try:
        # try 1: treat template as a path to a template
        ret_val = renderer.render_path(template, content)
    except FileNotFoundError as e:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        try:
            # try 2: treat template as a template in this current directory
            ret_val = renderer.render_path(os.path.join(dir_path, template), content)
        except FileNotFoundError as e:
            try:
                # try 2b: treat template as a template in this current directory -- but add .mustache ext
                ret_val = renderer.render_path(os.path.join(dir_path, template + ".mustache"), content)
            except Exception as e:
                # try 3: treat template as a string template (will usually render something...)
                ret_val = renderer.render(template, content)

    return ret_val


""" TODO -- not sure what TemplateSpec might be able to do, but adding this here as a research todo item ... """
from pystache import TemplateSpec
class FeatureType(TemplateSpec):
    pass


def main():
    # bin/python ott/map_server/geoserver_config/templates/views.py

    data = {'id': 'FX', 'name': 'Frank X', 'type': 'sub-human', 'path': 'crooked'}
    p = render('style_config', data)
    #p = render('style_config.mustache', data)
    #p = render('ott/map_server/geoserver_config/templates/style_config.mustache', data)
    print(p)


if __name__=='__main__':
    main()
