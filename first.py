def count(lst):
    global more
    global less
    for i in range(len(lst)):
        if len(lst[i]) > 5:
            more=more+1
        elif len(lst[i])<5:
            less=less+1
    
    return more, less

lst =[]
x=int(input("how many elements"))
for i in range(x):
    ele=input("enter a name")
    lst.append(ele)

more=0
less=0

more,less=count(lst)
print(lst)
print(more)
print(less)
print("done")
