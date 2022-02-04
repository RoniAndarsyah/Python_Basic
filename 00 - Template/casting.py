#Casting : Merubah dari 1 type ke type lain

#Misalnya
#Ini Adalah Integer
print("====INTEGER====")
data_int = 9;
print("data = ", data_int, ",type =", type(data_int))
data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)
print("data = ", data_float, ",type =", type(data_float))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

#Ini Adalah FLOAT
print("====FLOAT ====")
data_float = 0;
print("data = ", data_float, ",type =", type(data_float))
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_bool, ",type =", type(data_bool))

#Ini Adalah bool
print("====BOOLEAN====")
data_bool = False;
print("data = ", data_bool, ",type =", type(data_bool))
data_int = int(data_bool)
data_str = str(data_bool)
data_float = bool(data_bool)
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_str, ",type =", type(data_str))
print("data = ", data_float, ",type =", type(data_float))

#Ini Adalah string
print("====STRING ====")
data_str = "10";
print("data = ", data_str, ",type =", type(data_str))
data_int = int(data_str) #String Harus Angka
data_bool = str(data_str) #String Harus Angka
data_float = str(data_str) #Jika String Kosong
print("data = ", data_int, ",type =", type(data_int))
print("data = ", data_bool, ",type =", type(data_bool))
print("data = ", data_float, ",type =", type(data_float))