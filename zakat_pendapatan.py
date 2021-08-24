#Program ini dibuat untuk dapat melakukan perhitungan zakat mal penghasilan
#program ini dirancang untuk mencapai batas aman dalam bermuamalah
#programmer sarankan anda untuk bersedekah

#follow me on instagram : faris_helmi_permana
#ada pertanyaan hub. farissyarif23@gmail.com / 1@farishelmi.com

print("selamat datang, disini anda akan menghitung zakat pendapatan anda")

nama = str(input("masukkan nama anda (bapak/ibu) : "))
harga_emas = int(input("masukkan harga emas 1gr hari ini : "))
penghasilan = int(input("pendapatan anda perbulan : "))

penghasilan_pertahun = (penghasilan * 12)
print ("pendapatan anda pertahun : " , penghasilan_pertahun)

nisab = (85 * harga_emas)
print ("nisab emas :" , nisab)

ZAKAT = (penghasilan_pertahun * 2.5 / 100 )

if (penghasilan_pertahun >= nisab):
    print("keluarkan zakat sebesar :", ZAKAT)
else:
    print(nama, " tidak wajib membayar zakat, tapi alangkah baiknya untuk bersedekah sebanyak : ", ZAKAT , " pertahun")   
