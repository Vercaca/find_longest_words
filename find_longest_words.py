'''
 Date: 2019/02/19
 Company: AS_S
 Time given: 30 mins
 Time used : 26 mins

 Question:
    Longest Word: Design and coding question: Given a list of English words, write a program to find the longest word made of other words in the list.


'''

WORD_LIST = ['verysuperman', 'asuperman', 'super', 'man', 'very', 'superman']
# ans = 'verysuperman'

def list_minus_list(x, y):
    return list(set(x) - set(y))

def find_suspended_words(words, word, pos, suspended_word_list):
    # print('checking word: {} in pos {}'.format(word, pos))
    if word in suspended_word_list:
        return

    if len(word[pos:]) == 0:
        suspended_word_list.append(word)
        return

    for w in words:
        len_w = len(w)
        if  len_w > len(word):
            continue

        if word[pos:len_w+pos] == w:
            find_suspended_words(list_minus_list(words, [w]), word, len_w+pos, suspended_word_list)
    return


suspended_word_list = []
for word in WORD_LIST:
    find_suspended_words(list_minus_list(WORD_LIST,[word]), word, 0, suspended_word_list)


print('suspended_word_list = {}'.format(suspended_word_list))
res = max(suspended_word_list, key=lambda x: len(x))
print(res)
