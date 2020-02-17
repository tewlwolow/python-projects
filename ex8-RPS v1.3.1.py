# import sys module for final smooth exit function and random for computer modes
import sys, random

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

# computer quick match game mode
def compquick():
    # general loop for quick match game mode
    while True:

        # player one loop + error catching
        while True:
            player_one=input("Play rock, paper, or scissors: ")
            if player_one=="leave": # forcequit in quick match mode player one input
                print("The programme will finish now.")
                quit()
            elif player_one!="rock" and player_one!="scissors" and player_one!="paper":
                print("Oops! Try again!")
                continue
            else:
                break

        # computer loop + error catching       
        player_two= random.choice(["rock","paper","scissors"])
        print("Computer played",player_two,"!")
            
            
        # general loop victory conditions + messages
        if player_one=="rock"and player_two=="paper":
            print("Paper beats rock! Computer won.")
            break
        if player_one=="rock" and player_two=="scissors":
            print("Rock beats scissors! You won.")
            break
        if player_one=="paper" and player_two=="rock":
            print("Paper beats rock! You won.")
            break
        if player_one=="paper" and player_two=="scissors":
            print("Scissors beat paper! Computer won.")
            break
        if player_one=="scissors" and player_two=="rock":
            print("Rock beats scissors! Computer won.")
            break
        if player_one=="scissors" and player_two=="paper":
            print("Scissors beat paper! You won.")
            break
        if player_one==player_two:
            print ("It's a draw!")
            break

