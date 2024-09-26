var_value = 5
var_ref = 10
var_shr = 5
print("value of var_value at start: ", var_value)
print("value of var_ref at start: ", )
print("value of var_shr at start: ", var_shr)

def passValue(var_value_func):
	var_value_func = 10

def passRef(var_ref_func):
	# var_ref_func.append(10) 
	var_ref_func+=1
	print('inside passref',var_ref_func)

def passShr(var_shr_func):
	# var_shr_func.append(10) 
	var_shr_func+=1
	print('inside shref',var_shr_func)


print("\nAfter applying Evaluation techniques")
passValue(var_value)
print("value of var_value at end: ", var_value)

passRef(var_ref)
print("value of var_ref at end: ", var_ref)

passShr(var_shr)
print("value of var_shr at end: ", var_shr)