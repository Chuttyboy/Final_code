# # dict1 = {0: 'v1', 15: 'v1', 30: 'v1'}
# # dict2 = {0: 'v2', 15: 'v2', 31: 'v2'}
# # dict3 = {}


# # for key in dict1.keys():
# #     import pdb;pdb.set_trace()
# #     if not key in dict2:      
# #         print(key)
# #     else:
# #         print("nothing")

# def Merge(dict1, dict2):
#     res = {**dict1, **dict2}
#     return res
     
# # Driver code
# dict1 = {0: 'v1', 15: 'v1', 30: 'v1'}
# dict2 = {0: 'v2', 15: 'v2', 31: 'v2'}
# dict3 = Merge(dict1, dict2)
# print(dict3)
from collections import defaultdict

d1 = {0: 'v1', 15: 'v1', 30: 'v1'}
d2 = {0: 'v2', 15: 'v2', 31: 'v2'}

dd = defaultdict(list)

for d in (d1, d2): # you can list as many input dicts as you want here
    for key, value in d.items():
        dd[key].append(value)

print(dd)