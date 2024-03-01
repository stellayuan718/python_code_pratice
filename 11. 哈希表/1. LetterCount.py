def letterCount(s):
    freq = {}
    for piece in s:
        word = ''.join(c for c in piece if c.isalpha())
        if word:
            freq[word] = 1 + freq.get(word, 0)

    max_word  = ''
    max_count = 0
    # 遍历字典，记录最大数
    for (w, c) in freq.items():
        if c > max_count:
            max_word = w
            max_count = c

    print('The most frequent word is', max_word)
    print('Its number of occurrences is', max_count)

s = "Hello World How ard you I am fine thank you and you"
letterCount(s)

from collections import  Counter
def letterCount2(s):
    c = Counter(x for x in s if x != " ")

    for letter, count in c.most_common(4):
        print('%s: %7d' % (letter, count))

s = "Hello World How ard you I am fine thank you and you"
letterCount2(s)