"""
fill_synapse_format.py

Populates the synapse format table for the given database

@author Christopher Brittin
@date 7 August 2019
"""

import argparse
import MySQLdb

SQLLOGIN = '~/.my.cnf'

def get_synapse(synId):
    sql = ("select preCont.continname as pre,"
        "group_concat(distinct(postCont.continname) separator ',') as post,"
        "synapse.idcontin as synId,"
        "min(image.sectionnumber) as sectNum1,"
        "max(image.sectionnumber) as sectNum2,"
        "count(distinct(synapse.idsynapse)) as sects "
        "from synapse "
        "join object as preObj on preObj.idobject = synapse.idpre "
        "join contin as preCont on preCont.idcontin = preObj.idcontin "
        "join object as postObj on postObj.idobject = synapse.idpost "
        "join contin as postCont on postCont.idcontin = postObj.idcontin "
        "join object as synObj on synObj.idobject = synapse.idsynapse "
        "join image on image.idimage = synObj.idimage "
        "join contin as synCont on synCont.idcontin = synObj.idcontin "
        "where synapse.idcontin = %s" %synId)
    cur.execute(sql)
    return cur.fetchone()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('db',
                        action="store",
                        help= "Database to be populated")
 

    params = parser.parse_args()

    con = MySQLdb.connect(read_default_file=SQLLOGIN,db=params.db)
    cur = con.cursor()


    #Get all distinct synapse contins
    sql = "select distinct(idcontin) from synapse"
    cur.execute(sql)
    contins = [a[0] for a in cur.fetchall()]
   
    syn = []
    for c in contins:
        s = get_synapse(c)
        if not s[3]: continue
        syn.append(s)

    
    #Insert into synapse_format table
    sql = ("insert into synapse_format "
           "(pre,post,idcontin,sectNum1,sectNum2,sects) "
           "values (%s,%s,%s,%s,%s,%s)")
    cur.executemany(sql,syn)

    con.commit()

    con.close()




