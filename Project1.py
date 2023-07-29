def BinarySearch(l, search, low=0, high=None):
    if high < low: # to check if the value to be searched exists
        return -1
    midpoint =(low+high)//2
    if l[midpoint] == search :
        return midpoint
    elif l[midpoint] > search:
        return BinarySearch(l,search,low,midpoint-1)
    else:
        return BinarySearch(l,search,midpoint+1,high)
    

l=[10,20,30,40,50,65,70,80]
h=len(l)-1 #high
to_search=65 
r=BinarySearch(l,to_search,0,h)
if r!=-1:
    print("the number",to_search,"is in",r+1,"th postion")
else:
    print("error!")
