companyCount= int(input('company sayini daxil edin: '))
arr=[]
for i in range(companyCount):
    country=input('olkelerin adini daxil edin: ')
    arr.append(country)
new_arr=set(arr)
n=len(new_arr)
print('umumi olke sayi {}-dir'.format(n))