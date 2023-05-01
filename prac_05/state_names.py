"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
Estimate: 5 minutes
Actual:   5 minutes
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#print(CODE_TO_NAME)

# loop through and print all states
for i in CODE_TO_NAME:
    print("{:3} is {}".format(i, CODE_TO_NAME[i]))

#get shortname
state_code = input("Enter short state: ")
while state_code != "":
    try:
        #convert to capital
        state_code = state_code.upper()
        #get full state name
        state_name = CODE_TO_NAME[state_code]
        print(state_code, "is", state_name)
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")
