words = input().split()

filtered_words = [print(word) for word in words if len(word) % 2 == 0]