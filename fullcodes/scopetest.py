def test():
    #global b
    b=20
    #global a
    #a=10
    print "Inside test() a=%d"%(a)
    print "Inside test() b=%d"%(b)

a=1
print "Outside test() a=%d"%(a)
test()
print "Outside test() a=%d"%(a)
print "Outside test() b=%d"%(b)
