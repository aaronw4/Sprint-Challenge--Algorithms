'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    # LC_word = word.lower()
    letters = list(word)
    last = len(letters) - 1

    def count_helper(arr, count=0, position=0):
        
        if position == last:
            print (count)
            return count
        elif arr[position] == 't' and arr[position + 1] == 'h':
            count += 1
            return (count_helper(arr, count, position + 1))
        else:
            return (count_helper(arr, count, position + 1))

    if len(letters) < 2:
        return 0
    else:
        return count_helper(letters)   


       
