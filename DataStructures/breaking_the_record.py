# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    ma = mi = scores[0]
    solution = [0,0]
    for ele in scores:
        if ele > ma:
            solution[0] += 1
            ma = ele
        if ele < mi :
            solution[1] += 1
            mi = ele
    return solution


if __name__ == '__main__':
    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
