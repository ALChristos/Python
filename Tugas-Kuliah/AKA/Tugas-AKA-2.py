ArrayBilangan = [121,80,63,74,57,39,88,122,109,30]
BilGanjil = 0

for i in ArrayBilangan:
    if i % 2 != 0:
        BilGanjil += 1
        
print(f"Jumlah Bilangan Ganjil dari {ArrayBilangan} \nSebanyak: {BilGanjil} Bilangan")

