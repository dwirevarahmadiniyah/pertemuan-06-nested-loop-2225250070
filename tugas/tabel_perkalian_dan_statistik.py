print("Tabel Perkalian dan Statistik")

n = int(input("n: "))

# Validasi n dengan while
while n <= 0:
    print("n harus lebih dari 0!")
    n = int(input("Masukkan n lagi: "))

# Inisialisasi total keseluruhan dan counter genap
total_keseluruhan = 0
counter_genap = 0

# Nested loop untuk tabel perkalian
for i in range(1, n + 1):
    total_baris = 0

    for j in range(1, n + 1):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
        
        total_baris += hasil
        total_keseluruhan += hasil

        # Pencacahan bilangan genap
        if hasil % 2 == 0:
            counter_genap += 1

    print(f"Total baris {i} = {total_baris}")
    print()

print("Statistik:")
print(f"Total keseluruhan = {total_keseluruhan}")
print(f"Banyak hasil genap = {counter_genap}")