import numpy as np

def knapsack(price,wt,W):
    n=len(price)
    ratio=[]
    for i in range(n):
        ratio.append((price[i]/wt[i],price[i],wt[i],i))
    ratio.sort(key=lambda x:x[0],reverse=True)
    profit=0
    item=[]
    for ratio,price,w,id in ratio:
        if(w<=W):
            W-=w
            profit+=price
            item.append(id)
    return item , profit
price=(100,250,300,210,260,350)
wt=(10,20,25,30,40,50)
W=100
print(knapsack(price,wt,W))