def map_int_to_digits(num):
    ratusan = num // 100
    puluhan = (num % 100) // 10
    satuan = num % 10
    return {"ratusan": ratusan, "puluhan": puluhan, "satuan": satuan}


random_list = [2.1, 3, "hello", 2.7, 51,
               "python", 5.5, 737, "world", "AI", 412]

float_list = list(filter(lambda x: isinstance(x, float), random_list))
int_list = list(filter(lambda x: isinstance(x, int), random_list))
string_list = list(filter(lambda x: isinstance(x, str), random_list))

print("data float:", float_list)

print("data int:")
for item in int_list:
    print(map_int_to_digits(item))

print("data string:", string_list)
