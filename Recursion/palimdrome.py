# Given a string S, check if it is palindrome or not.

def palindrome(str, i):
    if i >= len(str)/2:
        return True
    
    if str[i] != str[len(str) -i -1]:
        return False
    
    if str[i] == str[len(str) -i -1]:
        i+=1
        return palindrome(str, i)
    


if __name__ == '__main__':
    str = "madam"
    status = palindrome(str, 0)
    if status is True:
        print(f"{str} is a palindrome" )
    else: 
        print(f"{str} is not a palindrome" )
   
    