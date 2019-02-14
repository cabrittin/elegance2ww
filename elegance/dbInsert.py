"""
dbInsert.py

Module for inserting Elegance databases for WormWiring.

Functions:
----------
turn_foreign_keys_off(cur):
    Turns foreign keys off.
object_table(cur):
    Inserts into WW object table.
contin_table(cur):
    Inserts into WW contin table.
relationship_table(cur):
    Inserts into WW relationship table.
image_table(cur):
    Inserts into WW image table.
synapse_relationship_table(cur):
    Inserts into WW synapse_object table.
display_table(cur):
    Inserts into WW display_object table.
"""

def turn_foreign_keys_off(cur):
    """
    Turns foriegn keys off.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    """
    sql = ("SET FOREIGN_KEY_CHECKS=0")
    cur.execute(sql)

def object_table(cur,data):
    """
    Inserts into WW object table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idobject,x,y,idimage,idcontin]
    """
    sql = ("insert into object "
           "(idobject,x,y,idimage,idcontin) "
           "values (%s,%s,%s,%s,%s)")
    cur.executemany(sql,data)
    
def contin_table(cur,data):
    """
    Inserts into WW contin table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idcontin,continname,type]
    """
    sql = ("insert into contin "
           "(idcontin,continname,type) "
           "values (%s,%s,%s)")
    cur.executemany(sql,data)

def relationship_table(cur,data):
    """
    Inserts into WW relationship table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idrelationship,idobject1,idobject2]
    """
    sql = ("insert into relationship "
           "(idrelationship,idobject1,idobject2) "
           "values (%s,%s,%s)")
    cur.executemany(sql,data)

def image_table(cur,data):
    """
    Inserts into WW image table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idimage,imagename,sectionnumber,series]
    """
    sql = ("insert into image "
           "(idimage,imagename,sectionnumber,series) "
           "values (%s,%s,%s,%s)")
    cur.executemany(sql,data)

def synapse_table(cur,data):
    """
    Inserts into WW synapse table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idsynapse,idcontin,idpre,idpost]
    """
    sql = ("insert into synapse "
           "(idsynapse,idcontin,idpre,idpost) "
           "values (%s,%s,%s,%s)")
    cur.executemany(sql,data)

def display_table(cur,data):
    """
    Inserts into WW object table.
    
    Parameters:
    -----------
    cur : MySQLdb cursor
    data : data to insert

    data format: [idobject,x,y,z,cellbody,remarks]
    """
    sql = ("insert into display "
           "(idcontin,idobject1,x1,y1,z1,cellbody1,remarks1,idobject2,x2,y2,z2,cellbody2,remarks2) "
           "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    cur.executemany(sql,data)
