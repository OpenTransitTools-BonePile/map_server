mapproxy...


How to:
 1. get info on a WMS layer: bin/mapproxy-util autoconfig --capabilities=http://imagery.oregonexplorer.info/arcgis/services/NAIP_2016/NAIP_2016_WM/ImageServer/WMSServer?request=GetCapabilities&service=WMS
 1. write a .yaml config file for mapproxy
 1. run the demo:
  - bin/mapproxy serve-develop mapproxy/<your mp config>.yaml
  - http://localhost:8080/demo

Examples:
 - https://github.com/rzymek/geoproxy/blob/master/isok_cieniowanie.yaml

