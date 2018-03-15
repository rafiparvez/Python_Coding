
score_arr = [2,3,7]
num_points = len(score_arr)
target = 12

## Approach 1: Recursive
def score_combinations(score_arr, m, target):
    '''
    :param score_arr: array of scores
    :param m: number of score points under consideration
    :param target: target score
    :return:
    '''
    # When target score is 0, withouy choosing any score-points, we can make
    # this combination
    if target==0:
        return 1

    #When runs out of points under consideration
    if m <=0:
        return 0

    #We cannot sum up anything to -ve
    if target < 0:
        return 0

    else:
        # target score including mth score
        combs_includ = score_combinations(score_arr, m, target - score_arr[m-1])

        # target score excluding mth score
        combs_exclud = score_combinations(score_arr, m - 1, target)
        return combs_includ + combs_exclud

print(score_combinations(score_arr, num_points, target))


## Approach 2: DP
def score_combinations_dp(score_arr, k):
    m = len(score_arr)
    A = [[0]* (k+1) for _ in score_arr]

    #when target score k = 0, it can totaled using any score-point each in 1 way
    for i in range(m):
        A[i][0] = 1

    for i in range(m):
        for j in range(1, k+1):
            #solution excluding ith score-point
            score_point_excluding = A[i-1][j] if i>0 else 0
            score_point_including = A[i][j - score_arr[i]] \
                if (j - score_arr[i]) >=0 else 0

            A[i][j] = score_point_excluding + score_point_including

    print(A)
    return A[-1][-1]


print(score_combinations_dp(score_arr, target))