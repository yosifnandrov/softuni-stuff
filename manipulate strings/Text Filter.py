# import re
#
# ban_words = input().split(", ")
#
# text = input()
# word = re.findall(r'\w+', text)
# new_text = ""
# for i in range(len(ban_words)):
#     for w in word:
#         if w == ban_words[i]:
#             new_text = text.replace(w, "*"*len(w))
#             text = new_text
#             break
# print(new_text)

ban_words = input().split(", ")
text = input()

for word in ban_words:
    while word in text:
        text = text.replace(word, "*"*len(word))
print(text)