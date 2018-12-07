from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool

alphabet = list('abcdefghijklmnopqrstuvwxyz')

with open('input/day5_in.txt') as file:
    polymer = file.readline()
    polymer.rstrip()


# polymer = 'dabAcCaCBAcCcaDA'

def one_upper_one_lower(a: str, b: str) -> bool:
    if a.islower() and b.isupper():
        return True
    elif a.isupper() and b.islower():
        return True
    else:
        return False


def reduce_polymer(polymer: str):
    complete = False
    while not complete:
        i = 0
        max = len(polymer) - 1
        complete = True

        while i < max:
            if polymer[i].upper() == polymer[i + 1].upper():
                if one_upper_one_lower(polymer[i], polymer[i + 1]):
                    polymer = polymer[:i] + polymer[i + 2:]
                    complete = False
                    break
            i += 1
    return polymer

def reduce_polymer_2(polymer: str)->str:
    complete = False
    while not complete:
        initial_len = len(polymer)
        for letter in alphabet:
            polymer = polymer.replace(letter.lower() + letter.upper(), '').replace(letter.upper() + letter.lower(), '')

        if len(polymer) == initial_len:
            complete = True
    return polymer


part1_polymer = polymer
part1_polymer = reduce_polymer_2(part1_polymer)
part1_result = len(part1_polymer)
print(f'Part 1: {part1_result}')


def reduce_polymer_letter(letter):
    part2_polymer = polymer
    part2_polymer = part2_polymer.replace(letter, '').replace(letter.upper(), '')

    result = len(reduce_polymer_2(part2_polymer))
    # part2_results.append((letter, result))
    return result


part2_results = []

pool = ThreadPool(16)
results = pool.map(reduce_polymer_letter, alphabet)
pool.close()
pool.join()
part2_results = list(zip(alphabet, results))


part2_results.sort(key=lambda result: result[1])
print(part2_results)
print(f'Part 2: {part2_results[0][1]}')
print('done')