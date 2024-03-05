with open("books/frankenstein.txt") as f:
    file_contents =f.read()
    dic_num_letters = {}
    lower_file_contents = file_contents.lower()
    for letter in lower_file_contents:
        if letter.isalpha():
            if letter in dic_num_letters:
                dic_num_letters[letter] += 1
            else:
                dic_num_letters[letter] = 1
    print(dic_num_letters)
    