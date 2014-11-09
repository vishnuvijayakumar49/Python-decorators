def logger(func):
	def inner(*args,**kwargs):
		print "argmnts were :%s,%s" %(args,kwargs)
		return func(*args,**kwargs)
	return inner


@logger
def foo(x,y=2):
	return x*y

foo(5,4)	
