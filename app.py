string_1 = 'hello'
string_2 = 'friend'
#geeft h e l l o
print(*string_1)
#geeft f r i e n d
print(*string_2)
#geeft hello friend (de sep is wat hij normaal is dus " ")
#vandaar dat er een spatie tussen string_1 en string_2
print(string_1, string_2)
#als je sep = '' (niets) doet dan geeft hij hellofriend (zonder spatie)
print(string_1, string_2, sep = "")
#als je sep = ' good ' doet dan stopt hij dat tussen string_1 en string_2
#dus hij geeft: hello good friend
print(string_1, string_2, sep = ' good ')