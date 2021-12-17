fib = [0,1,1,2,3,5,8,13,21,34,55,89,144]
def convert(val, units):
	global fib
	val = round(abs(val))
	def fib_find():
		global fib
		fib += [fib[-1]+fib[-2]]

	def helper(val):
		if val < 1:
			return [1];
		if val == 1:
			return [2];
		i = -1;
		while fib[i] > val:
			i-=1
		return [i]+helper(val-fib[i])


	out = 0;
	while fib[-1] <= val:
			fib_find	()
	y = helper(val)
	if units == "mi":
		x = 1.609344
		for i in y:
			out += fib[i+1]
		
	elif units == "km":
		x = 0.62137119224
		for i in y:
			out += fib[i-1]
		
	else:	
		print("No")
	
	

	print("Guess: ", out)
	print("Actual :", x*val)
	print("Error: ", (out-x*val)/(x*val))