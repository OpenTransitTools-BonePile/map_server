import os
from mustache import template
from ott.utils import gtfs_utils
from ott.utils import file_utils


template_dir = 'ott/map_server/templates/'

@template(template_dir + 'stores.mustache')
def stores(db_name='ott', schema='TRIMET', user='geoserve'):
    v = {
        'db_name': db_name,
        'schema': schema,
        'user':  user,
    }
    return v

def generate_all(geo_workspace="geoserver/data/workspaces/ott"):
    feed_list = gtfs_utils.get_feeds_from_config()
    for feed in feed_list:
        feed_name = gtfs_utils.get_schema_name_from_feed(feed)
        dir_path = os.path.join(geo_workspace, feed_name)
        file_path = os.path.join(dir_path, 'datastore.xml')
        file_utils.mkdir(dir_path)

        with open(file_path, 'w+') as f:
            content = stores(schema=feed_name)
            f.write(content)

