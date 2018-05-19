# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define jd = Character("John Doe", color="#DEDEDC")
define sb = Character("Snooze Button", color="#073A7C")
define hr = Character("Honor Roll", color="#9C020E")
define ss = Character("Short Stack", color="#B6853F")
define ll = Character("Loose Leaf", color="#677538")
define an = Character("All Nighter", color="#452F91")
define pt = Character("Parentals")

# The game starts here.

label start:

    scene ttb

    pt "Diimmeee!! It's time to get up!"

    "Errughhhh... What time is it?"

    pt "Dime! Come on, today's your orientation!!"

    "Oh Celestia, that's today?"

    pt "DIME I SWEAR TO FUCKING CHRIST YOU GET YOUR ASS UP NOW."

    "o shit dont wanna get my ass beat" 

    jd "hello!"

    sb "hey!"

    hr "fuck you."

    ss "that was uncalled for..."

    ll "god i love you short stack"

    an "whoa whoa calm your panties."


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
