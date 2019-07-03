def reverse_string(a_string):
    if len(a_string) == 0: 
        return a_string
    reverse = list(a_string)
    for i in range(len(a_string)//2):
        reverse[i], reverse[-i-1] = reverse[-i-1], reverse[i]
    return ''.join(reverse)


def main():
    print(reverse_string('cool'))


if __name__ == "__main__":
    main()