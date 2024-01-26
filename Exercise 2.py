
def print_sum_of_current_and_previous(limit):
    print ("Printing current and previous number sum in a range(10)")
    
    # Initialize the previous number to 0
    pnum = 0

    # Iterate through the range of numbers
    for cnum in range(limit):
        # Calculate the sum of the current and previous number
        sum = cnum + pnum

         # Printing the current number, previous number, and their sum
        print(f"Current Number {cnum} Previous Number: {pnum}  Sum: {sum}")
        
        # Update the previous number for the next iteration
        pnum = cnum

# Call the function with the limit set to 10
print_sum_of_current_and_previous(10)



            