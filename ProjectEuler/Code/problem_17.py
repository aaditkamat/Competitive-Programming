def represent(num, hash_map):
    if num in hash_map:
        return hash_map[num]
    if num < 100:
        return hash_map[num - num % 10] + hash_map[num % 10]
    if num % 100 == 0:
        return hash_map[num // 100] + hash_map[100]
    return hash_map[num // 100] + hash_map[100] + 'and' + represent(num % 100, hash_map)

def solution(num):
    hash_map = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'hundred',
        1000: 'onethousand',
    }
    count = 0
    for i in range(1, num + 1):
        rep = represent(i, hash_map)
        count += len(rep)
    return count

print(solution(1000))