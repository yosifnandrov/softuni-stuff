# def palindrome(word, index):
#     if len(word) <= 1:
#         return f"{word} is a palindrome"
#     not_palindrome = "not" in palindrome(word[1:-1],index)
#     if word[0] == word[-1] and not not_palindrome:
#         return f"{word} is a palindrome"
#     else:
#         return f"{word} is not a palindrome"

def palindrome(word,index):
    if index >= len(word) // 2:
        return f'{word} is a palindrome'
    if word[index] == word[len(word) - 1 - index]:
        return palindrome(word, index +1)
    return f"{word} is not a palindrome"






print(palindrome_s("abba", 0))
print(palindrome_s("gotig", 0))