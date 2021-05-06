import re

with open("text.txt","r+") as text_ph:
    text_ph.write('Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of '
                  '\nclassical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, '
                  '\na Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin '
                  '\nwords, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in '
                  '\nclassical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 '
                  '\nand 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, '
                  '\nwritten in 45 BC. This book is a treatise on the theory of ethics, very popular during the '
                  '\nRenaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in '
                  '\nsection 1.10.32.')


with open("text.txt") as final_text_ph:
    text = final_text_ph.read()

with open("searched.txt", "w") as searched_ph:
    searched_ph.write(f"Lorem\nIpsum\n1.10.32")

with open("searched.txt") as searched_words_ph:
    searched = searched_words_ph.read().split()

words_dict = {}
for word in searched:
    matches = re.findall(rf'(?<=[\s"])({word})(?=[\s,.!?])', text, re.MULTILINE + re.IGNORECASE)
    words_dict[word.lower()] = len(matches)
with open("output.txt", "w") as output_ph:
    for word,count in sorted(words_dict.items(), key = lambda c:c[1], reverse=True):
        print(f"{word} - {count}", file= output_ph)


