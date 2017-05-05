from mustache import template
from ott.utils import gtfs_utils


template_dir = 'ott/map_server/templates/'

@template(template_dir + 'stores.mustache')
def stores(db_name='ott', schema='TRIMET', user='geoserve'):
    v = {
        'db_name': db_name,
        'schema': schema,
        'user':  user,
    }
    return v

def generate_all():
    feed_list = gtfs_utils.get_feeds_from_config()
    for feed in feed_list:
        feed_name = gtfs_utils.get_schema_name_from_feed(feed)
        print feed_name
        #print stores()
