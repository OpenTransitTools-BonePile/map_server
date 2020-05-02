cd geoserver
e="export GEOSERVER_DATA_DIR=$PWD/data"
echo $e
eval $e
rm logs/run.out
nohup bin/startup.sh > logs/run.out &
tail -f logs/run.out
echo "username: admin"
echo "password: geoserver"
##cat $GEOSERVER_DATA_DIR/security/masterpw.info
