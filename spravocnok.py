phone_spr = {"Amal": "5645556", "mehman": "123456", "nastya": "0986655"}

myfile = open('phone.txt', 'w')

str = " ".join([f"{item[0]}:{item[1]}" for item in phone_spr.items()])

myfile.writelines(str)

myfile.close()

myfile = open("phone.txt", "r")

str = myfile.read().split(" ")

dict = {}

for a in str:
    p = a.split(":")
    dict[p[0]] = p[1]

    print(p)

print(dict)

myfile.close()
