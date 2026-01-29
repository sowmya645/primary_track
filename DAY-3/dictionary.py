dict={"k1":"v1","k2":"v2"}
print(dict["k1"])
print(dict.get("k2"))
print(dict.keys())
print(dict.values())
for key,value in dict.items():
    print(f"key: {key}   value: {value}")
dict.update({"k1":"v"})
print(dict)
dict.pop("k1")
print(dict)