#buatkan perhitungan
#luas segiempat, luas segitiga, luas lingkaran

print("luas segiempat")
sisi1 = int(input("masukkan sisi 1 : "))
sisi2 = int(input("masukkan sisi 2 : "))

luas = sisi1 * sisi2
print("rumus luas segiempat adalah L = S x S")
print("Jadi luas segiempat tersebut adalah : ", luas)


print("=============================")


print("luas segitiga")
alas = int(input("masukkan alas : "))
tinggi = int(input("masukkan tinggi : "))

luas_segitiga = alas * tinggi / 2
print("rumus luas segitiga adalah a x t : 2")
print("jadi luas segitiga tersebut adalah : ", luas_segitiga)


print("==============================")


print("luas lingkaran")
phi = 3.14
r = int(input("masukkan jari-jari : "))

luas_lingkaran = phi * r * r
print("rumus luas lingkaran adalah phi x r x r")
print("jadi luas lingkaran tersebut adalah : ", luas_lingkaran)