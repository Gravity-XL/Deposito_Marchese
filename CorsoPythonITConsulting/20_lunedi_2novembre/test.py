import pandas as pd
df = pd.DataFrame({"citta": ["Roma", "Milano", "Roma", "Napoli ", "Como"]})
print(pd.get_dummies(df["citta"]).astype(int))