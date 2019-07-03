def dec_to_bin(number):
    if number == 0:
        return ''
    else:
        return str(dec_to_bin(number//2)) + str((number%2))


def main():
    print(dec_to_bin(100))


if __name__ == "__main__":
    main()