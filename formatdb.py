"""
formatdb.py

Elegance database to WormWiring database

created: Christopher Brittin
date: 07 February 2018

"""

import argparse
import elegance

def image_object_relation(img,obj):
    nimg = len(img)
    idImg = dict([(img[i][0],i) for i in range(nimg)])
    _obj,_img = [],[]
    for o in obj:
        if o[3] in idImg:
            o[3] = idImg[o[3]]
            _obj.append(o)
    for i in img:
        if i[0] in idImg:
            i[0] = idImg[i[0]]
            i[1] = i[1].split('.')[0]
            _img.append(i)
    return _img,_obj

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('fromdb',
                        action="store",
                        help= "Elegance database")
   
    parser.add_argument('todb',
                        action="store",
                        help="WormWiring database"
                        )
    
    params = parser.parse_args()

    
    con = elegance.connect.default(params.fromdb)
    cur = con.cursor()

    img = elegance.dbGet.image_table(cur)
    contin = elegance.dbGet.contin_table(cur)
    obj = elegance.dbGet.object_table(cur)
    rel = elegance.dbGet.relationship_table(cur)
    syn = elegance.dbGet.synapse_table(cur)
    display = elegance.dbGet.display_table(cur)

    con.close()
    
    img,obj = image_object_relation(img,obj)

    con = elegance.connect.default(params.todb)
    cur = con.cursor()

    elegance.dbInsert.turn_foreign_keys_off(cur)
    elegance.dbInsert.object_table(cur,obj)
    elegance.dbInsert.contin_table(cur,contin)
    elegance.dbInsert.relationship_table(cur,rel)
    elegance.dbInsert.image_table(cur,img)
    elegance.dbInsert.synapse_table(cur,syn)
    elegance.dbInsert.display_table(cur,display)
   
    con.commit()

    
