#!/bin/bash

echo "START /custom-cont-init.d Script"
sed -i "/listen\ \[\:\:\]\:/d" /config/nginx/site-confs/default.conf
echo "END /custom-cont-init.d Script"
