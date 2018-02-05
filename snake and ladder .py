import random
count=0
while(count<100):
    roll=input("enter 'r' to roll a dice")
    if roll=='r':
        r=random.randint(1,6)
        print("your random no is ",r)
        print("you are in postion",count)
        print("your count",count)
        count=count+r
        print(count)
    if count>100:
        print("your number is greater than 100 ")#if it is more tn 100 play again
        count=count-r
    elif count==100:
         print("you win")#you will be won 
          
            
    elif count==8:
         count=37
         print("move towards 37")#there is ladder where u climb
    elif count==11:
         count=2
         print("snake bite ooops") #snakes bites u 
    elif count==13:
         count=34
         print("move towards 34")#another ladder where u climb
    elif count==25:
         count=4
         print("hohoho snake bite again")#big snake bites u 
    elif count==38:
         count=9
         print("here i come hahaha")#snake bite 
    elif count==40:
         count=68
         print("move towards 68")#up up away to 64
    elif count==52:
         count=81
         print("yippe towards 81")#climb to 81    
    elif count==65:
         count=46
         print("ouch!! sanke bite")#huge snake bite 
    elif count==76:
         count=97
         print("yahoo u can do it 97")#near to the finish point 
    elif count==89:
         count=70
         print("hehe go back to 70")#back to 70 snake bite
    elif count==93:
         count=64
         print("oops!! go to 64")#again snake bite 
    else:
        print("play agian")
       
