'''
 Date: 2019/03/05
 Company: __DAY (Codility)
 Time given: 30-45 mins
 Time used : 15 mins

 Question:
    Given a tel no. 'tel' with format in digits, dashes '-' or spaces ' '
    Assume that the tel must contains at least 2 digits


    Reformat tel with the following requirements:
        1. 3 digits in a group
        2. seperate each group with '-', remove other dashes or spaces
        3. the last one or two groups can be with 2 digits if necessaries

 Example: "339 - 3921 2042"  -> "339-392-120-42"
          "339 - 3921 204"   -> "339-392-12-04"
          "3 3-939-212-0422" -> "339-392-120-422"
'''
import sys

def reformat(tel):
    # remove non-digits
    tel = tel.replace(' ', '').replace('-', '')

    n_digits = len(tel)
    if n_digits <= 3:
        return tel

    # grouping
    n_groups = n_digits // 3
    remainder = n_digits % 3

    if remainder == 0:
        new_tel = [tel[i:i+3] for i in range(0, n_digits, 3)]

    elif remainder == 1:
        new_tel = [tel[i:i+3] for i in range(0, n_digits-4,3)]
        new_tel += [tel[-4:-2], tel[-2:]]
    else:
        new_tel = [tel[i:i+3] for i in range(0, n_digits-2,3)]
        new_tel += [tel[-2:]]

    # join groups as str format
    new_tel = '-'.join(new_tel)

    return new_tel

if __name__ == '__main__':

    if len(sys.argv) > 1:
        tel = ''.join(sys.argv[1:])
    else:
        tel = "339 - 3921 2042"

    reformatted_tel = reformat(tel)

    print('"{}" -> "{}"'.format(tel, reformatted_tel))
