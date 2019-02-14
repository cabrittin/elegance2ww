"""
dbGet.py

Module for formatting Elegance databases for WormWiring.

Functions:
----------
object_table(cur):
    Returns array of formatted WW object table.
contin_table(cur):
    Returns array of formatted WW contin table.
relationship_table(cur):
    Returns array of formatted WW relationship table.
image_table(cur):
    Returns array of formatted WW image table.
synapse_relationship_table(cur):
    Returns array of formatted WW synapse_object table.
display_tablescur):
    Returns the WW display_object table.
"""

def object_table(cur):
    """
    Returns relevant object table fields for WW object table.

    Parameters:
    -----------
    cur : MySQLdb cursor

    """
    sql = ("select OBJ_Name,OBJ_X,OBJ_Y,IMG_Number,CON_Number "
            "from object")
    cur.execute(sql)
    return [list(a) for a in cur.fetchall()]

def contin_table(cur):
    """
    Returns relevant contin table fields for WW contin table.

    Parameters:
    -----------
    cur : MySQLdb cursor

    """
    sql = ("select CON_Number,CON_AlternateName,type "
            "from contin "
            "where CON_Remarks like '%%OK%%'")
    cur.execute(sql)
    return [list(a) for a in cur.fetchall()]

def relationship_table(cur):
    """
    Returns relevant relationship table fields for WW relationship table.

    Parameters:
    -----------
    cur : MySQLdb cursor

    """
    sql = ("select relID,ObjName1,ObjName2 "
            "from relationship")
    cur.execute(sql)
    return [list(a) for a in cur.fetchall()]

def image_table(cur):
    """
    Returns relevant image table fields for WW image table.

    Parameters:
    -----------
    cur : MySQLdb cursor

    """
    sql = ("select IMG_Number,IMG_File,IMG_SectionNumber,IMG_Series "
            "from image")
    cur.execute(sql)
    return [list(a) for a in cur.fetchall()]

def synapse_table(cur):
    """
    Returns relevant synapse data for WW synapse_relationship table.

    Paramters:
    ----------
    cur : MySQLdb cursor

    """
    sql = ("select object.OBJ_Name,object.CON_Number, object.fromObj,object.toObj "
            "from object "
            "join contin on contin.CON_Number = object.CON_Number "
            "where contin.type in ('chemical','electrical')")
    
    cur.execute(sql)
    data = []
    for a in cur.fetchall():
        post = a[3].split(',')
        for p in post:
            if p and a[2]:
                data.append([a[0],a[1],a[2],p])
    return data

def display_table(cur):
    """ 
    Returns the WW display_object.

    Parameters:
    -----------
    cur : MySQLdb cursor

    """

    sql = ("select continNum,objName1,x1,y1,z1,cellbody1,remarks1,"
           "objName2,x2,y2,z2,cellbody2,remarks2 "
           "from display2")
    cur.execute(sql)
    return [d for d in cur.fetchall()]

    
