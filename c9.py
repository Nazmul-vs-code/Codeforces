string_1, string_2 = map(str, input().split())


string_1 = string_1.lower()
string_2 =  string_2.lower()

if (string_1 < string_2):
    print(-1) 

elif (string_1 > string_2):
    print(1)


else:
    print(0)



