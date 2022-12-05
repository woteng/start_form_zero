# TIPE DATA

from ctypes import c_double

# integer angka tanpa koma
data_integer = 1
print(type(data_integer))
print("data :", data_integer, ", bertipe :", type(data_integer))

# float angka dengan koma
data_float = 1.9
print(type(data_float))
print("data :", data_float, ", bertipe :", type(data_float))

# string karakter atau huruf
data_string = "hello cok"
print(type(data_string))
print("data :", data_string, ", bertipe :", type(data_string))

# boolean true or false (1 or 0) (biner)
data_boolean = True
print(type(data_boolean))
print("data :", data_boolean, ", bertipe :", type(data_boolean))

# TIPE DATA KHUSUS

# bilangan kompleks
data_complex = complex(5, 6)
print(type(data_complex))
print("data :", data_complex, ", bertipe :", type(data_complex))

# tipe data dari bahasa C
# fisrt import librarynya dari c

# import library
# from ctypes import c_double

data_c_double = c_double(10.5)
print(type(data_c_double))
print("data :", data_c_double, ", bertipe :", type(data_c_double))
