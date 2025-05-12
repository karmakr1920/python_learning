# You are given an integer array digits, where each element is a digit. The array may contain duplicates.

# You need to find all the unique integers that follow the given requirements:

# The integer consists of the concatenation of three elements from digits in any arbitrary order.
# The integer does not have leading zeros.
# The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.

# Return a sorted array of the unique integers.

def findEvenNumbers(digits):
    # digits_count = len(digits)
    # result = set()
    # for i in range(digits_count):
    #     for j in range(digits_count):
    #         if i == j:
    #             continue
    #         for k in range(digits_count):
    #             if k == i or k == j:
    #                 continue
    #             d1,d2,d3 = digits[i],digits[j],digits[k]
    #             if d1 == 0:
    #                 continue
    #             if d3 % 2 != 0:
    #                 continue
    #             num = d1*100 + d2*10 + d3
    #             result.add(num)
    # return sorted(result)
    freq = [0] * 10
    for d in digits:
        freq[d] += 1

    result = []

    for num in range(100, 1000, 2):  # Only even numbers
        d1 = num // 100
        d2 = (num // 10) % 10
        d3 = num % 10

        needed = [0] * 10
        needed[d1] += 1
        needed[d2] += 1
        needed[d3] += 1

        if all(freq[d] >= needed[d] for d in range(10)):
            result.append(num)

    return result
