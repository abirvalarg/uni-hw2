def main():
    with open('input1.txt') as fp:
        lines = list(fp)
    with open('input2.txt') as fp:
        lines += list(fp)
    lines.sort()
    with open('output.txt', 'w') as fp:
        fp.writelines(lines)


if __name__ == '__main__':
    main()
