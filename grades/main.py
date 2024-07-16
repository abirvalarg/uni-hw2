def main():
    with open('input.txt') as fp:
        grades = {p[0].strip(): int(p[1].strip()) for p in [s.split(',') for s in fp]}
    average = sum(grades.values()) / len(grades)
    aboveAverage = {name: grade for (name, grade) in grades.items() if grade > average}
    with open('output.txt', 'w') as fp:
        fp.writelines([name + '\n' for name in aboveAverage.keys()])

if __name__ == '__main__':
    main()
