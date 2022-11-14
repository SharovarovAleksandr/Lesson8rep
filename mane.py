def main_function(a,b):
    s=a*b
    perim=2*(a+b)
    return s, perim
    
def test_function():
    while True:
        a = int(input("Введіть довжину однієї сторони прямокутника: "))
        if a>0:
            break
        esle:
        print("Сторона не може бути менше або дорівнювати 0")
    while True:
        b = int(input("Введіть довжину другої сторони прямокутника: "))
        if b>0:
            break
        esle:
        print("Сторона не може бути менше або дорівнювати 0")
    return a,b

print("Ця программа вираховує площу та периметр прямокутника")
c=test_function()
d=main_function(c[0],c[1])
print(f'Площа = {d[0]}')
print(f'Периметр = {d[1]}')


#a=int(input("Введіть довжину однієї сторони прямокутника: "))
#b=int(input("Введіть довжину другої сторони прямокутника: "))
#if a>0 and b>0:
#   d=main_function(a,b)
#  print(f'Площа = {d[0]}')
#    print(f'Периметр = {d[1]}')
#else:
#    print("Сторона не може бути менше або дрівнювати 0")
#    if a<0 and b>0:
#        a = int(input("Введіть повторно довжину першої сторони прямокутника: "))
#    elif a>0 and b<0:
#        b = int(input("Введіть повторно довжину другої сторони прямокутника: "))
#    d = main_function(a, b)
#    print(f'Площа = {d[0]}')
#    print(f'Периметр = {d[1]}')
>>>>>>> test


