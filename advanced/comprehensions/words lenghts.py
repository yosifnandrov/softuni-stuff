words = input().split(", ")

words_len = [print(f"{word} -> {len(word)}", end=", ") if not word == words[-1] else print(f"{word} -> {len(word)}") for word in words]
