def swap(word, i, j):
    word_list = list(word)
    word_list[i], word_list[j] = word_list[j], word_list[i]
    return ''.join(word_list)

def permute_word(word):
    result = permute_word_recursively(word, 0)
    return result

def permute_word_recursively(word, current_index):
    result = []
    if current_index == len(word) - 1:
        result.append(word)
        return result
    for index in range(current_index, len(word)):
        word = swap(word, current_index, index)
        result.extend(permute_word_recursively(word, current_index + 1))        
    return result

def main():

    input_word = ["ab", "bad", "word","absent"]
    for index in range(len(input_word)):
        print(index + 1, ".\t Input string: '", input_word[index], "'", sep="")
        response = permute_word(input_word[index])
        print(f'Length of output {len(response)}:{response}')
        print('-' * 100)

if __name__ == '__main__':
    main()

