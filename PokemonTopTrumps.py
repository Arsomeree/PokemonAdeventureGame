import os
import requests

import random

global my_score
global battle_no
global opponent_score
my_score=0
battle_no=0
opponent_score=0
def random_pokemonid():
    random_number = random.randint(1,151)
    url = "https://pokeapi.co/api/v2/pokemon/{}/".format(random_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
    "1": pokemon["id"],
    "name": pokemon["name"],
    "2": pokemon ["height"],
    "3": pokemon["weight"],
}

def print_game_over():
        print()
        print("   _____          __  __ ______    ______      ________ _____  ")
        print("  / ____|   /\   |  \/  |  ____|  / __ \ \    / /  ____|  __ \ ")
        print(" | |  __   /  \  | \  / | |__    | |  | \ \  / /| |__  | |__) |")
        print(" | | |_ | / /\ \ | |\/| |  __|   | |  | |\ \/ / |  __| |  _  / ")
        print(" | |__| |/ ____ \| |  | | |____  | |__| | \  /  | |____| | \ \ ")
        print("  \_____/_/    \_\_|  |_|______|  \____/   \/   |______|_|  \_\ ")
        print()


def print_you_win():
    print()
    print("___    _______________  ___   ___              ____________________      ___ ")
    print(" \ \   / // __  \  | |  | |   \  \            /  /  /  ___  \   |  \     |  |")
    print("  \ \_/ /|||  | |  | |  | |    \  \    __    /  /  |  |   |  |  |   \    |  |")
    print("   \   / | |  | |  | |  | |     \  \  /  \  /  /   |  |   |  |  |  | \   |  |")
    print("    | |  | |__| |  | |__| |      \  \/ /\ \/  /    |  |___|  |  |  |\ \__|  |")
    print("    |_|   \____/    \____/        \___/  \___/      \_______/   |__| \______|")
    print()

def print_loser():
    print()
    print(" 88                                              ")
    print(" 88                                              ")
    print(" 88                                              ")
    print(" 88  ,adPPYba,  ,adPPYba,  ,adPPYba, 8b,dPPYba,  ")
    print(" 88 a8"     "8a I8[    "" a8P_____88 88P'   Y8   ")
    print(" 88 8b       d8  ` Y8ba,  8PP""''''  88          ")
    print(" 88 '8a,   ,a8' aa    ]8I  8b,   ,aa 88          ")
    print(" 88  `'YbbdP''  `'YbbdP''  `'Ybbd8'  88          ")
    print()

def print_battle():
    print()
    print("────────▄███████████▄────────")
    print("─────▄███▓▓▓▓▓▓▓▓▓▓▓███▄─────")
    print("────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███────")
    print("───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██───")
    print("──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──")
    print("─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─")
    print("██▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓██")
    print("██▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓██")
    print("██▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓██")
    print("███████████░░███░░███████████")
    print("██░░░░░░░██░░███░░██░░░░░░░██")
    print("██░░░░░░░░██░░░░░██░░░░░░░░██")
    print("██░░░░░░░░░███████░░░░░░░░░██")
    print("─██░░░░░░░░░░░░░░░░░░░░░░░██─")
    print("──██░░░░░░░░░░░░░░░░░░░░░██──")
    print("───██░░░░░░░░░░░░░░░░░░░██───")
    print("────███░░░░░░░░░░░░░░░███────")
    print("─────▀███░░░░░░░░░░░███▀─────")
    print("────────▀███████████▀────────")
    print()

