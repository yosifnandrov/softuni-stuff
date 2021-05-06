import validation

test_email = input()

while not test_email == "End":
    if "@" not in test_email:
        raise validation.MustContainAtSymbolError("Email must contain @")
    else:
        test_email = test_email.split("@")
        if len(test_email[0]) <= 4:
            raise validation.NameTooShortError("Name must be more than 4 characters")
        else:
            test_email = "".join(test_email)
            test_email = test_email.split(".")
            domains = ["com","net","bg","org"]
            if test_email[-1] not in domains:
                raise validation.InvalidDomainError("Domain must be one of the following: .com, .bg, .net, .org")
    print("Email is valid")
    test_email = input()


