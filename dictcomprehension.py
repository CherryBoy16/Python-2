dict2={"daaku":12,"gamechanger":10,"sankranthi":14}
r={key:value for key,value in dict2.items()}
keys = ["daaku", "gamechanger", "sankranthi"]
values = [12, 10, 14]
t = {key: value for key, value in zip(keys, values)}
print(r,t)