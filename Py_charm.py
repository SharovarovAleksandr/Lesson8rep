import math
def main_function(a,b):
    s=a*b/2
    perim=a+b+math.sqrt(a*a+b*b)
    return s, perim

def test_function():
    while True:
        a = int(input("Введіть довжину одного катета прямокутного трикутника: "))
        if a>0:
            break
        esle:
        print("Катет трикутника не може бути менше або дорівнювати 0")
    while True:
        b = int(input("Введіть довжину другого катета прямокутного трикутника: "))
        if b>0:
            break
        esle:
        print("Катет трикутника не може бути менше або дорівнювати 0")
    return a,b

print("Ця программа вираховує площу та периметр прямокутньго трикутника за двома катетами")
c=test_function()
d=main_function(c[0],c[1])
print(f'Площа трикутника= {d[0]}')
print(f'Периметр трикутника= {d[1]}')