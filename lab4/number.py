class Integer(object):
	def __init__(self, number, flag):
		self.f = flag
		self.n = number
	def printInteger(self):
		if self.f == True:	
			print self.n #as it is (+)
		else:
			print self.n * -1
class NegativeInteger(Integer)
	def __init__(self, number,False):
		
if __name__=="__main__":
	test = Integer(8, True)
	test.printInteger()



