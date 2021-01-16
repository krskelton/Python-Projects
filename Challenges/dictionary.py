myDictionary = {"fname": "Kristin", "lname": "Skelton"}
print(myDictionary.get("fname"))
myDictionary["fname"] = "Cali"
print(myDictionary.get("fname"))
myDictionary["phone"] = "111-111-1111"
print(myDictionary)
myDic2 = {"employee1":{"fname": "Kristin", "lname": "Skelton"}, "employee2": {"fname":"Seth", "lname": "Neubauer"}}
print(myDic2)
thisDic = dict.fromkeys(myDictionary)
print(thisDic)
