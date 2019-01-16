"""
toWW.py

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
synapse_object_table(cur):
    Returns array of formatted WW synapse_object table.
display_table(cur):
    Returns array of formatted WW display table.
"""

def object_table(cur):
    sql = ("select OBJ_Name,CON_Number,IMG_Number,OBJ_X,OBJ_Y "
            "from object")
    cur.execute(sql)
    return cur.fetchall()
