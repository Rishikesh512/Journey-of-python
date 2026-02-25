color = input('Enter trafic light color(Red/Yellow/Green):')

if color.lower() == "red" :
    print("Stop")

elif color.lower() == "yellow" :
    print("Wait")

elif color.lower() == "green" :
    print("Go")

else :
    print("Invalid color please select Red,Yellow,Green color")