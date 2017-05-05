from mustache import template

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
    print stores()