def shout(func):
    def wapper():
        result = func()
        return result.upper()
    return wapper

@shout
def greet():
    return "Hello"

print(greet())