def print_beach():
    print()
    print("                 %%%%                                         ")
    print("                  %%%%-(                                      ")
    print("               _%%%%%_/                         \ ' /         ")
    print("              _%%%%%%%%                        - (_) -        ")
    print("            _%%%%%%%/ \%                        / , \         ")
    print("           %%%%%%%%%\\ \_                                     ")
    print("            %%%%%%   \ \\                                     ")
    print("                )    /\_/                                     ")
    print("               /(___. \                                       ")
    print("             '----' (                                         ")
    print("            /       )                                         ")
    print("---....____/        (_____ __ _ ___ ___ __ _ _ _____ _ _ ___  ")
    print( "          /         )---...___ =-= = -_= -=_= _-=_-_ -=- =-_ ")
    print( "   ,'          (         ```--.._= -_= -_= _-=- -_= _=-      ")
    print("    ,-'            )                 ``--._=-_ =-=_-= _-= _   ")
    print("    '-._    '-..___(                       ``-._=_-=_- =_-=   ")
    print("        ``---....__)                            `-._-=_-_=-   ")
    print("              )|)|                                  `-._=-_   ")
    print("              '-'-.\_                                    `-.``")
    print()

def print_forest():
    print()
    print("          &&& &&  & &&                    ")
    print("     && &\/&\|& ()|/ @, &&                ")
    print("    &\/(/&/&||/& /_/)_&/_&                ")
    print("  &() &\/&|()|/&\/ '%"" &&\&              ")
    print("  &_\_&&_\ |& |&&/&__%_/_& &&             ")
    print(" &&   && & &| &| /& & % ()& /&&           ")
    print(" ()&_---()&\&\|&&-&&--%---()~             ")
    print("           \|||                           ")
    print("            |||                           ")
    print("            |||                           ")
    print("            |||                           ")
    print("      , -=-~  .-^- _                      ")
    print("            `                             ")
    print()

def print_pikachu():
    print()
    print(" :::,                                           ")
    print("  '::::'._                                      ")
    print("   '.    '.                          __.,,.''   ")
    print("    '.    '.                _..-'''':::         ")
    print("      \     \,.--....--.,-''      _:''          ")
    print("  /\   \  .               .    .-'              ")
    print(" /  \   \                   ':'                 ")
    print(" /    \  :                     :                ")
    print("/      \:                       :               ")
    print("\       :                       :               ")
    print("\      :      ,--,         ,-,  :               ")
    print("\    :      |(_):|       |():| :                ")
    print("  \   :     __'--'   __    '-'_  :              ")
    print("   \  :    /  \      \/      / \ :              ")
    print("    \  :  (    )             \_/ :              ")
    print(" .-'' . :  \__/   '--''--'      :               ")
    print(" \  . .-:'.                   .:                ")
    print("  \' :| :  '-.__      ___...-' :                ")
    print("   \::|:        ''''''          '.              ")
    print(" .,:::':  :                       '.            ")
    print("  \::\:   :                         '._         ")
    print("   \::    :     /             '-._     ''.      ")
    print("    \:    :    /              .   :-._ :-'      ")
    print("     :    :   /               :   :  ''         ")
    print("     :   .'   )'.             :   :             ")
    print("       :  :  .'   '.          :   :             ")
    print("        : '..'      :      _.' _.:              ")
    print("        '._        :..---'\'''  _)              ")
    print("           '':---''_)      '-'-'                ")
    print("              '-'-'                             ")
    print()

def get_player_name():
     # The player enters their name and gets assigned to a variable called "name"
    name = input("What's your name? > ")

    # This is just an alternative name that the game wants to call the player
    alt_name = "Slowpoke"
    answer = input("Your name is {}, is that correct? [Y|N] > ".format(alt_name.upper()))

    if answer.lower() in ["y", "yes"]:
        name = alt_name
        print("You are fun, {}! Let's begin our adventure!".format(name.upper()))
    elif answer.lower() in ["n", "no"]:
        print("Ok, picky. {}achu it is. Let's get started on our Pokemon adventure. Can you catch them all!?".format(name.upper()))
        print_pikachu()
    else:
        print("Trying to be funny? Well, you will now be called {} anyway.".format(alt_name.upper()))
        name = alt_name

    return name

