class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(NameTooShortError):
    pass


class InvalidDomainError(NameTooShortError):
    pass


