# Author  : Gesa Rizky Nugraha
# Email   : gesarizkynugraha@gmail.com
# Website : karenabelajar.blogspot.com

# Menginput
a = float(input("Tuliskan Nilai A : "))
b = float(input("Tuliskan Nilai B: "))
c = float(input("Tuliskan Nilai C : "))

# Mengkonversi
z =((b*b)-(4*a*c))** 0.5
x1 =(-b + z)/(2*a)
x2 =(-b - z)/(2*a) 

# Menampilkan Hasil
print('==========================================================')
print('Maka X1 = %0.2f'  %(x1))
print('Maka X2 = %0.2f'  %(x2))
print('==========================================================')
