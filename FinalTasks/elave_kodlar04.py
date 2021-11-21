#istifadeci bir eded daxil edir ve 1-den hemin ededi qeder hasil hesablanir.

while True:
    n= input("ededi daxil edin: ")
    if (n=="q"):
        print("emeliyyat dayandirildi ")
        break
    else:
        n= int(n)
        faktorial= 1
        for i in range(2,n+1):
            faktorial *= i
            print ("Faktorial ", faktorial)

#fibanocci ededleri: 1,1,2,3,5,8,13 ve s. bu ededlerde 3.cu eded evvelki iki ededin cemine beraber olur
a=1
b=1
fibonacci=[a,b]
for i in range(10):
    a,b= b,(a+b)
    fibonacci.append(b)
print(fibonacci)
#bu proqramda kod 10 defe tekrarlanir yeni 12.ci fibanocci ededine qeder butun ededleri cap edir. kodu modifikasiya edib ededlerin sayini istifadeciden de almaq olar ve ya istifadecinin daxil etdiyi yerdeki fibanocci ededini de ekrana cap ede bilerik. 
