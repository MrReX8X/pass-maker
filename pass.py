import random

# colors

yellow='\033[93m'

gren='\033[92m'

cyan='\033[96m'

pink='\033[95m'

red='\033[91m'

b='\033[1m'

# code

print (red+b+"""

 _______  _______  _______  _______         __   __  _______  ___   _  _______  ______   

 |       ||   _   ||       ||       |       |  |_|  ||   _   ||   | | ||       ||    _ |  

 |    _  ||  |_|  ||  _____||  _____| ____  |       ||  |_|  ||   |_| ||    ___||   | ||  

 |   |_| ||       || |_____ | |_____ |____| |       ||       ||      _||   |___ |   |_||_ 

 |    ___||       ||_____  ||_____  |       |       ||       ||     |_ |    ___||    __  |

 |   |    |   _   | _____| | _____| |       | ||_|| ||   _   ||    _  ||   |___ |   |  | |

 |___|    |__| |__||_______||_______|       |_|   |_||__| |__||___| |_||_______||___|  |_|

                                                                                                         v 1.0

                                                                                                         """+b+red)

print (gren+b+"              <===[[ coded by Mr ReX 8X ]]===>"+b+gren)

print (" ")

print (yellow+b+"        <---( search on youtube Mr ReX 8X )--->"+b+yellow)

print (" ")

length=int(input(cyan+b+"Enter The Length Of The Password: "+b+cyan))

print (" ")

print (yellow+b+"-----> password  generated <----"+b+yellow)

print (" ")

char="abcdefghijklmnopqrstuvwxyz1234567890@#$%&*^"

password= (gren+b+" "+b+gren)

for i in range(length):

     password+=random.choice(char)

print(password)

print (" ")

print (yellow+b+"-----> grab your password <----"+b+yellow)

print (" ")
