def main_function(a,b):
    s=a*b
    perim=2*(a+b)
    return s, perim

print("Ця программа вираховує площу та периметр прямокутника")
d=main_function(5,4)

print(f'Площа = {d[0]}')
print(f'Периметр = {d[1]}')

