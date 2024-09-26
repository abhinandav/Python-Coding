#  Create a dict from string list with the strings as keys and lengths as values

li=['abhinand','thomas','ujwal']
new_dict={}
for i in li:
    new_dict[i]=len(i)

print(new_dict)

new={s:len(s) for s in li}
print(new)

sorted_key=dict(sorted(new.items(),key=lambda x:x[1]))
print(sorted_key)