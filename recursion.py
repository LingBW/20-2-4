a=[2,[5,7],[1],[8,[5,[4],6]],[9,3],67,56,35,89]
b=[]
def lst(ls,l=[]): 
    for i in ls:
        if type(i)==list:
            lst(i)
        else: l.append(i)
    return l
b=lst(a)
b.sort()
print b
raw_input()
