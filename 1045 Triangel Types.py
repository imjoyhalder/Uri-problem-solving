"""a,b,c = list(map(float,input().split()))
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if (a>=(b+c)):
    print("NAO FORMA TRIANGULO")
if (a**2 == (b**2 + c**2)):
    print("TRIANGULO RETANGULO")
if ((a**2)>(b**2+c**2)):
    print("TRIANGULO OBTUSANGULO")
if ((a**2)<(b**2+c**2)):
    print("TRIANGULO ACTANGULO")
if a==b==c:
    print("TRIANGULO EQUILATERO")
if a==b!=c or a==c!=b or b==c!=a:
    print("TRIANGULO ISOSCELES")

"""
a,b,c=list(map(float,input().split()))
if(a < b):
    temp = a
    a = b
    b = temp
if(b < c):
    temp = b
    b = c
    c = temp
if(a < b):
    temp = a
    a = b
    b = temp
if(a>=(b+c)):
    print("NAO FORMA TRIANGULO")
elif(a*a == (b*b+c*c)):
     print("TRIANGULO RETANGULO")
elif(a * a > (b*b+ c*c)):
    print("TRIANGULO OBTUSANGULO")
elif(a*a<(b*b + c*c)):
    print("TRIANGULO ACUTANGULO")
if(a == b and b == c):
        print("TRIANGULO EQUILATERO")
elif(a == b or b == c):
        print("TRIANGULO ISOSCELES")