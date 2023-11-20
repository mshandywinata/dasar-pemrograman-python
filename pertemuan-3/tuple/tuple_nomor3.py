# 3. manipulasi agar ada tambahan item "manggis" di antara item "jeruk" dan "ceri"
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

# manipulasi tuple buah agar ada tambahan item "manggis" di antara item "jeruk" dan "ceri"
buah_list = list(buah)
buah_list.insert(2, "manggis")
buah = tuple(buah_list)
print(buah)
