def sumOfsubSequence(index, sequence,data,sum, expectedSum) -> bool:
    if index == len(data):
        if sum == expectedSum:
            print(sequence)
            return True
        return False
    
    sequence.append(data[index])
    sum += data[index]
    
    if sumOfsubSequence(index + 1, sequence, data, sum, expectedSum) == True:
        return True
    
    sequence.pop()
    sum -= data[index]
    if sumOfsubSequence(index + 1, sequence, data, sum, expectedSum) == True:
        return True
    
    return False

if __name__ == '__main__':
    data = [1,2,1]
    sequence = []

    sumOfsubSequence(0, sequence, data,0, 2)

