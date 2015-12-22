#make at least two if/elif/else conditionals.


def unicornName(human_name):
    for i in human_name[0]:
        if i == "a":
            return "Alpenhorn"
        elif i == "b":
            return "Barleycorn"
        elif i == "c":
            return "Candy Corn"
        elif i == "e":
            return "English Horn"
        elif i == "f":
            return "Flugelhorn"
        elif i == "g":
            return "Golden Horn"
        elif i == "h":
            return "Hawthorn"
        elif i == "l":
            return "Longhorn"
        elif i == "m":
            return "Matterhorn"
        elif i == "p":
            return "Peppercorn"
        elif i == "s":
            return "Sweet Corn"
        else:
            return "Buckthorn"


print "---------"*5
print"                             YOU   ARE    A    UNICORN !!!!!"
print "Bucolic Field of Green Grass"
print" You wake up in a field of green grass. You stand up on unsteady legs, and look down to realize you've got four legs, cloven silver hooves, and a shining, glimmering coat."
print " A moon-shaped pool of water nearby reveals your limitless eyes, silken beard, horse body, and lion's tale."
print " Any human would weep with joy at the sublime sight of you."
name = raw_input("What is your name? ").lower()
name = unicornName(name)

print " "
print "Your randomly generated unicorn name is: %s." % name
print "What a beautiful new name! You shall wear it proudly."
print "You look around. To your north is a grove of aspen trees. Their leaves flutter in a slight breeze."
print "Bluebells grow underneath the aspen trees. The bluebells are so blue and look delectable."
print "To your south is the ocean. It's quiet now; the tide has ebbed."
print "East and west are a vast expanse of undistinguishable field."

current_movement = raw_input("Would you like to go north, south, east, or west? [Type 'N','S','E' or 'W'.]").lower()
if current_movement == "n":
    print "Aspen Grove"
    print "You are in a circular grove of aspen trees. The forest floor is carpeted with a sea of bluebells gently moving in the breeze."
    bluebells = raw_input("Your mouth is watering. You are hungry after your nap. Would you like to eat the bluebells? [Type 'Y' or 'N']")
    if bluebells == "y":
        print "You lower your muzzle to gently pull a few delicate blossoms. Those things are irresistible, and they're nestled on a scrumptious bed of sweet grass."
        print "Soon you're munching away and not paying much attention to your surroundings."
        print "You hear a rustling from the aspens and look up."
        print "A human is trying unsuccessfully to hide behind a tree, but she's looking at you. You suspect from your magical unicorn-sensors that she is a Virgin."
        print "She extends her hand towards you. You smell something so intoxicating. Even better than bluebell nectar."
        print " You haven't seen one before, but you think it might be a mythical Sugar Cube."
        sugar = raw_input ("Do you approach the human and eat the sugar cube? [Type 'Y' or 'N']").lower()
        if sugar == "y":
            print "You cautiously approach and kneel down, lowering your neck to eat the Sugar Cube."
            print "It melts in your mouth with the most wonderful simultaneous grainy crunch. You look up at her and she gazes down at you with pure adoration."
            print "You could get used to this!"
            print "Thank you for playing 'YOU ARE A UNICORN !!!!!'"
            exit()
        elif sugar == "n":
            print "You whinny and rear up at the human, doing your best to look menacing."
            print "It seems to work. She looks scared. She turns around and runs away, leaving you in peace."
            print "You're free to munch on bluebells to your heart's delight. Maybe you'll work on the aspen leaves next. Yum!"
            print "Thank you for playing 'YOU ARE A UNICORN !!!!!!'"
            exit()
    elif bluebells == "n":
        print "But you're so hungry! You decide to take a nap and try being an unicorn again another day."
        exit()

elif (current_movement == "e") or (current_movement == "w"):
    print "You walk and walk in an endless green plain. You seem to have gotten yourself turned around. You're exactly where you started."
    print "You walked so far and are so exhausted, decide to take a nap and try being a unicorn again another day."
    print "Thank you for playing 'YOU ARE A UNICORN !!!!!'"
    exit()

elif (current_movement) == "s":
    print "You enjoy the feeling of sand against your hooves. You gallop merrily down to the seashore."
    print "You look out into the ocean and see your cousins, the Narwhales, frolicing."
    print "The narwhales seem to have been practicing synchronized swimming because they spell out:"
    print "'T o o   b a d   y o u    d o n ' t    k n o w    h o w   t o   s n o r k e l ,    %s !'" % name.upper() 
    print "You whinny and laugh. They're such kidders!"
    print "Awww. They've left a perfect nautilus for you, but you can't pick it up. Instead you poke your horn through it and wear it as a crown."
    print "You look beautiful!"
    print "Thank you for playing 'YOU ARE A UNICORN !!!!!'"
    exit()
