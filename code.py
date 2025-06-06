with open("ip_addresses.txt","r") as file:
    file_text = file.read()
list=file_text.split()
with open("blocked_ip.txt","r") as file:
    file__text=file.read()
list1=file__text.split()
print(list)
print(list1)
for i in list.copy():
    if i in list1:
        list.remove(i)
print(list)
