import sys

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    greet = 'Hello, {}'.format(who_to_greet)
    return greet


print(greet("Welcome"))
print(greet("Home!"))
print("Hello, Python World!")
