def main():
    symbols = input('symbols to trim> ')
    with open('input.txt') as fp:
        result = [(l.rstrip(symbols + '\n') + ';')[::-1] + '\n' for l in fp]
    with open('output.txt', 'w') as fp:
        fp.writelines(result)


if __name__ == '__main__':
    main()
