color_codes = {"bisque1": "#ffe4c4", "red": "#ee3b3b", "blue": "#98f5ff", "green": "#76ee00", "forestgreen" : "#228b22"}

color_name = input("Enter the name of the color ").lower()
while color_name != "":
    print("The code for \"{}\" is {}".format(color_name, color_codes.get(color_name)))
    color_name = input("Enter the name of the color: ")