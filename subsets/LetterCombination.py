def letter_combinations(digits):
    result = []
    if digits == "":
        return result
    phone_map = {
        "1": [],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"]
    }
    return letter_combinations_recursively(digits, phone_map, result)
            
def letter_combinations_recursively(digits, phone_map, result):
    if len(digits) == 1:
        return phone_map[digits[0]]
    else:
        result = letter_combinations_recursively(digits[1:], phone_map, result)
        output = []
        for letter in phone_map[digits[0]]:
            for res in result:
                w = ''.join([letter, res])
                output.append(w)
        return output


def main():
    digits_array = ["23", "73", "426", "78", "925", "2345"]
    counter = 1
    for digits in digits_array:
        print(counter, ".\t All letter combinations for '",
              digits, "': ", letter_combinations(digits), sep="")
        counter += 1
        print("-" * 100)


if __name__ == "__main__":
    main()