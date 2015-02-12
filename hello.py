'''
In this examples we used Python 2.x because most
of the machines in class had that version, but from
our next class, we will be using 3.x

Esp. you can see our print doesn't have ()
'''

print "Hello Word!"

#Python is Dynamically
#typed
x = "30"
print x * 3

x = 30
print x * 3

#sample function

def my_sum(a,b):
	return a + b

y = input("Value of A: ")
z = input("Value of B: ")

total = my_sum(y,z)

print "A + B = ",total
