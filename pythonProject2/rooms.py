import characters
def room1(character):
    print("You awaken inside a small room, dimly lit by candles scattered across the walls and floors, some shaggy clothes scrappy shoes and a bag being all you have.\n"
              "Directly infront of you, you see a door with 3 locks on it, to your right you see a full wall of books.\n"
              "To your left you see what appears to be a barren wall, until you notice one large eye drawn into the wall.\n"
              "You cant see whats behind you.\n"
              "What do you want to do?\n")
    while "Key" not in character.inventory:
          user_choice = input("- Go to the left wall\n"
                  "- Go to the door\n"
                  "- Go to the right wall\n"
                  "- Look behind you\n")
          if user_choice.lower == "Go to the right wall" or "Go to right wall":
                print("As you walk closer to the wall filled with books it sems you are being...resisted forced away from it.\n"
                          "Regardless, you press onwards. The books seem to be crumbling and Dusty, however there is one row with 6 "
                          "different books that seem to call to you\nLiterally or metaphorically you cant tell\nOne book seems "
                          "charred at the ends, one seems covered in dirt, while the one directly next to it seems to take up much "
                          "more space than the others\nOne book is covered in cobwebs, one is feels like its looking at you, wanting"
                          " youo know more about it..or it wants to know more about you\nThe Final book seems to be covered in "
                          "scratch marks and blood soaked deep into its edges\n"
                          "Which do you choose?\n -Charred\n Dirty\n Spacious\n Cobwebs\n Scratched\n")
                user_fear = input("Choose Wisely:")
                if user_fear.lower == "Charred":
                    print("As you touch the book you can feel a sudden warmth surrund you that wasnt there before\n"
                              "When you lookat the title of the book, 'Wir brennen alle ab', that warmth becomes a discomforting heat that fires beneath you skin\n"
                              "You begin to feel the burn, but you cant tell if you like it or not, you quickly put the book in the your bag")
                    character.marks.append("The Desolation")
                    character.health -= 7
                    character.fear += 7
                elif user_fear.lower == "Dirty":
                    print("You grab the book swiping the dirt and dust off of the cover, but you still cant read it.\n"
                          "Suddenly every piece of clothing you are wearing, no matter how baggy it truly is feels just a bit too tight, too compressed on your body\n"
                          "A you read the book the floor seems to begin to concave beneath you, causing you to sink, the wood panels of thius ground hugging you tightly,"
                          "feeling like the loving embrace of warm dirt walls\n"
                          "No matter how freaked out you are by this sudden tightness, you cant tell if you like it or not. You place the book in your bag, stepping out of this sudden hole in the floor and decide to move on\n")
                    character.marks.append("The Buried")
                    character.fear += 9
                elif user_fear.lower == "Spacious":
                    print("While the book appears heavy when you look at it, when you grab iut suddenly it is so much lighter than air.\n"
                          "When you flip through the pages they discuss the joy of falling and the widness of our universe, and you can't help to smell hints of ozone with each page turn\n"
                          "You realize your body aswell feels lighter than air, you decide to put the book away hoping itll keep you grounded, but you know it wants to float away too\n ")
                    character.marks.append("The Vast")
                    character.fear += 5
                elif user_fear.lower == "Cobwebs":
                    print("You swipe and swat the several spider webs and tiny spiders scuttling across the cover of the book off, so you can try to read it.\n"
                          "Though you try to open and it feels you have to pry the pages open cause they themselves are stuck together by spiderwebs. You seem to have to swipe off another set of spiders every other page\n"
                          "As the spiders keep crawling on you you are disgusted though you seem to think there is an inherent beauty in their intricate patterns and resilience.\n"
                          "They are small but deeply intelligent and truly strong creatures, this seems to compell you, both the words of the book and the webs themselves make you want to put the book in your bag\n"
                          "Its no mystery when a swarm of spiders scuttles out of the mouth of your bag and back to the bookcase, but for every hundred that crawled out you swear you can heaar millions more scuttling around inside the bag itself.\n")
                    character.marks.append("The Web")
                    character.fear += 12
                elif user_fear.lower == "Scratched":
                    print("It smells rancid, of dried blood. The pages crack and crumble if you dont handle them with care, the dried blood soaked into their pages making them fragile.\n"
                          "The book tells a story of a huntsman and a werewolf chasing eachother eternily. For they are both trapped in this eternal dance of hunting.\n"
                          "Back and forth back and forth the werewolf is so close to catching the huntsman but the huntsman evades\n"
                          "Similarly, the huntsman gets so very close to catching the werewolf but he evades in turn, you seem to find a beauty in this glorious dance of hunting and chasing\n"
                          "The idea of being a predator and no longer being prey entices you as you feel your, once short and now long nails digging into the leather cover of this book\n"
                          "With a toothy grin filled with your overbearingly large canines, you finish that section oif the book and place the scratched book into your bag.")
                    character.marks.append("The Hunt")
                    character.fear += 10
                else:
                    print("You look for this book title, up and down, from the highest top left corner all the way to the lowest bottom right but dont see anything by its names\n"
                          "Discouraged you turn around and walk back to the center of the room thinking about what to do next")
          elif user_choice.lower == "Go to left wall" or "Go to the left wall":
                    print("As you walk to the left wall the scratched lines forming the giant eye seem to begin glowing this "
                          "sickingly bright shade of green\n"
                          "A feeling flushes through your body, a feeling of being watched, of being known, of being completley"
                          " realized and everything that you are being judged and critiqued\n"
                          "Though you can hear something clatter along thefloor, you pick it up and look at it, its a key!\n"
                          "It seems to be very oddly shaped\n")
                    character.inventory.append("Key")
                    character.marks.append("The Eye")
                    character.fear += 15
          elif user_choice.lower == "Look behind me" or "Look behind you":
              print("You turn your head, you can feel a chilling feeling creep up your spine and see nothing, not that there "
                    "is nothing to be seen but it seems that you simply cant see it.\n"
                    "The darkness of the room that was one pushing on your back is now pushing onto your face. It is malicious and hateful.\n"
                    "This fear forces you to turn back around, forever with the secrets pushing down on your back\n")
              characters.marks.append("The Dark")
              characters.fear += 15
          elif user_choice.lower == "Go to the door" or "Go to door":
              print("As you walk to the door it becmes clear. Even with all your skills, detective, wat...detective...weird.\n"
                    " Reagrdless, with all your skills this lock cant be picked, youll need a specific key for it\n")
          else:
              print("Im sorry, even though im all-seeing I couldn't understand that absolute tomfoolery you just said to me, try again")




def room2(characters):
    print("The Key twists and turns and unlocks into a new room\n"
          "You look around and the room seems to be...well not a room at all infact, what made you even think that silly?\n"
          "You are outside, the grass brushes softly across your face as you push yourself off the ground\n"
          "You take a deep breath in and your lungs are suddenly filled with fog, the fog begins to choke you so you cough it all up\n"
          "Thats when you realize the door behind you is gone, a dissipating fog  left in its place.\n"
              "The idea of being alone forces into your soul, not a faulty loneliness like your life has been, truly alone\n"
              f"No one may have understood you in your life, but they were still around, you chose not to speak to them, {characters.name}\n"
              "Here and now you are truly all alone, no one around to be a bother to\n"
              f"What do you want to do now,{characters.name}")
        user_choice2 = input("- Walk forwards"
                             "- Walk to the left\n"
                             "- Walk to the right\n"
                             "- Walk backwards\n"
                             "- Check your bag\n")


      def room3(character):
          pass