import numpy as np
import pandas as pd
Study_Hours_Per_Week=[15, 10, 12, 8]
student=["Laila","Daaku","Devara","Ram"]
id=[12,21,43,62]
dict2={"Study_Hours_Per_Week":Study_Hours_Per_Week, "student":student,"id":id}
print(dict2)
df=pd.DataFrame(dict2)
print(df)