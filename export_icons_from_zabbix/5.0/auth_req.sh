#!/bin/bash

curl -H "Content-type: application/json-rpc" -X POST http://YOUR-ZABBIX-URL/api_jsonrpc.php -d'
{
    "jsonrpc": "2.0",
    "method": "user.login",
    "params": {
        "user": "YOUR-ZABBIX-USER",
        "password": "YOUR-ZABBIX-PASSWORD"
    },
    "id": 1
}'
