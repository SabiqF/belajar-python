list_nim = []
list_uts = []
list_uas = []
list_total = []

ulang = 2
for i in range(ulang):
    print("data ke - " + str(i+1))
    list_nim.append(input("Masukkan NIM anda : "))
    list_uts.append(int(input("Masukkan nilai UTS anda : ")))
    list_uas.append(int(input("Masukkan nilai UAS anda : ")))

for i in range(ulang):
    list_total.append(list_uas[i] + list_uts[i] / 2)

print("=" * 45)
print("NIM          Nilai UTS        Nilai UAS")
print("=" * 45)

for i in range(ulang):
    print(list_nim[i], ("") * 50, list_uts[i], ("") *50, list_uas[i], ("") *50, list_total[i])
