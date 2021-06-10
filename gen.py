def even_no(n):
    for i in range(2,n+1,2):
            yield i
            

for i in even_no(10):
    print(i)


