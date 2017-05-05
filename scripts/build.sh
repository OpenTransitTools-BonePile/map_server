if [ ! -f "geoserver/bin/xxx.jar" ];
then
    wget http://sourceforge.net/projects/geoserver/files/GeoServer/2.11.0/geoserver-2.11.0-bin.zip
fi

echo "##############################################"
echo "# to run the code generator                  #"
echo "#                                            #"
echo "# java -jar lib/swagger-codegen-cli.jar help #"
echo "#                                            #"
echo "##############################################"

echo "https://github.com/swagger-api/swagger-codegen?ref=producthunt#overview"

langs=(java javascript python html dynamic-html)
for l in "${langs[@]}"
do
   mkdir -p bindings/$l
   echo java -jar lib/swagger-codegen-cli.jar generate -i swagger.yaml -l $l -o bindings/$l
   java -jar lib/swagger-codegen-cli.jar generate -i swagger.yaml -l $l -o bindings/$l
done
