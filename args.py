def cubic(num,*args):
    if args:
        s = [i**num for i in args]
        return (s)
    else:
        return 'you didn\'t pass any args'


num = [1,2,3]
print(cubic(3))

     
