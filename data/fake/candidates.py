from faker import Faker
import pandas as pd

fake = Faker() 

df2 = []

for n in range(3):
    df2.append(list(fake.profile().values()))

df2 = pd.DataFrame(df2, columns=fake.profile().keys())
print(df2)
df2