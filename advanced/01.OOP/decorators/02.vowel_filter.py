def vowel_filter(fn):
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        return [a for a in result if a.lower() in "aouyie"]
    return wrapper


@vowel_filter
def get_letters():
    return ["A", "b", "c", "d", "e"]

print(get_letters())