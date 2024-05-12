string = "hotel"

if len(string) == 1:
    a = string*6
    print(a)
elif len(string) == 2:
    b = string[1::-1]
    print(b)
elif len(string) == 3:
    c = string[-1] + string[:-1]
    print(c)
elif len(string) == 4:
    d = string[::-1]
    print(d)
else
    print(string, sep="t")

   
