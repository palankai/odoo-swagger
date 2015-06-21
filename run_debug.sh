#!/bin/bash

docker build -t odoo-swagger-dev odoo/
docker run -ti --rm -p 8069:8069 -v $(pwd)/addons:/mnt/extra-addons -v $(pwd)/odoo/config:/etc/odoo odoo-swagger-dev openerp-server $@
