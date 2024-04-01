while True:
    swimming_time = input("How many minutes did you complete the swimming\n"
                        "event in? ")
    if not swimming_time.isdigit():
        print("Please enter your event time in a number format (minutes).")
        continue
    running_time = input("How many minutes did you complete the running event"
                        "\nin? ")
    if not running_time.isdigit():
        print("Please enter your event time in a number format (minutes).")
        continue
    cycling_time = input("How many minutes did you complete the cycling event"
                        "\nin? ")
    if not cycling_time.isdigit():
        print("Please enter your event time in a number format (minutes).")
        continue
    traiathlon_time = int(swimming_time) + int(running_time) + int(cycling_time)
    if traiathlon_time <= 100:
        print(f"Your total triathlon time is {traiathlon_time} minutes.\n"
            "Congratulations! You have received the provincial colours award.")
    elif traiathlon_time > 100 and traiathlon_time <= 105:
        print(f"Your total triathlon time is {traiathlon_time} minutes.\n"
            "Congratulations! You have received the provincial half colours\n"
            "award.")
    elif traiathlon_time >= 106 and traiathlon_time <= 110:
        print(f"Your total triathlon time is {traiathlon_time} minutes.\n"
            "Congratulations! You have received the provincial scroll award.")
    elif traiathlon_time >= 111:
        print(f"Your total triathlon time is {traiathlon_time} minutes.\n"
            "Unfortunately you have received no award.")
    else:
        print("Sorry. Please enter your event time in a number format (minutes).")
    exit_loop = input("Do you want to calculate your total triathlon time\n"
                      "again? (y/n): ").lower()
    if exit_loop == "y":
        pass
    else:
        print("Goodbye. Best of luck at the Triathlon Games next year!")
        break
