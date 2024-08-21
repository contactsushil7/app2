# Given a string S, check if it is palindrome or not.

def printSubSequence(index: int, subsequence:list,listsdata:list):
    if index >= len(listsdata):
        print(subsequence)
        return
   
    subsequence.append(listsdata[index])
    index += 1
    printSubSequence(index, subsequence,listsdata)
    subsequence.pop()
    printSubSequence(index, subsequence,listsdata)



   


if __name__ == '__main__':
    listdata = [3,1,2]
    subsequence = []
    printSubSequence(0,subsequence,listdata)
   
    