def intro():

    print("\nYou are a well esteemed pokemon trainer well on your way to becoming the next pokemon master!\n"
          "After defeating Gym Leaders Brock and Misty you have nearly completed your mission of conquering the Indigo League.\n"
          "But you aren't quite ready yet! You still have more gym badges to win and many pokemon to catch! Good Luck!\n"
          "Your journey begins...you have just left home. \n")



def pokemon_battle():
        global my_score
        global  battle_no
        global opponent_score
        my_chosen_pokemon = random_pokemonid()
        print('A pokemon has appeared! Get ready to battle...')
        print_battle()
        print("you have been allocated the pokemon {}".format(my_chosen_pokemon['name']))
        # 5. Ask the user which stat they want to use (id, height or weight)
        pokemon_chosen_stat = input(
            "Choose a stat that you think will beat your opponent. Choose from: pokemon id [1] | pokemon height [2] | pokemon weight? [3] )")

        opponent_pokemon = random_pokemonid()
        print("Your opponent is the pokemon {}".format(opponent_pokemon["name"]))

        # 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

        my_pokemon_chosen_stat = my_chosen_pokemon[pokemon_chosen_stat]
        opponent_pokemon_stat = opponent_pokemon[pokemon_chosen_stat]
        if my_pokemon_chosen_stat > opponent_pokemon_stat:
            print("You have won and defeated your opponent! You are truly on your way to catching them all.")
            print("Your score was {}".format(my_pokemon_chosen_stat))
            print("Your opponent score was {}".format(opponent_pokemon_stat))
            print_you_win()
            my_score = my_score + 1
            battle_no=battle_no +1

        elif my_pokemon_chosen_stat < opponent_pokemon_stat:
            print("You have lost, what a shame, you need to sharpen up those pokemon trainer skills!")
            print("Your score was {}".format(my_pokemon_chosen_stat))
            print("Your opponent score was {}".format(opponent_pokemon_stat))
            print_loser()
            battle_no = battle_no + 1
            opponent_score=opponent_score +1
        else:
            print("You have drawn. I think you can do better than that!")
            print("Your score was {}".format(my_pokemon_chosen_stat))
            print("Your opponent score was {}".format(opponent_pokemon_stat))
            battle_no = battle_no + 1
        if not  pokemon_chosen_stat in ['1','2','3']:
         print('Stop being a Smartass and choose from the options 1,2 or 3!')
