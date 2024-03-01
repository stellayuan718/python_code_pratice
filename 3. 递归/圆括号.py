# 给n对圆括号，写函数生成所有括号的组合
# 思考：循环退出条件，序列中没有括号了
# 给一个函数，result 用来存结果，tmp用来寸临时值，也是排列组合的题目

def generateParenthesis(n):
    def generate(prefix, left, right, parens=[]):
        if right == 0: parens.append(prefix)
        if left > 0: generate(prefix + '(', left-1, right)
        if right > left: generate(prefix + ')', left, right-1)

    return generate('', n, n)


generateParenthesis(4)