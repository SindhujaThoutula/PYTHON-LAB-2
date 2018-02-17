UMKC = {"Python":55,"Cloud":25,"Mobile":10,"Oracle":40,"Testing":60,"Hadoop":100}
for index in UMKC.items():
 print(index)
S=int(input("Min range: "))
P=int(input("Max range: "))
K=dict((a, b) for a, b in UMKC.items() if b >= S and b<=P)
print("You can buy",K.keys())