from typing import List


class EmailValidator:
    min_length: int
    mails: List
    domains: List

    def __init__(self,min_length:int, mails:List,domains:List):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return len(name) >= self.min_length

    def __validate_mail(self,mail):
        return mail in self.mails

    def __validate_domain(self,domain):
        return domain in self.domains

    def validate(self,email):
        username, rest = email.split("@")
        mail,domain = rest.split(".")[0], rest.split(".")[-1]
        return self.__validate_domain(domain) and self.__validate_name(username) and self.__validate_mail(mail)



mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))