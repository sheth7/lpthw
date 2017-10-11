print "Enter n:",
n = int (raw_input())
def fib(n):
    i=1
    a=0
    b=1
    c=0
    if (n==1):
        print "nth fib number is:",a
    elif (n==2):
        print "nth fib number is:",b
    else:
        while (i<n):
            c=a+b
            a=b
            b=c
            i=i+1
        print "nth fib number is:",a
fib(n)
