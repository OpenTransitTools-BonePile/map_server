if [ -d "geoserver" ];
then
    rm -rf geoserver-old
    mv geoserver geoserver-old
fi

if [ ! -f "geoserver.zip" ];
then
    curl "https://build.geoserver.org/geoserver/2.14.x/geoserver-2.14.x-latest-bin.zip" > geoserver.zip
    curl "https://build.geoserver.org/geoserver/2.14.x/ext-latest/geoserver-2.14-SNAPSHOT-css-plugin.zip" > css.zip
fi

unzip geoserver.zip
mv geoserver-2.14-SNAPSHOT geoserver
unzip css.zip -d geoserver/webapps/geoserver/WEB-INF/lib/
rm -rf geoserver/data
rm -rf geoserver/data_dir

echo "cd geoserver"
echo "bin/startup.sh > run.out &"
echo "export GEOSERVER_DATA_DIR=/java/DEV/map_server/geoserver/data"
echo "cat \$GEOSERVER_DATA_DIR/security/masterpw.info"