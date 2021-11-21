n=int(input()) 
arr=[]
for i in range(0,n):
    a=int(input())
    arr.append(a)
arr.sort()
print(arr[-2]) 

#her hansisa metoddan istifade etmeden yazmaq ucun:
b=int(input('listin olcusunu daxil edin: '))
arr=[]
for i in range(0,b):
    listElementi=int(input())
    arr.append(listElementi)
n=len(arr)
maksimum= max(arr[0],arr[1])
ikinci_maksimum=min(arr[0],arr[1])
for x in range(2,n):
    if arr[x]>maksimum:
        ikinci_maksimum=maksimum
        maksimum=arr[x]
    elif arr[x]>ikinci_maksimum:
        arr[x]=ikinci_maksimum
print(ikinci_maksimum)

            
    