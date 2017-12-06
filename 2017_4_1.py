sum = 0

with open('day4_in.txt') as file:
    for line in file:
        # remove newline
        line = line.rstrip()
        words = line.split(' ')

        found_words = []
        valid_password = True
        for word in words:
            if word not in found_words:
                found_words.append(word)
            else:
                valid_password = False

        if valid_password:
            sum += 1

        print('Valid: {}, PW: {}'.format(valid_password, line))

print('Sum: \n {}'.format(sum))

