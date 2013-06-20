try:  
	raise EOFError("aa", "bb")  
except RuntimeError, e:  
	print "[RuntimeErro]: ", e  
except EOFError, e:  
	print "[EOFError]: ", e  
except Exception, e:  
	print "[Error]: ", e  
finally:  
	print "final"  
