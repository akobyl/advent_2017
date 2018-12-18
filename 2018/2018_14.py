recipes = [3, 7]
elf1 = 0
elf2 = 1

input = 580741
digits_needed = 10
done = False

while not done:
    score = recipes[elf1] + recipes[elf2]
    recipes += [int(num) for num in list(str(score))]

    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)
    # print(recipes)

    if len(recipes) >= (input + digits_needed):
        done = True

last_10 = recipes[input:input+10]
print('Part 1: ' + ''.join([str(i) for i in last_10]))

recipes = '37'
elf1 = 0
elf2 = 1

# input_str = '51589'       # should result 9
# input_str ='01245'        # should result 5
# input_str = '92510'         # should result 18
# input_str = '59414'         # should result 2018
input_str = '580741'
match = False

print('Part 2: ')
while not match:
    score = int(recipes[elf1]) + int(recipes[elf2])
    recipes += str(score)

    elf1 = (elf1 + int(recipes[elf1]) + 1) % len(recipes)
    elf2 = (elf2 + int(recipes[elf2]) + 1) % len(recipes)

    recipes_str = ''.join(str(i) for i in recipes)
    if input_str in recipes_str[-10:]:
        match = True

    if len(recipes) > 20330673:
        print('hi')

print(recipes_str.find(input_str))
