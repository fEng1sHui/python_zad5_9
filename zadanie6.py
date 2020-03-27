def main():
    integer = int(input('Input: '))

    def fib(d):
        if d < 2:
            return d
        return fib(d - 2) + fib(d - 1)

    print([fib(el) for el in range(integer) if el != 0 and el != 1 and el != 2])

if __name__ == '__main__':
    main()