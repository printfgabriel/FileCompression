
def counting(content):
    counter = {}
    for letter in content:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter


def main():
    file = open("teste.txt", "r+")
    content = file.read()
    count = counting(content)
    print(count.most_common(1))
    file.close()


main()