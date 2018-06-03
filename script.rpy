# The script of the game goes in this file.

# Text blips

init python:
  def blipParents(event, **kwargs):
    if event == "show" and _preferences.text_cps != 0:
      renpy.sound.play("sound/blip.ogg", channel="music", loop=True)
    elif event == "slow_done" or event == "end":
      renpy.sound.stop(channel="music")

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define dad = Character("Dime a Dozen", color="#DEDEDC")
define sb = Character("Snooze Button", color="#073A7C")
define hr = Character("Honor Roll", color="#9C020E")
define ss = Character("Short Stack", color="#B6853F")
define ll = Character("Loose Leaf", color="#677538")
define an = Character("All Nighter", color="#452F91")
define pt = Character("Parentals", callback=blipParents)

# The game starts here.

label start:

    scene dr

    play sound "alarm clock.mp3" fadein 1.0 loop

    "I hear the alarm clock blaring."

    "I start to get up, it wasn’t going to stop anytime soon, so might as well get started on today."

    play sound "switch.mp3"

    "As I turn off the alarm, I get started on my usual morning routine: brush hair, teeth, the works."

    "Everything was going fine until I looked into the mirror."

    scene medicore

    "There I was, just me."

    "This was a {i}supposedly{/i} a big day for me, the first day of the rest of my life."

    "My parents were excited, sure, but me? I didn’t feel anything. Not joy, nervousness, excitement... not even fear."

    "Just...Nothing."

    "Why did my parents even name me Dime a Dozen? It's as if they knew that one day, I'd be questioning everything about myself, even my own name is plain!"

    "Would going to this school really change anything?"

    pt "Diimmeee!! It's time to go!"


    return
