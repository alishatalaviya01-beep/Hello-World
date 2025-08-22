lst=[10,20,30,40,50,20]
x=int(input("enter element of search"))
count=0
for i in lst:
    if i== x:
        count +=1

    if count>0:
        print(x,"found",count,"time(S) in the list")
    else:
        print(x,"not found the list")
