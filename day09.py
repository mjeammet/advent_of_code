f = open('inputs/day09_input','r+')

def first_part():
    sum_last_numbers = 0 

    for line in f:
        history = [[]]
        history[0] = line.strip().split(" ")
        history = get_complete_history(history)

        history.reverse()

        last_number = 0
        
        for sequence in history:
            last_number += int(sequence[-1])
            
        sum_last_numbers += last_number
        print(f"This round's number is {last_number}, for a total of {sum_last_numbers}")

    return sum_last_numbers

def get_complete_history(history):
    last_sequence = history[-1]
    new_sequence = []
    for i in range(len(last_sequence)-1):
        new_sequence.append(int(last_sequence[i+1])-int(last_sequence[i]))

    history.append(new_sequence)
    if all(diff == 0 for diff in new_sequence):
        return history
    
    return get_complete_history(history)

def second_part():
    sum_first_numbers = 0 

    for line in f:
        history = [[]]
        history[0] = line.strip().split(" ")
        history = get_complete_history(history)


        history.reverse()

        first_number = 0
        
        for numseq in range(len(history)-1):
            sequence = history[numseq]
            first_number = int(history[numseq+1][0]) - first_number
            
        sum_first_numbers += first_number
        # print(f"This round's number is {first_number}, for a total of {sum_first_numbers}")

    return sum_first_numbers


print(second_part())
