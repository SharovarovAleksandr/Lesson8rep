import math
def main_function_triangl(a,b):
    s=a*b/2
    perim=a+b+math.sqrt(a*a+b*b)
    return s, perim

def test_function_triangl():
    while True:
        a = int(input("Введіть довжину одного катета прямокутного трикутника: "))
        if a>0:
            break
        else:
            print("Катет трикутника не може бути менше або дорівнювати 0")
    while True:
        b = int(input("Введіть довжину другого катета прямокутного трикутника: "))
        if b>0:
            break
        else:
            print("Катет трикутника не може бути менше або дорівнювати 0")
    return a,b

print("Ця программа вираховує площу та периметр прямокутньго трикутника за двома катетами")
c=test_function_triangl()
d=main_function_triangl(c[0],c[1])
print(f'Площа трикутника= {d[0]}')
print(f'Периметр трикутника= {d[1]}')