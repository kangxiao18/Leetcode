# # Derangement
# # A derangement is a permutation of elements such that no element appears in its original position.
# # Example: for N = 4, { 2143, 2341, 2413, 3142, 3412, 3421, 4123, 4312, 4321 }
# #
# # Problem: Given a positive integer N, print all derangements. (Order of different derangements does not matter)
# 深度优先搜索实现错位重排问题
count = 0


def getN(N):
    assert type(N) == type(1), "输入数据类型错误!!!"
    assert N > 0, "输入数据取值范围错误!!!"
    global count
    count = 0
    count_shuffle_num([None], list(range(1, N + 1)), N)


def count_shuffle_num(prior, resNums, chosNums):
    global count
    if chosNums < 1:
        return
    elif chosNums == 1:
        prior = prior + resNums
        if len(prior) - 1 != prior[-1]:
            count += 1
            # print(prior)
            print('              ', prior[1:], '\tcount =', count)
        return
    else:
        for i in resNums:
            if i == len(prior):
                continue
            else:
                resNums_ = resNums[:]
                resNums_.remove(i)
                count_shuffle_num(prior + [i], resNums_, chosNums - 1)


if __name__ == '__main__':
    a = 5
    print('位置序号标记->', list(range(1, a + 1)), '<-位置序号标记')
    getN(a)
    print('综上所述:\tD{0} = {1}'.format(a, count))
