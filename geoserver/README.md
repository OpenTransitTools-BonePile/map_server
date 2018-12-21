geoserver
==========

install:
  1. install java 8
  1. grab geoserver -- https://docs.geoserver.org/latest/en/user/installation/index.html#installation
  1. wget https://build.geoserver.org/geoserver/2.14.x/geoserver-2.14.x-latest-bin.zip
  1. grab css plugin -- https://docs.geoserver.org/latest/en/user/styling/css/install.html
  1. wget https://build.geoserver.org/geoserver/2.14.x/ext-latest/geoserver-2.14-SNAPSHOT-css-plugin.zip
  1. cd geoserver/lib
  1. unzip ../g*css-plugin.zip 
  1. export GEOSERVER_DATA_DIR=/java/DEV/map_server/geoserver/data
  1. cd geoserver/bin
  1. sh startup.sh 

run:
  1. scripts/run.sh
