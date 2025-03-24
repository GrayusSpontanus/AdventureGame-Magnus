#Elijah Roberson
#12/2/24
#Adventure Game
import characters as ch
import rooms as r
if __name__ == '__main__':
    #Make your character                                             
    username = input("Enter your name: ")
    main_character = ch.Character(username)
    print(main_character)
    #room 1
    r.room1(main_character)

    #room 2
    r.room2(main_character)

    #room 3
    r.room3(main_character)