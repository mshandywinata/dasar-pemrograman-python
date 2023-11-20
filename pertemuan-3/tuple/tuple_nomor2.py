# 2. manipulasi tuple buah agar item "durian" dapat dihapus
buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

# manipulasi tuple buah agar item "durian" dapat dihapus
buah_list = list(buah)
buah_list.pop(3)
buah = tuple(buah_list)
print(buah)
