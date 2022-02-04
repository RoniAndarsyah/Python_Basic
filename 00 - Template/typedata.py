#a = 10, a adalah variable dan nilainya 10 

#tipe data : Angka Stauan (Integer)
# tidak ada koma nya
data_integer = 1
print("data :", data_integer)
print("- bertype :", type(data_integer))

#membuat type data: angka dengan koma (float)
datafloat = 1,6655
print("data :", datafloat)
print("- bertype :", type(datafloat))

#membuat type data: Kumpulan Karakter (String)
data_string = "Mikum"
print("data :", data_string)
print("- bertype :", type(data_string))

#membuat type data: Biner true/false (Boolean/Biner)
data_bool = True
print("data :", data_bool)
print("- bertype :", type(data_bool))

#membuat type data: Data Khusus
#Bilangan Kompleks
data_complex = complex(5,6)
print("data :", data_complex)
print("- bertype :", type(data_complex))

#Tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data :", data_c_double)
print("- bertype :", type(data_c_double))