def explore():
    global my_score
    global  battle_no
    global opponent_score
    next_location = input(
        "Where do you want to start heading? Choose from: Forest [1] | next town [2] | beach? [3]")

    if next_location in ["1", ' 1']:
        print("You have chosen to head to the forest")
        print_forest()
        print('As you stroll through the long grass you hear a rustling coming from behind you.....')
        pokemon_battle()
    if next_location in ['3', ' 3']:
        print("You have chosen to head to the beach. ")
        print_beach()
        print("You wander along the beach, with the sand between your feet, on this lovely, relaxing, sunny day!\n"
              "All of a sudden, you hear a loud SPLASH!!!!")
        pokemon_battle()

    if next_location in ["2", " 2"]:
        towns=[
           {'name':"Fuchsia City",'gym_leader':"Janine", 'badge':'the Soul badge'},
           {'name': "Viridian City",'gym_leader':"Giovanni",'badge':'the Earth badge'},
           {'name': "Vermillion City",'gym_leader':"Lt. Surge",'badge':'the Thunder badge'},
           {'name': "Celedon City",'gym_leader':"Erika",'badge':'the Rainbow badge'},
           {'name': "Saffron City",'gym_leader':"Sabrina",'badge':'the Marsh badge'},
           {'name': "Cinnabar island gym ",'gym_leader':"Blaine",'badge':'the Volcano badge'},]

        random_town = random.choice(towns)
        town=random_town["name"]
        gym_leader=random_town["gym_leader"]
        gym_badge=random_town["badge"]

        print("You have chosen to head to the next town")
        print("You have entered {}.".format(town))
        battle= input("As you are here would you like to Battle the local gym leader? [Y/N]")
        if battle in ['N', 'n', 'no', 'No']:
            print(' Oh, not in the mood for a fight today? Fine you decide to explore the wonders of the city... \n '
                 'You enter the local Squirtle sunglasses emporium, as you try some sunglasses on, you catch the glance of a pokemon\n'
                  ' Seems that glance has angered it!!!!! \n'
                 'Looks like the fight may find you instead...\n')
            pokemon_battle()
        if battle in ["Yes", "Y", "yes", "y"]:
         rounds = int(input(
                 "You have made your way to the next gym leader {}! Can you defeat them? How many rounds would you like to play?".format(
                    gym_leader)))
         while rounds not in range(1, 5):
          rounds = int(input("Sorry! I can only play between 1 and 5 rounds. Try again:"))
         else:

             print("Challenge accepted! I will play you for", rounds, "rounds! Let's begin!!!")
             print_battle()
         for item in range(rounds):
          my_chosen_pokemon = random_pokemonid()

          print("You have been allocated the Pokemon: {}".format(my_chosen_pokemon['name']))
                # 5. Ask the user which stat they want to use (id, height or weight)
          pokemon_chosen_stat = input(
                    "Choose a stat that you think will beat your opponent. Choose from: pokemon id [1] | pokemon height [2] | pokemon weight [3]?)")

          opponent_pokemon = random_pokemonid()
          print("Your opponent is the pokemon {}".format(opponent_pokemon["name"]))

                # 6. Compare the player's and opponent's Pokemon on the chosen stat to decide who wins

          my_pokemon_chosen_stat = my_chosen_pokemon[pokemon_chosen_stat]
          opponent_pokemon_stat = opponent_pokemon[pokemon_chosen_stat]
          if my_pokemon_chosen_stat > opponent_pokemon_stat:
           print("You have won this round")
           print("Your score was {}".format(my_pokemon_chosen_stat))
           print("Your opponent score was {}".format(opponent_pokemon_stat))
           print_you_win()
           my_score = my_score + 1
           battle_no = battle_no + 1

          elif my_pokemon_chosen_stat < opponent_pokemon_stat:
            print("You have lost, better luck next time!")
            print("Your score was {}".format(my_pokemon_chosen_stat))
            print("Your opponent score was {}".format(opponent_pokemon_stat))
            print_loser()
            battle_no = battle_no + 1
            opponent_score=opponent_score +1
          else:
           print("You have drawn.")
           print("Your score was {}".format(my_pokemon_chosen_stat))
           print("Your opponent score was {}".format(opponent_pokemon_stat))
           battle_no = battle_no + 1
        if my_score>opponent_score:
              print("You have won and defeated {}! You have recieved {} and are truly on your way to becoming the next pokemon master!".format(gym_leader,gym_badge))
        if opponent_score>my_score:
              print('Unfortunately you have been defeated this time! You need to brush up on your poke skills!')

    if not  next_location in ['1','2','3']:
        print('Stop being a Smartass and choose from the options 1,2 or 3!')

   # print("You have chosen to head to the {}. As you start to make you way you hear a noise nearby....".format(next_location.upper()))
    #print("Oh no you have just encountered a pokemon can you defeat it?!\n\n")



# Here, insert all of your code to play one round

#4. Get a random Pokemon for the player and another for their opponent
def run_game():

    get_player_name()
    intro()
    explore()
    explore()
    explore()
    print('You have scored: {} out of {} battles.'.format(my_score,battle_no))
    if  my_score>battle_no:
        print("Congratulations you have won! You have become a fine Pokemon Master!")
    else:
        print("You have not become a Pokemon Master this time! Maybe polish up those Pokemon trainer skills and try again!")

    print_game_over()

run_game()
