def chia_het_5(n):
    t=int(n,2)
    if(t%5==0):
        return True
    else:
        return False
b=input ("nhap chuoi so nhi phan(tach boi dau phay)")
a=b.split(',')
c=[so for so in a if chia_het_5(so)]
if len(c)>0:
    q=','.join(c)
    print( "cac so nhi phan chia het cho 5 la ", q)
else:
    print("kh cos so nao chia het cho 5")