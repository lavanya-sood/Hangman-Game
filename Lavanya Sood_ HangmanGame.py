#Hangman by Lavanya Sood
from graphics import *
import random

#Define the main function
def main():
    #draw the window
    win = GraphWin("Hangman", 800,500)
    win.setBackground("Black")
    score = 0

    # Open a file
    fo = open("score.txt", "r+")
    readstr = fo.read();
    highscore=int(readstr)

    # Close the opened file
    fo.close()
    incre = 5
    dashes = ""
    word_found = False
    hints = None

    #background and title image
    title = Image(Point(400,250),"dreamworks vs pixar3.gif")
    title.draw(win)
    heading = "Press a key to continue"
    comments = ""
    chances = 0
    tries = []
    text = Text(Point(400+incre,450),heading)
    text.setSize(30)
    text.draw(win)
    incre = incre + 200
    text.setOutline("White")
    key = win.getKey()
    text.undraw()
    title.undraw()
    win.setBackground("Black")
    title = Image(Point(400,250),"dvsp.gif")
    title.draw(win)
    select = ""

    #select category
    while select != "d" or "p":
        select = win.getKey()

        #select dreamworks category
        if select == "d":
            title.undraw()
            bkg = Image(Point(400,250),"dreamworks.gif")
            bkg.draw(win)
            hang = "Welcome to Dreamworks"
            text = Text(Point(400,40),hang)
            text.setSize(30)
            text.draw(win)
            text.setOutline("White")
            words = ["alex","shrek","marty","fiona","gloria","melman","vitaly","stefano","po","shifu"]
            break

        #select pixar category
        elif select == "p":
            title.undraw()
            bkg = Image(Point(400,250),"pixar.gif")
            bkg.draw(win)
            hang = "Welcome to Pixar"
            text = Text(Point(400,40),hang)
            text.setSize(30)
            text.draw(win)
            text.setOutline("White")
            words = ["nemo","woody","sadness","buzz","mike","joy","sulley","dory","mcqueen","mater"]
            break

#add a score
    while words:
        scoreText="Score: "+str(score)+"\n"+"Highscore: "+str(highscore)
        scoring = Text(Point(750,20),scoreText)
        scoring.setSize(15)
        scoring.draw(win)
        scoring.setOutline("White")
        if select == "d":
            list_length = len(words)-1
            
#select a random word
            secret_position = random.randint(0,list_length)
            secret = (words[secret_position]).lower()
            words.remove(words[secret_position])
            secret_length = len(secret)
        else:
            list_length = len(words)-1
            secret_position = random.randint(0,list_length)
            secret = (words[secret_position]).lower()
            words.remove(words[secret_position])
            secret_length = len(secret)
            

#rules on how to play
        rules = "INSTRUCTIONS:\nPress a key to enter a letter and guess the word\nYou have 8 chances in total"           
        rule = Text(Point(400,440),rules)
        rule.setSize(20)
        rule.draw(win)
        rule.setOutline("White")
 
        #list of guesses
        word_guesses = []
        blanks = ""
        
#print the word in blanks form
        for i in secret:
               word_guesses.append("__  ")
        for x in word_guesses:
            blanks = blanks + x
            
        lines = Text(Point(400,120),blanks)
        lines.setSize(36)
        lines.draw(win)
        lines.setOutline("White")
        num_correct = 0
        
#list of guesses
        tried_letters = None
        tries=""
        correct_tries=""
        #setting comments as empty
        comments = None
        listof_tries = "Your Tries"
        tried_letters_text = Text(Point(400,200),listof_tries)
        tried_letters_text.setSize(20)
        tried_letters_text.draw(win)
        tried_letters_text.setOutline("White")
        
