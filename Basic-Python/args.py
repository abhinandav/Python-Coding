def sumofAll(*args,**kwargs):
    for arg in args:
        print('arg-',arg)
    for k,v in kwargs.items():
        print(k,'-->',v)


sumofAll([1,2,3,4],{'five':5,'six':6})