
def countOfSubsequenceWithSumK(index,data,sum,expectedSum)->int:
    if index == len(data):
        if sum == expectedSum:
            return 1
        return 0

    sum = sum + data[index]
    left = countOfSubsequenceWithSumK(index +1 ,data,sum,expectedSum)
    sum = sum - data[index]
    right = countOfSubsequenceWithSumK(index +1 ,data,sum,expectedSum)

    return left + right


if __name__ == '__main__':
    data = [1,2,1]
    print(countOfSubsequenceWithSumK(0 ,data,0,2))
