map_server project
==========

The map_server project contains a [geoserver](http://geoserver.org) config for the OTT project.
  1. [gtfs](ott/loader/gtfs/README.md), which contains routines to cache and compare gtfs feeds.
  1. 

Setup
--- 
 1. pre-req: install java 8, python 2.7 or python 3.6, install buildout
 1. use loader or osm project to load osm2pgsql tables into postgres
 1. git clone https://github.com/OpenTransitTools/map_server.git
 1. cd map_server
 1. buildout

Geoserver
--- 
To get geoserver up and running: see geoserver/README.md

 1. cd map_server
 1. bin/generate_geoserver_config
 1. export GEOSERVER_DATA_DIR=${PWD}/geoserver/data 
 1. cd to dir where you'd like to install geoserver
 1. <some path>/map_server/scripts/install_geoserver.sh
 1. cd geoserver
 1. bin/startup.sh 

Map Proxy
-----

Avoid checking <tokens> in: git update-index --assume-unchanged mapproxy/metro_p_state.yaml
