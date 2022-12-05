# CASTING TIPE DATA
# (merubah satu tipe data ke tipe data lain)
# (int) -> (float) -> (str)

# INTEGER
print("=====INTEGER=====")
data_int = 7
print("data :", data_int, ", bertipe :", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)  # 0 = false, 1 = true

print("data :", data_float, ", bertipe :", type(data_float))
print("data :", data_str, ", bertipe :", type(data_str))
print("data :", data_bool, ", bertipe :", type(data_bool))

# FLOAT
print("float")
data_float = 7.6
print("data :", data_float, ", bertipe :", type(data_float))

data_int = int(data_float)  # dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)  # 0 = false, 1 = true

print("data :", data_int, ", bertipe :", type(data_int))
print("data :", data_str, ", bertipe :", type(data_str))
print("data :", data_bool, ", bertipe :", type(data_bool))

# BOOLEAN
print("boolean")
data_bool = True
print("data :", data_bool, ", bertipe :", type(data_bool))

data_int = int(data_bool)  # dibulatkan ke bawah
data_str = str(data_bool)
data_float = float(data_bool)  # 0 = false, 1 = true

print("data :", data_int, ", bertipe :", type(data_int))
print("data :", data_str, ", bertipe :", type(data_str))
print("data :", data_float, ", bertipe :", type(data_float))

# String
print("String")
data_str = "10"
print("data :", data_str, ", bertipe :", type(data_str))

data_int = int(data_str)  # dibulatkan ke bawah
data_bool = bool(data_str)  # jika kosong baru jadi false
data_float = float(data_str)  # 0 = false, 1 = true

print("data :", data_int, ", bertipe :", type(data_int))
print("data :", data_bool, ", bertipe :", type(data_bool))
print("data :", data_float, ", bertipe :", type(data_float))
