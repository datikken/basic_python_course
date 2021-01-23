#basic function
def func1():
    print("I'am groot!")

#function that takes arguments
def func2(arg1, arg2):
    print(arg1 + arg2)

def exponentiation(base, exp):
    print(pow(base, exp))

func1()
func2(1,2)

#executes func and prints execution status
print(func1())
print(exponentiation(2,2))