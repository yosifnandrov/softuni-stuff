class vowels:

    def __init__(self,text:str):
        self.text = text
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index <= len(self.text) - 1:
            self.index += 1
            if self.is_vowel(self.text[self.index-1]):
                return self.text[self.index - 1]
        else:
            raise StopIteration

    @staticmethod
    def is_vowel(letter:str):
        vowels = "aoeiuy"
        return letter.lower() in vowels

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)