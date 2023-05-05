def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1

dizi = [4, 8, 3, 84, 47, 76, 9, 24, 68]



# kullanıcıdan aranacak elemanı al
aranan_eleman = int(input("Lütfen aranacak elemanı girin: "))

# diziyi sırala
dizi.sort()
print("Dizi sıralanmış hali:", dizi)

# dizide aranan elemanın indeksini al
result = binary_search(dizi, 0, len(dizi)-1, aranan_eleman)

if result != -1:
    print(f"Aranan eleman {aranan_eleman} dizinin {result}. indeksinde bulundu.")
else:
    print("Aranan eleman dizide bulunamadı.")
