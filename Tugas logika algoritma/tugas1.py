print("Tugas Mandiri 1")
print("=======================")
harga_telur = 26000
berat = 5
ongkos = 3500
uang = 200000

total_harga_telur = harga_telur * berat
total_ongkos = ongkos * 2        #pulang pergi
total_biaya = total_harga_telur + total_ongkos
sisa_uang = uang - total_biaya

print("ibu memiliki uang sebesar Rp", uang)
print("ibu membeli telur ", berat, "kg ", "dengan harga Rp", total_harga_telur)
print("dipotong ongkos ", total_ongkos)
print("sisa uang ibu tinggal ", sisa_uang)

if sisa_uang <= 0 :
    print("uang tidak cukup")
else :
    print("uang cukup")