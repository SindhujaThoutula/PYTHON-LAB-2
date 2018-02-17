List = [{"Name": 'Sindhu', "PhNo":8312143114, "Email": "sindhuthouthula@gmail.com"}, {"Name": "Ratnavalli", "PhNo":9985006849, "Email": "avalli24@gmail.com"}, {"Name": "Raji", "PhNo":8297184129, "Email": "raji2158@gmail.com"}]
nm = input("Give name to obtain contact: ")
for a in List:
    if nm in a.values():
        print(a)
num = int(input("Give number to obtain contact: "))
for b in List:
    if num in b.values():
        print(b)
nme = input("Give name to obtain contact and edit no: ")
for c in List:
    if nme in c.values():
        print(c)
Newno = int(input("Give no to edit: "))
c["no"] = Newno
print(c)