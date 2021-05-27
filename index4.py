# x = []
# x.append(1)
# x.append([1,"kox"])
# for i in range (0, len(x)):
#     print(type(x[i]))
    
# y=2
# if type(y)==int:
#     print("int")
# if str(type(y).find("int")):
#     print("int")

x=[1,2,"abc",["a","b"],0]
for i in x:
    if type(i) == list:
        for j in i:
            print(j)
    else:
        print(i)
        
y=[1,6,4,22]
print(1 in y)
print(67 in y)
