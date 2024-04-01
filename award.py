def calculate_triathlon_time():
    # Loop until the user decides to stop calculating triathlon time
    while True:
        # Gather input for swimming time
        swimming_time = input("How many minutes did you complete the swimming\n"
                              "event in? ")
        # Validate input for swimming time
        if not swimming_time.isdigit():
            print("Please enter your event time in a number format (minutes).")
            continue
        
        # Gather input for running time
        running_time = input("How many minutes did you complete the running event"
                             "\nin? ")
        # Validate input for running time
        if not running_time.isdigit():
            print("Please enter your event time in a number format (minutes).")
            continue
        
        # Gather input for cycling time
        cycling_time = input("How many minutes did you complete the cycling event"
                             "\nin? ")
        # Validate input for cycling time
        if not cycling_time.isdigit():
            print("Please enter your event time in a number format (minutes).")
            continue

        # Calculate total triathlon time
        triathlon_time = int(swimming_time) + int(running_time) + int(cycling_time)
        
        # Determine award based on triathlon time
        if triathlon_time <= 100:
            award = "provincial colours"
        elif 100 < triathlon_time <= 105:
            award = "provincial half colours"
        elif 105 < triathlon_time <= 110:
            award = "provincial scroll"
        else:
            award = "no"

        # Display triathlon time and award
        print(f"Your total triathlon time is {triathlon_time} minutes.")
        if award != "no":
            print(f"Congratulations! You have received the {award} award.")
        else:
            print("Unfortunately you have received no award.")

        # Ask if the user wants to calculate triathlon time again
        exit_loop = input("Do you want to calculate your total triathlon time\n"
                          "again? (y/n): ").lower()
        if exit_loop != "y":
            print("Goodbye. Best of luck at the Triathlon Games next year!")
            break

# Test the function
calculate_triathlon_time()
