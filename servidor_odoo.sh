#Solo cuando se corre el servidor con una base de datos nueva
./odoo/odoo-bin --addons-path=./odoo/addons,./enterprise,./custom_addons -d odoo_db -r odoo -w odoo --db_host=127.0.0.1 -i base --limit-time-real 0 --limit-memory-hard 0
#./odoo/odoo-bin --addons-path=./odoo/addons,./enterprise,./custom_addons -d odoo_db -r odoo -w odoo --db_host=127.0.0.1 --limit-time-real 0 --limit-memory-hard 0