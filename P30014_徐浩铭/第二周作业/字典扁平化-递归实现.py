# {'a':{'b':1,'c':2}, 'd':{'e':3,'f':{'g':4}}}  ==> {'a.b':1, 'a.c':2, 'd.e':3, 'd.f.g':4}
dict1 = {'a':{'b':1,'c':{'2':555}}, 'd':{'e':3,'f':{'g':{'e':4}}}}
dict2 = {'a':{'b':1,'c':{'2':555}}, 'd':{'e':3,'f':{'g':{'e':4}}}, 'm':{'n':1}}
d = {'a':1}


def dict_flat(dic,newdict=None, prefix=''):
    if newdict is None:
        newdict = {}
    for k, v in dic.items():
        if isinstance(v, dict):      
            dict_flat(v, newdict, prefix+k+'.')
        else:
            newdict[prefix+k] = v
    return newdict
                
print(dict_flat(dict1))
