from random import randrange

def checkfunction(d):
    if d == 2:
        return True
    if d % 2 == 0 or d <= 1:
        return False

    first = int(d**0.5) + 1
    for second in range(3, first, 2):
        if d % second == 0:
            return False
    return True

def main():
    array = []
    for i in range(10):
        d = randrange(1, 200)
        array.append(d)
    print(array)
    print(list(filter(lambda arg: checkfunction(arg), array)))

if __name__ == '__main__':
    main()