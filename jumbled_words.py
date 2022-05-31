import random
def choose():
    words=['computer','science','programming','board','rainbow','mathematics','water','reverse','condition']
    pick=random.choice(words)
    return pick
def jumble(word):
    jumbled="".join(random.sample(word,len(word)))
    return jumbled
def thank(p1n,p2n,p1,p2):
    print(p1n,",your score: ",p1)
    print(p2n,",your score: ",p2)
    print("Thanks for playing,Have a nice day...")
def play():
    p1name=input("Player 1,Please enter your name: ")
    p2name=input("Player 2,Please enter your name: ")
    po1=0
    po2=0
    turn=0
    while(1):
        picked_word=choose()
        qn=jumble(picked_word)
        print(qn)
        if(turn%2==0):
            print(p1name," ,your turn")
            ans=input("what's on your mind: ")
            if(ans==picked_word):
                po1=po1+1
                print("Your score= ",po1)
            else:
                print("Better luck next time,i thought ",picked_word)
            c=input("Press 1 to continue and 0 to exit...")
            c=int(c)
            if(c==0):
                thank(p1name,p2name,po1,po2)
                break
        else:
             print(p2name," ,your turn")
             ans=input("what's on your mind: ")
             if(ans==picked_word):
                 po2=po2+1
                 print("Your score= ",po2)
             else:
                 print("Better luck next time,i thought ",picked_word)
             c=input("Press 1 to continue and 0 to exit...")
             c=int(c)
             if(c==0):
                 thank(p1name,p2name,po1,po2)
                 break
        turn=turn+1
play()
            
                      