rm nohup.out
rm -rf mapproxy/cache_data
nohup bin/mapproxy serve-develop -b :18080 mapproxy/basemap_map.yaml &
nohup bin/mapproxy serve-develop -b :28080 mapproxy/basemap_aerial.yaml &
