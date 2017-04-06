# Problem 79

# Given that the three characters are always asked for in order, analyse the
# file so as to determine the shortest possible secret passcode of unknown
# length.


logs = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710,
        629, 168, 160, 689, 716, 731, 736, 729, 316, 729, 729, 710, 769, 290,
        719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362,
        319, 760, 316, 729, 380, 319, 728, 716]


def digits(l_list):
    """ Determines the digits used for the passcode. """
    nums = []
    for i in l_list:
        j = str(i)
        for k in range(0, len(j)):
            if j[k] not in nums:
                nums.append(j[k])
    return nums


def pos_n(l_list, a_list, num):
    """ Determines the passcode. """
    poss = []
    for i in l_list:
        j = str(i)
        if num in j:
            k = j.index(num)
            if k != 0:
                poss.append(j[k - 1 : k])
    for i in poss:
        if i not in a_list:
            return False
    return True


# main
answer = []
keys = digits(logs)
i = 0
while len(keys) != 0:
    if pos_n(logs, answer, keys[i]):
        answer.extend(keys[i])
        keys.remove(keys[i])
    i += 1
    if i >= len(keys):
        i = 0
print(answer)