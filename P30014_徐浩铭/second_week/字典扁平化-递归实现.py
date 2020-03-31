# {'a':{'b':1,'c':2}, 'd':{'e':3,'f':{'g':4}}}  ==> {'a.b':1, 'a.c':2, 'd.e':3, 'd.f.g':4}
dict1 = {'a':{'b':1,'c':{'2':555}}, 'd':{'e':3,'f':{'g':{'e':4}}}}
dict2 = {'a':{'b':1,'c':{'2':555}}, 'd':{'e':3,'f':{'g':{'e':4}}}, 'm':{'n':1}}
d = {'a':1}



def dict_flat(dic, interval='.', *, newdict=None, prefix=''):
    """
    第一个参数是待扁平化的字典，第二个参数是分隔符，剩下的参数不用管
    返回值是已扁平化的新字典，老字典保持不变，可重复使用，而不变质。
    """
    if newdict is None:
        newdict = {}
    for k, v in dic.items():
        if isinstance(v, dict):      
            dict_flat(v, newdict=newdict, prefix=prefix+k+interval)
        else:
            newdict[prefix+k] = v
    return newdict
                
dict_flat(dict1)