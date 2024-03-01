results = set()
keys = set()


def permLetter(word, rule):
    rule = rule.lower()
    for c in rule:
        keys.add(c)
    permHelper(word, rule, 0, "")


def permHelper(word, rule, index, prefix):
    length = len(word)

    for i in range(index, length):
        c = word[i]
        # i 是位置函数
        # prefix 是结果函数
        if (c in keys):
            permHelper(word, rule, i + 1, prefix + c)

            # 回退到发现字母的那里， 将字母大写
            c = c.upper()

            # 重新进入递归
            permHelper(word, rule, i + 1, prefix + c)
        else:
            prefix += c

    # 跳出递归方法
    if (len(prefix) == len(word)):
        # 这一次遍历结束了，将结果添加到result中
        results.add(prefix)


word = "medium-one"
rule = "nm"

permLetter(word, rule)
print(results)