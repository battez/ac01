'''
second part answer to this day's problem.
'''

# input data file provided by advent of code
file = "input-official.txt"

# this function updates the highest values tracker variable, highest
def update_top(total):
    global highest
    highest.append(total)
    highest.sort(reverse=True)
    highest.pop()
    
with open(file=file) as f:
    
    # track everything where the index will be the elf number (minus one)
    highest, total = [0,0,0], 0

    for line in f:
        
        if line != "\n":
            total+= int(line)

        elif total:
            update_top(total)

            # and reset the running total for next line
            total = 0

        else:
            pass

    else:
        # last pass required if end of file
        update_top(total)

# output
print(sum(highest), "grand total")