# a troubleshooting program using python

import time
import sys
import os

# welcoming the user
print("Welcome to the Troubleshooting Program Version 1.1")
print("")  # leaving blank line

# asking the user for an input to the first question that will be asked, the question can be changed to the question of your choice
question1 = input(str("Is The Screen of Your Phone Broken - yes/no :"))

# if the user says yes
if question1 == "yes":
    print("Please Repair Your Phone From the Nearest Service Center.")
    print("")  # solution to the problem
    sys.exit()
    # stops the program

# if user says anything other than yes
else:
    question2 = input(
        str("Does the Battery of Your Phone Drain Out Too Fast - yes/no :"))

    if question2 == "yes":
        print("Please Try to Uninstall some Game or Apps from Your Phone or Run Your Phone on Power Saving Mode to Save Battery life.")
        sys.exit()

    else:
        question3 = input(str("Is Your Phone Got WEt - yes/no :"))
        if question3 == "yes":
            print("Please Try to Dry Your Phone Using a Hair Dryer.")
            sys.exit()
        else:
            print(
                "Sorry there are no more Solutions Left in the Troubleshooting Problem.")
            print("")
            print("Thank You for Using Troubleshooting Program Version 1.1")
