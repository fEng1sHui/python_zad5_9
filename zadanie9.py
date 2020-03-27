def main():
    with open('txt','r',encoding='UTF-8') as file:
        source = file.read()
        words = len(source.split())
        print("Wyrazow: " + str(words))

if __name__ == '__main__':
    main()