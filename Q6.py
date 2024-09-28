a = int(input("輸入係數A:"))
b = int(input("輸入係數B:"))
c = int(input("輸入係數C:"))
x1 = (-b+((b**2-4*a*c)**(1/2)))/2*a
x2 = (-b-((b**2-4*a*c)**(1/2)))/2*a
print('方程式的根為:x1=',x1)
print('方程式的根為:x2=',x2)