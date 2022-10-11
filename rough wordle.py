import random
from collections import Counter

words = open('wordle.txt').read().splitlines()
# Loads possible answers into a list
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# All letters in alphabet

ans = 'swath'
# Picks random answer

n = input('Input your chosen word length: ')
# Input your guess

def wordle(ans, gss, n): # if ans = 'swath' and gss = 'state' outputs GYGG- but should be G-GG-
   
    """
    Parameters
    ----------
    ans : string
        Randomly chosen target word which we are trying to find.
    gss : string
        Our guess of the target word.
    n : int
        Length of word which we will play by.

    Returns
    -------
    output : string
        Sequence of characters given as a hint after guess is inputted.
    """
    
    output = ''
    pos = 0
    rpt = []
    Counter(elem[0] for elem in rpt)
    
    for i in gss:
        if i == ans[pos]:
            if gss.count(i) > ans.count(i):
                
            rpt.append((i, pos))
            output += 'G'
        elif i in ans:
            if rpt[pos].count(i) == ans.count(i) and gss.count(i) > ans.count(i):
                output += '-'
            else:
                rpt.append((i, pos))
                output += 'Y'
        else:
            rpt.append((i, pos))
            if i not in letters:
                output += '-'
            else:
                letters.remove(i)
                output += '-'
        print(rpt)
        pos += 1
    rpt = []
    print('Output:     ', output)
    print('Letters remaining:', letters)
    return output, output == 'GGGGG' # true if correct, false otherwise

num_of_gss = 0
gss_crctly = False
    
while num_of_gss < 6 and not gss_crctly:
    guess = input('Input your guess of length '+ str(n) + ': ')
    num_of_gss += 1     
    print('Guess #' + str(num_of_gss) + ':   ', guess)
    gss_crctly = wordle(ans, guess, n)[1]

if gss_crctly:
    print('Well done! You guessed the final word in', num_of_gss, 'guesses.')
else:
    print('Unlucky...the final word was', ans + '.')
    