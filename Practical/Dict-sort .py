price={'abhinand':21,'thomas':25,'ujwal':24,'jawhar':20,'shamal':23}


# based on value
sorted_price1=dict(sorted(price.items(),key=lambda x:x[1]))
print(sorted_price1)


#based on key
sorted_price2=dict(sorted(price.items(),key=lambda x:x[0]))
print(sorted_price2)




