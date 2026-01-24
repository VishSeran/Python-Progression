Dict = {"key1": "1", "key2": "2", "key3": "3", "key4": [1,2,3,4]}
print(Dict)
#Append new key to Dict
Dict['key5']= "5"
print(Dict)
#check whether the key is in the Dict

print('key1' in Dict)

Dict["key1"]
print(Dict.keys())

print(Dict.values())


del(Dict["key1"])
print(Dict)