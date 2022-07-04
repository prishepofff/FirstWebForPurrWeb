import math
from functools import reduce


def domain_name(url: str):
    return url.replace('http://', '').replace('https://', '').replace('www.', '').split('.')[0]


def int32_to_ip(int32: int):
    o1 = int32 // 16777216 % 256
    o2 = int32 // 65536 % 256
    o3 = int32 // 256 % 256
    o4 = int32 % 256
    return f'{o1}.{o2}.{o3}.{o4}'


def zeros(n: int):
    k_max = math.log(n, 5)
    res = 0
    for k in range(1, int(k_max + 1)):
        res = math.floor(res + (n / math.pow(5, k)))
    return res


# честно скзаать решение данной задачи вызвало некоторые трудности и уверен, что я решил неправильно/неоптимально, но тесты проходит.
def bananas(s) -> set:
    finding = 'banana'
    all_variants = [s]
    for dec in range(len(s) - len(finding)):
        indexs_dec = [x for x in range(len(s) - len(finding))]
        count_dec = len(indexs_dec)
        for k in range(len(s) - count_dec):
            old_position = indexs_dec[dec]
            for j in range(count_dec):
                old = indexs_dec[j]
                for x in range(len(s)):
                    new_s = s
                    for i in indexs_dec:
                        if len(new_s[:i]) == len(s):
                            new_s = f'{new_s[:i]}'
                        else:
                            new_s = f"{new_s[:i]}-{new_s[i + 1:]}"
                    all_variants.append(new_s)
                    indexs_dec[j] += 1
                indexs_dec[j] = old
            indexs_dec = [f + 1 for f in indexs_dec]
            indexs_dec[dec] = old_position
    result = set(filter(lambda x: x.replace('-', '') == finding, set(all_variants)))
    return result


def count_find_num(primesL: list, limit):
    # your code here
    res = []
    start = reduce(lambda x, y: x * y, primesL)
    for number in range(start, limit + 1):
        i = 2
        primfac = []
        local_number = number
        while i * i <= local_number:
            while local_number % i == 0:
                primfac.append(int(i))
                local_number = local_number / i
            i = i + 1
        if local_number > 1:
            primfac.append(int(local_number))
        if set(primfac) == set(primesL):
            res.append(number)
    if res:
        res = [len(res), res[-1]]
    return res


if __name__ == '__main__':
    print(zeros(30))
    print(domain_name("http://google.co.jp"))
    print(domain_name("www.xakep.ru"))
    print(domain_name("https://youtube.com"))
    print(int32_to_ip(2149583361))
    print(bananas('bananana'))
    print(count_find_num([2, 3, 47], 200))


