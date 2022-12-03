'''
very hacky first part answer to this day's problem, 
it actually tracks which elf as well as how many calories that elf has.
'''
file = "input-official.txt"

# use this to track the answers
def update(total, idx):
    global highest, elf
    if highest < total:
        highest = total
        elf = idx

with open(file=file) as f:
    
    # track everything where the index will be the elf number (minus one)
    highest, total, idx, elf =  0, 0, 0, 0

    for line in f:
        
        if line != "\n":
            total+= int(line)
            print("adding on amount")

        else: 
            print("newline detected")            
            if total:
                idx +=1

            # add last one onto the tracker

            update(total, idx)

            # reset the running total for next line
            total = 0
    else:
        # python for/else construct -- in case it's end of file now. 
        idx +=1
        update(total, idx)



print(highest, "amount")
print(elf, "which elf")

