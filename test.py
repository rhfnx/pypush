barang =[{
    "nama":"pena",
    "jumlah":5,
    "harga":7000
},{
    "nama":"pensil",
    "jumlah":8,
    "harga":2000
}]

def func(jumlah,harga):
    return jumlah*harga

# total1 = func(barang[0]["jumlah"],barang[0]["harga"])
# total2 = func(barang[1]["jumlah"],barang[1]["harga"])
# print(total1+total2)
arr = []
for i in range(len(barang)):
    total1 = func(barang[i]["jumlah"],barang[i]["harga"])
    arr.append(total1)
    print(sum(arr[::-1]))

