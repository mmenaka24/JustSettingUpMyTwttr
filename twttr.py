def main():
    str = input("Input: ")
    output = ""

    vowels = ["a", "e", "i", "o", "u"]

    for char in str:
        if not char.lower() in vowels:
            output = output + char

    print("Output: " + output)


main()
