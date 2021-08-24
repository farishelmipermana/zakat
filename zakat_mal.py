#program ini dibuat untuk anda menghitung zakat mal yang harus anda keluarkan
#follow me on instagram : faris_helmi_permana
#ada pertanyaan hub. farissyarif23@gmail.com / 1@farishelmi.com


print("Disini kita akan menghitung zakat mal (harta) yang harus anda keluarkan.")

nama = str(input("masukkan nama anda (bapak/ibu) : " ))
harga_emas = int(input("masukkan harga emas hari ini dalam 1gr : " ))
uang = int(input("total uang yang anda miliki saat ini (yang telah disimpan selama 1 tahun) : "))

ZAKAT = (uang * 2.5 / 100)
nisab = (harga_emas * 85)

if (uang >= nisab):
    print (nama, " wajib membayar zakat sebesar ", ZAKAT, " rupiah")
else:
    print (nama, "tidak wajib membayar zakat mal")
