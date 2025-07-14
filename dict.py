thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
    print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)
thisdict["color"] = "red"
print(thisdict)
thisdict.pop("model")
print(thisdict)