#loop
        while word_found == False and chances<8:
            guess = ""
            guess = win.getKey()
            
            #check the guess
            if len(guess) != 1 or not guess.isalpha() :
                if guess == "Escape":
                    exit()
                    win.close()
                #When the letter is not an alphabet
                comment = "That's not even a letter!"
                if comments is not None:
                    comments.undraw()
                comments = Text(Point(400,300),comment)
                comments.setSize(20)
                comments.draw(win)
                comments.setOutline("White")

            elif guess in secret and guess not in correct_tries:
                pos = 0
                lines.undraw()
                correct_tries=correct_tries+guess
                

                #checking the position of guess
                for i in range(0,len(secret)):
                    if secret[i]== guess:
                        pos = i
                        word_guesses[pos]=guess + "   "
                        num_correct = num_correct + 1
                        
                #adding the guess in word
                guess_add =""
                for x in word_guesses:
                    guess_add = guess_add + x
                lines = Text(Point(400,120),guess_add)
                lines.setSize(36)
                lines.draw(win)
                incre = incre + 60
                lines.setOutline("White")
                
                #comment for good guess
                Happy = "Good Job!"
                if comments is not None:
                    comments.undraw()
                comments = Text(Point(400,300),Happy)
                comments.setSize(25)
                comments.draw(win)
                comments.setOutline("White")
                
            #checking the list of words
            elif guess in tries or guess in correct_tries:
                #If letter already in the list
                already_try = "Already tried that"
                if comments is not None:
                    comments.undraw()
                comments = Text(Point(400,300),already_try)
                comments.setSize(25)
                comments.draw(win)
                comments.setOutline("White")
                
            #elif guess not in secret:
            else:
                wrong_try = "Nope! Try again"
                if comments is not None:
                    comments.undraw()
                comments = Text(Point(400,300),wrong_try)
                comments.setSize(25)
                comments.draw(win)
                comments.setOutline("White")
                chances = chances + 1
                tries = tries + " " + guess

            #Printing the tries
            if tried_letters is not None:
                tried_letters.undraw()
            tried_letters = Text(Point(400,240),tries)
            tried_letters.setSize(20)
            tried_letters.draw(win)
            tried_letters.setOutline("White")
            hangman=None
            
            #Print the hangman
            if chances == 1:
                hangman = Image(Point(720,300),"1.gif")
                hangman.draw(win)
                
            elif chances == 2:
                hangman = Image(Point(720,300),"2.gif")
                hangman.draw(win)
                #Hints for the characters
                if secret == "nemo" or secret == "dory":
                     hint= "HINT: This character is from Finding Nemo!"
                elif secret == "woody" or secret == "buzz":
                   hint= "HINT: This character is from Toy Story!"
                elif secret == "sadness" or secret == "joy":
                    hint= "HINT: This character is from Inside out!"
                elif secret == "mike" or secret == "sulley":
                    hint= "HINT: This character is from Monsters Inc!"
                elif secret == "mcqueen" or secret == "mater":
                   hint= "HINT: This character is from Cars!"
                elif secret == "vitaly" or secret == "stefano":
                    hint= "HINT: This character is from Madagascar!"
                elif secret == "melman" or secret == "alex":
                    hint= "HINT: This character is from Madagascar!"
                elif secret == "shrek" or secret == "fiona":
                    hint= "HINT: This character is from Shrek!"
                elif secret == "po" or secret == "shifu":
                   hint= "HINT: This character is from Kung Fu Panda!"
                elif secret == "gloria" or secret == "marty":
                    hint= "This character is from Madagascar!"
                hints = Text(Point(400,370),hint)
                hints.setSize(20)
                hints.draw(win)
                hints.setOutline("White")
                
            elif chances == 3:
                hangman = Image(Point(720,300),"3.gif")
                hangman.draw(win)
                
            elif chances == 4:
                hangman = Image(Point(720,300),"4.gif")
                hangman.draw(win)
                #undraw last hint
                hints.undraw()
                    
                #new hints after 4 wrong tries
                if secret == "nemo":
                     hint= "HINT: He is orange in color"
                elif secret == "woody":
                    hint= "HINT: He is the cowboy!"
                elif secret == "sadness":
                    hint= "HINT: She is blue in color!"
                elif secret == "mike":
                    hint= "HINT: He only has one eye!"
                elif secret == "mcqueen":
                    hint= "HINT: He is the red race car!"
                elif secret == "vitaly":
                    hint= "HINT: He is a tiger"
                elif secret == "melman":
                    hint= "HINT: He is the girraffe!"
                elif secret == "shrek":
                    hint= "HINT: He is green in color!"
                elif secret == "po":
                    hint= "HINT: He loves Martial Arts!"
                elif secret == "gloria":
                   hint= "HINT: She loves to Dance!"
                elif secret == "buzz":
                    hint= "HINT: He is the spaceranger!"
                elif secret == "dory":
                    hint= "HINT: She has a habit of forgetting"
                elif secret == "joy":
                    hint= "HINT: She is always happy!"
                elif secret == "sulley":
                    hint= "HINT: He is the big blue monster"
                elif secret == "mater":
                    hint= "HINT: He is the tow truck!"
                elif secret == "fiona":
                    hint= "HINT: She is the princess!"
                elif secret == "shifu":
                    hint= "HINT: He is the Master!"
                elif secret == "alex":
                    hint= "HINT: He is the lion!"
                elif secret == "stefano":
                   hint= "HINT: He is the seal!"
                elif secret == "marty":
                   hint= "HINT: He is the zebra"
                   
                hints = Text(Point(400,370),hint)
                hints.setSize(20)
                hints.draw(win)
                hints.setOutline("White")
                
            elif chances ==5:
                hangman = Image(Point(720,300),"5.gif")
                hangman.draw(win)
                
            elif chances == 6:
                hangman = Image(Point(720,300),"6.gif")
                hangman.draw(win)
                
            elif chances == 7:
                hangman = Image(Point(720,300),"7.gif")
                hangman.draw(win)
                
            elif chances == 8:
                hints.undraw()
                hangman = Image(Point(720,300),"8.gif")
                hangman.draw(win)
                Sad = "Oops! You're dead"
                #reveal the correct answer
                reveal = "The word was: " + secret
                answer = Text(Point(400,390),reveal)
                answer.setSize(20)
                answer.draw(win)
                answer.setOutline("White")
                #undraw the previous comment
                if comments is not None:
                    comments.undraw()
                    #Final comment
                comments = Text(Point(400,300),Sad)
                comments.setSize(30)
                comments.draw(win)
                comments.setOutline("White")

            #score
            if num_correct == secret_length:
                score += 1
                if score>highscore:
                    highscore=score
                    # Open a file
                    fo = open("score.txt", "w")
                    #write the score
                    fo.write(str(score));
                    fo.close()
                    #print score
                scoring.setText("Score: "+str(score)+"\n"+"Highscore: "+str(highscore))
                scoring.setSize(15)
                #replay the game when win
                Happy = "You got it!\nPress Return for next \nOr escape to exit"
                if comments is not None:
                    comments.undraw()
                comments = Text(Point(400,300),Happy)
                comments.setSize(30)
                comments.draw(win)
                comments.setOutline("White")
                word_found = True
#end loop          

    #PLAY AGAIN
        next=""
        while next!="Return" or next!="Escape":
            next = win.getKey()
            if next == "Return":
                #New word
                chances = 0
                tries = []
                word_found = False
                incre = 5
                dashes = ""
                false_guesses = 0
                incorrect_guesses = []
                #New DreamWorks Word
                if select == "d":
                    bkg = Image(Point(400,250),"dreamworks.gif")
                    bkg.draw(win)
                    hang = "Welcome to Dreamworks"
                    text = Text(Point(400,40),hang)
                    text.setSize(30)
                    text.draw(win)
                    text.setOutline("White")
                else:
                    #New Pixar Word
                    bkg = Image(Point(400,250),"pixar.gif")
                    bkg.draw(win)
                    hang = "Welcome to Pixar"
                    text = Text(Point(400,40),hang)
                    text.setSize(30)
                    text.draw(win)
                    text.setOutline("White")
                break
            #end the game
            elif next == "Escape":
                exit()
                win.close()

    #close window
    win.getMouse()
    win.close()

main()
