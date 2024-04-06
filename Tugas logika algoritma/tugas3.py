b1 = int(input("Masukan bilangan pertama : "))
b2 = int(input("Masukan bilangan kedua : "))
b3 = int(input("Masukan bilangan ketiga : "))
b4 = int(input("Masukan bilangan keempat : "))

if b1<b2 and b2<b3 and b3<b4:
    terbesar = b4
if b1>b2 and b1>b3 and b1>b4:
    terbesar = b1
if b2>b1 and b2>b3 and b1>b4:
    terbesar = b2
if b3>b4 and b3>b2 and b3>b1:
    terbesar = b3

print("Bilangan terbesar adalah ", terbesar)


print("========================================")


#jumlah kelereng masing-masing
aldi = int(input("Masukkan jumlah kelereng Aldi: "))
budi = aldi - 15
anto = (aldi + budi) * 2
agung = (aldi + budi + anto) - 5

# Tampilkan jumlah kelereng Budi, Anto, dan Agung
print("Jumlah kelereng Budi:", budi)
print("Jumlah kelereng Anto:", anto)
print("Jumlah kelereng Agung:", agung)