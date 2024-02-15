a=''
while a!="end":
    a=input()
    if a =='1':
        print('Один')
    elif a =='2':
        print('Два')
    elif a =='3':
        print('Три')
    elif a =='4':
        print('Четыре')
    elif a =='5':
        print('Пять')
    elif a =='6':
        print('Шесть')
    elif a =='7':
        print('Семь')
    elif a =='end':
        print()
    else:
        print('Не знаю такую')

a=''
while a!="end":
    b='Мы нашли '
    a=input()
    b=b+a
    if a =='1':
        b=b+' гриб в лесу'
        print(b)
    elif (a =='2' or a =='3'  or a =='4' ):
        b=b+' гриба в лесу'
        print(b)
    elif a =='end':
        print()
    else:
        print()
        b = b + ' грибов в лесу'
        print(b)

c=[6625, 333, 1, 333, 1, 12345, 333]
d=max(c)
print(d)
e=(c[len(c)-1]+c[len(c)-2]+c[len(c)-3])/3
print (e)

f=7
q=0
k=0
w=''
ww=''


while f<999999:
    sum=0
    ww=str(f)
    i=len(ww)-1
    while i>-1:
        sum=sum+int(ww[i])
        i=i-1

    q=sum%7
    if q==0:
        k=k+1

    if k==2:
        w='число '+str(f)+' и число '+str(f-1)
        print(w)
        k=0
    if q>0:
        k=0
    f=f+1

