mapproxy...


How to:
 1. get info on a WMS layer: bin/mapproxy-util autoconfig --capabilities=http://imagery.oregonexplorer.info/arcgis/services/NAIP_2016/NAIP_2016_WM/ImageServer/WMSServer?request=GetCapabilities&service=WMS
 1. write a .yaml config file for mapproxy
 1. run the demo:
  - bin/mapproxy serve-develop mapproxy/<your mp config>.yaml
  - http://localhost:8080/demo

Examples:
 - https://talks.omniscale.de/2016/foss4g/mapproxy/#1
 - https://github.com/rzymek/geoproxy/blob/master/isok_cieniowanie.yaml

HQ Tiles:
 - https://lists.osgeo.org/pipermail/mapproxy/2018-May/002741.html
 - https://github.com/Runalyze/Runalyze/issues/2036
 - http://a.tile.stamen.com/toner-lite/12/652/1576@2x.png
 - http://a.tile.stamen.com/toner-lite/12/652/1576%402x.png
 - https://www.w3schools.com/tags/ref_urlencode.asp

Auth:
 - https://lists.osgeo.org/pipermail/mapproxy/2018-Septemppber/002815.html
 - https://mapproxy.org/docs/nightly/auth.html#limited-to


Other:
 - https://github.com/openmaptiles
 - https://www.maptiler.com/blog/2018/10/timemachine-atlas.html
 - https://timemachineatlas.eu/ ... cool

 - https://www.mapbox.com/mapbox-gl-js/example/animate-a-line/