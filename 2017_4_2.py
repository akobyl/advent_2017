sum = 0

with open('day4_in.txt') as file:
    for line in file:
        print('---------\n{}'.format(line))
        # remove newline
        line = line.rstrip()
        words = line.split(' ')

        found_words = []
        found_words.append(list(words[0]))

        valid_password = True
        for word in words[1:]:
            # compare every iteration
            letters = list(word)
            print('letters: {}'.format(letters))

            for compare_word in found_words:
                all_letters_match = True
                for letter in letters:
                    print('\t\tcomparing letter {} in {}'.format(letter, compare_word))
                    if letter not in compare_word:
                        all_letters_match = False
                        print('\t\t\tdoes not match')
                    else:
                        print('\t\t\tdoes match')
                print('len letters: {}, len compare: {}'.format(len(letters), len(compare_word)))
                if all_letters_match and len(letters) == len(compare_word):
                    valid_password = False
                print('\t\tvalid password: {}, all letters match: {}'.format(valid_password, all_letters_match))
                print('\tcompared {} to {}, valid: {}'.format(letters, compare_word, valid_password))
            found_words.append(list(word))

        if valid_password:
            sum += 1

        print('Valid: {}, PW: {}'.format(valid_password, line))
        print('words: {}'.format(found_words))

print('Sum: \n {}'.format(sum))
