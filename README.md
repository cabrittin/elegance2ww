# elegance2ww
Formats Elegance databases to be compatible with WormWiring

The script create_db.sql is a myslq script that will create the new database. Prior to use, the default database name _db_name_ needs
to be replaced with the new database name. This can be done with the provded bash script. 

```
$ ./create_dabase.sh NEW_DB_NAME
```
The mysql username in the script will need to adjusted as needed. 

The python script requires Python3 and MySQLdb librarary
```
pip install mysqlclient
```

Then run the pyhton script
```
python ELEGANCE_DB_NAME WW_DB_NAME
```
