import pandas as pd
if __name__=='__main__':
    x = pd.read_csv("./qicc/key.csv")
    for y in x.values:
        print(y)