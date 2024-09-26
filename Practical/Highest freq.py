# def fq(a):
#     max=0
#     ele=None
#     f={}
#     for i in a:
#         if i not in f:
#             f[i]=1
#         else:
#             f[i]+=1
#             if(f[i]>max):
#                 max=f[i]
#                 ele=i
#     return ele

# print(fq('abhiand'))



from collections import Counter
s='kjnhfheinfsammisjfnwdekldmiiiiiiiiiiiiednnennnenkml'
counter=Counter(s)
ele=max(counter,key=counter.get)
print(ele,counter[ele])
