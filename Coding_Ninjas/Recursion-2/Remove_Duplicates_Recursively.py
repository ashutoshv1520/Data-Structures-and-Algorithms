# Problem ID 91, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string
    elif string[0]==string[1]:
        return removeConsecutiveDuplicates(string[1:])
    else:
        return string[0]+removeConsecutiveDuplicates(string[1:])
        
    

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
