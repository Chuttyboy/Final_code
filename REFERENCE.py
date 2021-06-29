#method 1
a = ["v1_0001.jpg","v1_0002.jpg","v1_0003.jpg","v1_0017.jpg","v1_0015.jpg",]
b = ["v2_0001.jpg","v2_0002.jpg","v2_00015.jpg","v2_0004.jpg","v2_0003.jpg"]


c = sorted(a)
print(c)

#method 2
a = ['v1_0001.jpg', 'v1_00015.jpg', 'v1_00017.jpg', 'v1_0002.jpg', 'v1_0003.jpg']
a.sort(key=lambda x: int(x.split('v1_')[1].split('.jpg')[0]))
print(a)
b = ["v2_0001.jpg","v2_0002.jpg","v2_00015.jpg","v2_0004.jpg","v2_0003.jpg"]
a.sort(key=lambda x: int(x.split('v1_')[1].split('.jpg')[0]))
print(a)

#method 2

import re
def sorted_nicely( l ):
    """ 
    Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)
              
# Driver code
a = ["v1_0001.jpg","v1_0002.jpg","v1_0003.jpg","v1_00017.jpg","v1_00015.jpg"]
print(sorted_nicely(a))