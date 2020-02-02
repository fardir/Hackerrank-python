def split_and_join(line):
    line = line.split()
    return '-'.join(x for x in line)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
