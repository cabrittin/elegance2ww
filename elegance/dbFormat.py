"""
dbFormat.py

Formats elegance database to WormWiring format

created: Christopher Brittin
date: 07 February 2019

"""


def image_object_relation(img,obj):
    nimg = len(img)
    idImg = dict([(img[i][0],i) for i in range(nimg)])
    _obj,_img = [],[]
    for o in obj:
        o[3] = idImg[o[3]]
        _obj.append(o)
    for i in img:
        i[0] = idImg[i[0]]
        i[1] = i[1].split('.')[0]
        _img.append(i)
    return _img,_obj




