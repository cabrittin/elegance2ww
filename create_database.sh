#!/bin/bash

oldName=_db_name_
newName=$1
sql=create_db.sql

sed -i "s/${oldName}/${newName}/g" "$sql"
mysql -uroot -p < $sql
sed -i "s/${newName}/${oldName}/g" "$sql"

