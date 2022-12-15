user_info={
'name':"vikash",
'age':25,
"gender":"male",
"college":"LPU"}
# if 'name'in user_info:
#     print('present')
# else:
#     print('absent')
# if "vikash" in user_info.values():
#     print('present')
# else:
#     print('absent')
# user_info_keys = user_info.keys()
# print(user_info.keys())
# print(type(user_info_keys))
# for i in user_info:
#     print(user_info[i])
# user_items=user_info.items()
# print(user_items)
# print(type(user_items))
for i ,j in user_info.items():
    print(f" {i}  = {j}")
