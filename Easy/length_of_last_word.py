#Given a string s consisting of words and spaces, return the length of the last word in the string.
#A word is a maximal substring consisting of non-space characters only. 

def lengthOfLastWord(str):
    count = 0
    x = str.split()
    index = len(x)-1
    count = len(x[index])
    return count

def main():
    str = input("Enter a string: ")
    ans = lengthOfLastWord(str)
    print(ans)

main()