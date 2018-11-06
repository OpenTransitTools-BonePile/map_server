map_server
==========

The map_server project contains a [geoserver](http://geoserver.org) config for the OTT project.
  1. [gtfs](ott/loader/gtfs/README.md), which contains routines to cache and compare gtfs feeds.
  1. 


install:
  1. install java 8
  1. git clone https://github.com/OpenTransitTools/map_server.git
  1. cd map_server
  1. scripts/build.sh

run:
  1. scripts/run.sh


Avoid checking <tokens> in: git update-index --assume-unchanged mapproxy/metro_p_state.yaml
  