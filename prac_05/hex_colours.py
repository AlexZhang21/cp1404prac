Estimate: 5 minutes
Actual:   5 minutes


COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF",
    "BLUEVIOLET": "#8A2BE2"
    # Add more colors here
}


keep_running = True
while keep_running:
    #get color name
    color_name = input("Enter a color name (or blank to quit): ").upper()
    # if not empty
    if color_name:
        #get color code
        color_code = COLOR_CODES[color_name]
        #got the code?
        if color_code:
            print(f"The color code for {color_name} is {color_code}")
        else:
            print(f"Sorry, {color_name} is not a valid color name.")
    #entered blank, stop the loop
    else:
        keep_running = False
