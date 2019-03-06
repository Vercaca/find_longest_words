'''
 Date: 2019/03/05
 Company: __DAY (via Codility)
 Time given: 30-45 mins
 Time used : 40 mins

 Question:
    Given a non-integer n, n could be in range [0 <= n <= 2,000,000]
    Count number of 1 digits in 11 to the power of n

 Example:
    n = 2, 11^n = 121, ans = 2
    n = 0, 11^n = 1, ans = 1

'''

def calculate_11_to_power_n(n):
    if n <= 1:
        return [1] * (n+1)

    # calcuate as backward
    int_prev =[1, 1]
    for _ in range(2, n+1):
        n_digits = len(int_prev)

        # calculate the middle digits
        digits = [1]
        digits += [int_prev[i]+int_prev[i-1] for i in range(1, n_digits)]
        digits += [int_prev[-1]]

        # add carry
        for i in range(2, len(digits)):
            digits[i] += digits[i-1] // 10 # carry
            digits[i-1] = digits[i-1] % 10 # remainder

        # update previous 
        int_prev = digits[:]

    # reverse as original
    digits = digits[::-1]

    return digits

def count_1_digits(digits):
    return digits.count(1)

def run(n):
    digits = calculate_11_to_power_n(n)
    str_11_p_n = ''.join([str(d) for d in digits])
    ans = count_1_digits(digits)

    print('n = {}, 11^n = {}, nums of 1 digits: {}'.format(n, str_11_p_n, ans))

def demo():
    for i in range(10):
        run(i)
if __name__ == '__main__':
    demo()