# computer normal game mode
def compnormal():
    # asks for user-defined round number
    usr_round_nmb=input("Please enter the number of rounds you want to play: ")
    if usr_round_nmb=="Leave" or usr_round_nmb=="leave":
        print("The programme will finish now.")
        quit()
    usr_round_nmb=int(usr_round_nmb)

    # define any round in normal game mode
    def compround():
        # general loop in normal game mode round
        rc=1 # round counter
        plonesc=0 # player one score
        pltwosc=0 # player one score
        print("If you want to finish and get results before completing all rounds, type 'get results'.") # info about early results
        while True:
            # player one loop + error catching
            if rc>usr_round_nmb:
                break
            while True:
                while True:
                    print("Round",rc) # print round number
                    player_one=input("Play rock, paper, or scissors: ")
                    if player_one=="Get results" or player_one=="get results": # break if early results requested
                        break
                    if player_one=="leave": # forcequit in normal game mode player one input
                        print("The programme will finish now.")
                        quit()
                    if player_one!="rock" and player_one!="scissors" and player_one!="paper":
                        print("Oops! Try again!")
                        continue
                    else:
                        break
                    
                # go straight to results, ignore computer
                if player_one=="Get results" or player_one=="get results":
                    break
                
                # computer loop + error catching       
                player_two= random.choice(["rock","paper","scissors"])
                print("Computer played",player_two,"!")
                    
                # general loop scoring conditions + messages
                if rc>usr_round_nmb or player_one=="Get results" or player_one=="get results":
                    break
                if player_one=="rock"and player_two=="paper":
                    print("Paper beats rock! Computer scores.")
                    pltwosc+=1 # computer scores round
                    break
                if player_one=="rock" and player_two=="scissors":
                    print("Rock beats scissors! You score.")
                    plonesc+=1 # you score round
                    break
                if player_one=="paper" and player_two=="rock":
                    print("Paper beats rock! You score.")
                    plonesc+=1
                    break
                if player_one=="paper" and player_two=="scissors":
                    print("Scissors beat paper! Computer scores.")
                    pltwosc+=1
                    break
                if player_one=="scissors" and player_two=="rock":
                    print("Rock beats scissors! Computer scores.")
                    pltwosc+=1
                    break
                if player_one=="scissors" and player_two=="paper":
                    print("Scissors beat paper! You score.")
                    plonesc+=1
                    break
                if player_one==player_two:
                    print ("It's a draw! Nobody scores.")
                    break
                return plonesc, pltwosc
                
                
            rc+=1 # increments round number

            # evaluate scores after all rounds
            if rc>usr_round_nmb or player_one=="Get results" or player_one=="get results":
                if plonesc>pltwosc:
                    print("Congratulations! You won",str(plonesc),"to",str(pltwosc)+"!")
                elif pltwosc>plonesc:
                    print("Tough luck! Computer won",str(pltwosc),"to",str(plonesc)+"!")
                else:
                    print ("You're both equally skilled. Draw!")
                break
                
    compround() # begin round loops


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
        print("If you want to finish and get results before completing all rounds, type 'get results'.") # info about early results
        while True:
            # player one loop + error catching
            if rc>usr_round_nmb:
                break
            while True:
                while True:
                    print("Round",rc) # print round number
                    player_one=input("PLAYER ONE: play rock, paper, or scissors: ")
                    if player_one=="Get results" or player_one=="get results": # break if early results requested
                        break
                    if player_one=="leave": # forcequit in normal game mode player one input
                        print("The programme will finish now.")
                        quit()
                    if player_one!="rock" and player_one!="scissors" and player_one!="paper":
                        print("Oops! Try again!")
                        continue
                    else:
                        break
                    
                # go straight to results, ignore player two
                if player_one=="Get results" or player_one=="get results":
                    break
                
                # player two loop + error catching       
                while True:
                    player_two=input("PLAYER TWO: play rock, paper, or scissors: ")
                    if player_two=="Get results" or player_two=="get results": # break if early results requested after player two round
                        break
                    elif player_two=="leave": # forcequit in quick match mode player one input
                        print("The programme will finish now.")
                        quit()
                    elif player_two!="rock" and player_two!="scissors" and player_two!="paper":
                        print("Oops! Try again!")
                        continue
                    else:
                        break
                    
                # general loop scoring conditions + messages
                if rc>usr_round_nmb or player_one=="Get results" or player_one=="get results" or player_two=="Get results" or player_two=="get results":
                    break
                if player_one=="rock"and player_two=="paper":
                    print("Paper beats rock! Player two scores.")
                    pltwosc+=1 # player two scores round
                    break
                if player_one=="rock" and player_two=="scissors":
                    print("Rock beats scissors! Player one scores.")
                    plonesc+=1 # player one scores round
                    break
                if player_one=="paper" and player_two=="rock":
                    print("Paper beats rock! Player one scores.")
                    plonesc+=1
                    break
                if player_one=="paper" and player_two=="scissors":
                    print("Scissors beat paper! Player two scores.")
                    pltwosc+=1
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
            if rc>usr_round_nmb or player_one=="Get results" or player_one=="get results" or player_two=="Get results" or player_two=="get results":
                if plonesc>pltwosc:
                    print("Congratulations! Player one won",str(plonesc),"to",str(pltwosc)+"!")
                elif pltwosc>plonesc:
                    print("Congratulations! Player two won",str(pltwosc),"to",str(plonesc)+"!")
                else:
                    print ("You're both equally skilled. Draw!")
                break
                
    round() # begin round loops
     
        
# main game loop, the programme starts here with Welcome screen
while True:
    try:   
        choice=input("Welcome to the Rock Paper Scissors game. You can quit by typing 'leave'.\nChoose mode: type 'quick match', 'normal game', 'computer quick match' and 'computer normal game': ")
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
        elif choice=="computer quick match" or choice=="Computer quick match":
            compquick() # computer quick match launcher
            again=input("Do you want to play again (y/n)?") # quick match mode loops ends here, main game loop continues
            if again=="y": # y/n continue checker
                continue # main loop again
            if again=="n": # leave main loop, go to exit
                break
        elif choice=="computer normal game" or choice=="Computer normal game":
            compnormal() # computer quick match launcher
            again=input("Do you want to play again (y/n)?") # quick match mode loops ends here, main game loop continues
            if again=="y": # y/n continue checker
                continue # main loop again
            if again=="n": # leave main loop, go to exit
                break            
    except:
        print("Please choose mode.") # error catching for wrong mode name input
        continue

    # exit main game with a prior message  
    if choice=="Leave" or choice=="leave":
            print("The programme will finish now.") 
            sys.exit()
