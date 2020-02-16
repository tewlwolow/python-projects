# import sys module for final smooth exit function
import sys


# quick match game mode
def quick():
    # general loop for quick match game mode
    while True:

        # player one loop + error catching
        while True:
            player_one=input("PLAYER ONE: play rock, paper, or scissors: ")
            if player_one=="leave": # forcequit in quick match mode player one input
                print("The programme will finish now.")
                quit()
            elif player_one!="rock" and player_one!="scissors" and player_one!="paper":
                print("Oops! Try again!")
                continue
            else:
                break

        # player two loop + error catching       
        while True:
            player_two=input("PLAYER TWO: play rock, paper, or scissors: ")
            if player_two=="leave": # forcequit in quick match mode player one input
                print("The programme will finish now.")
                quit()
            elif player_two!="rock" and player_two!="scissors" and player_two!="paper":
                print("Oops! Try again!")
                continue
            else:
                break
            
        # general loop victory conditions + messages
        if player_one=="rock"and player_two=="paper":
            print("Paper beats rock! Player two won.")
            break
        if player_one=="rock" and player_two=="scissors":
            print("Rock beats scissors! Player one won.")
            break
        if player_one=="paper" and player_two=="rock":
            print("Paper beats rock! Player one won.")
            break
        if player_one=="paper" and player_two=="scissors":
            print("Scissors beat paper! Player two won.")
            break
        if player_one=="scissors" and player_two=="rock":
            print("Rock beats scissors! Player two won.")
            break
        if player_one=="scissors" and player_two=="paper":
            print("Scissors beat paper! Player one won.")
            break
        if player_one==player_two:
            print ("It's a draw!")
            break


# normal game mode
def normal():
    # asks for user-defined round number
    usr_round_nmb=input("Please enter the number of rounds you want to play: ")
    if usr_round_nmb=="Leave" or usr_round_nmb=="leave":
        print("The programme will finish now.")
        quit()
    usr_round_nmb=int(usr_round_nmb)
    # define any round in normal game mode
    def round():
        # general loop in normal game mode round
        rc=1 # round counter
        plonesc=0 # player one score
        pltwosc=0 # player one score
        while True:
            # player one loop + error catching
            if rc>usr_round_nmb:
                break
            while True:
                while True:
                    print("Round",rc) # print round number
                    player_one=input("PLAYER ONE: play rock, paper, or scissors: ")
                    if player_one=="leave": # forcequit in normal game mode player one input
                        print("The programme will finish now.")
                        quit()
                    elif player_one!="rock" and player_one!="scissors" and player_one!="paper":
                        print("Oops! Try again!")
                        continue
                    else:
                        break

                # player two loop + error catching       
                while True:
                    player_two=input("PLAYER TWO: play rock, paper, or scissors: ")
                    if player_two=="leave": # forcequit in quick match mode player one input
                        print("The programme will finish now.")
                        quit()
                    elif player_two!="rock" and player_two!="scissors" and player_two!="paper":
                        print("Oops! Try again!")
                        continue
                    else:
                        break
                    
                # general loop scoring conditions + messages
                if player_one=="rock"and player_two=="paper":
                    print("Paper beats rock! Player two scores.")
                    pltwosc+=1 # player one scores round etc.
                    break
                if player_one=="rock" and player_two=="scissors":
                    print("Rock beats scissors! Player one scores.")
                    plonesc+=1
                    break
                if player_one=="paper" and player_two=="rock":
                    print("Paper beats rock! Player one scores.")
                    plonesc+=1
                    break
                if player_one=="paper" and player_two=="scissors":
                    print("Scissors beat paper! Player two scores.")
                    pltwosc+=1 # player two scores round etc.
                    break
                if player_one=="scissors" and player_two=="rock":
                    print("Rock beats scissors! Player two scores.")
                    pltwosc+=1
                    break
                if player_one=="scissors" and player_two=="paper":
                    print("Scissors beat paper! Player one scores.")
                    plonesc+=1
                    break
                if player_one==player_two:
                    print ("It's a draw! Nobody scores.")
                    break
                return plonesc, pltwosc
            rc+=1 # increments round number

            # evaluate scores after all rounds
            if rc>usr_round_nmb:
                if plonesc>pltwosc:
                    print("Congratulations! Player one won!")
                elif pltwosc>plonesc:
                    print("Congratulations! Player two won!")
                else:
                    print ("You're both equally good. Draw!")
                break
                
    round() # begin round loops
     
        
# main game loop, programme starts here with Welcome screen
while True:
    try:   
        choice=input("Welcome to the Rock Paper Scissors game. You can quit by typing 'Leave'. Choose mode: type either 'quick match' or 'normal game': ")
        if choice=="quick match" or choice=="Quick match":
            quick() # quick match launcher
            again=input("Do you want to play again (y/n)?") # quick match mode loops ends here, main game loop continues
            if again=="y": # y/n continue checker
                continue # main loop again
            if again=="n": # leave main loop, go to exit
                break            
        elif choice=="normal game" or choice=="Normal game":
            normal() # normal game launcher
            again=input("Do you want to play again (y/n)?") # normal mode loops ends here, main game loop continues
            if again=="y": # y/n continue checker
                continue # main loop again
            if again=="n":
                break # leave main loop, go to exit
    except:
        print("Please choose mode.") # error catching for wrong mode name input
        continue

    # exit main game with a prior message  
    if choice=="Leave" or choice=="leave":
            print("The programme will finish now.") 
            sys.exit()
