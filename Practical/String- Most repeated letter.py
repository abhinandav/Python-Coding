s='my name is abhinand and iam living in kerala.kerala is a state in indai and it is most beautiful'
from collections import Counter
fq=Counter(s.split())
repeated=max(fq,key=fq.get)
print(repeated)