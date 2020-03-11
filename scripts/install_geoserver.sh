VER=2.16

EXT_PLUGINS="imagemosaic-jdbc-plugin css-plugin vectortiles-plugin"

# !!! NOTE: mbstyle-plugin.zip moves to EXT_ in 2.17
COM_PLUGINS="mbstyle-plugin"

if [ -d "geoserver" ];
then
    rm -rf geoserver-old
    mv geoserver geoserver-old
fi

if [ ! -f "geoserver.zip" ];
then
    curl "https://build.geoserver.org/geoserver/$VER.x/geoserver-$VER.x-latest-bin.zip" > geoserver.zip

    # see: https://build.geoserver.org/geoserver/master/ext-latest/
    for p in $EXT_PLUGINS
    do
        curl "https://build.geoserver.org/geoserver/$VER.x/ext-latest/geoserver-$VER-SNAPSHOT-$p.zip" > ${p}.zip
    done

    # see: https://build.geoserver.org/geoserver/master/community-latest/
    for p in $COM_PLUGINS
    do
        curl "https://build.geoserver.org/geoserver/$VER.x/community-latest/geoserver-$VER-SNAPSHOT-$p.zip" > ${p}.zip
    done
fi

unzip geoserver.zip
mv geoserver-$VER-SNAPSHOT geoserver

for p in $EXT_PLUGINS $COM_PLUGINS
do
  unzip $p -d geoserver/webapps/geoserver/WEB-INF/lib/
done

rm -rf geoserver/data
rm -rf geoserver/data_dir
if [ -d ".git/" ]; then
  git restore -s@ -SW  -- geoserver
  git update-index --assume-unchanged geoserver/data/*.xml
fi
echo "cd geoserver"
echo "bin/startup.sh > run.out &"
echo "export GEOSERVER_DATA_DIR=/java/DEV/map_server/geoserver/data"
echo "cat \$GEOSERVER_DATA_DIR/security/masterpw.info"
