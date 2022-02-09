given_str = 'tadadattaetadadadafa' # can use user input here.

pattern = 'dada'   # can use user input here.

# given_str = input('word: ') # user input

# pattern = input('find pattern: ') # user input

count = 0  # initialize pattern find  count

for i in range(0,len(given_str)):   # iterrate over given_str.
    if given_str[i:i+len(pattern)] == pattern:  # match pattern based on current index .
        count +=1         # count increment 

print(count)
    
