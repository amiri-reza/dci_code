
############################## QUESTIONS ##############################
# Main menu
main_menu_question = " A: Geography  B: Physics  C: Chemistry   D: Mathematics"
quit_program = "to quit, press Q"
subject_choice = "Select a subject to continue:"
# Geography
g1 = "What is the biggest continent in the world?"
g1o = "A: Africa  B: Europe  C: Asia   D: North America"
g1a = "c"
g2 = "which Country is the most populated country?"
g2o = "A: Brazil  B: Australia  C: Russia  D: Bangladesh"
g2a = "a"
g3 = "What is the longest river in Germany?"
g3o = "A: Rhine  B: Elbe  C: Oder  D: Danube"
g3a = "d"

# Physics
p1 = "What is light speed (approximately)?"
p1o = "A: 200,000 km/s  B: 300,000 km/s  C: 400,000 km/s   D: 100,000 km/s"
p1a = "b"
p2 = "What is Einstein's Formula for special relativity?"
p2o = "A: E=MC^2  B: E=CM^2  C: C=ME^2  D: W=m*g"
p2a = "a"
p3 = "Which answer is True about Schrödinger's Cat?"
p3o = "A: alive  B: dead  C: dead and alive  D: sleep :)"
p3a = "c"

# Chemistry
c1 = "Which answer is one of three state of matter?"
c1o = "A: soil  B: fire  C: liquids   D: A, B and C"
c1a = "c"
c2 = "What is the heaviest liquid on Earth?"
c2o = "A: Gold  B: Water  C: Platinum  D: Mercury"
c2a = "d"
c3 = "What is Avogadro's Number?"
c3o = "A: 6.022*10^23  B: 9.81*10^23  C: 6.022*10 D: 6.022"
c3a = "a"

# Mathematics
m1 = "What is 2 + 2 * 2 / 2?"
m1o = "A: 4  B: 0  C: 1   D: 6"
m1a = "a"
m2 = "What is 2 ^ 6?"
m2o = "A: 64  B: 128  C: 512  D: 1024"
m2a = "a"
m3 = "What is sin30°?"
m3o = "A: 1  B: 60°  C: 2/3  D: 1/2"
m3a = "d"
############################  EXAM   ############################


right = "Excellent, Now a little more difficult. \n"
wrong = "Sorry, you were wrong. try again!"
win = "Congratulation! Your are a Genius."
lose = "OK, you ran away!"
i = 0
while i < 4:
    print("*"*79, main_menu_question.center(79), quit_program.center(79), subject_choice.center(79), sep="\n")
    main_q = input('{:^38s}'.format(" "))  # main question input
    user_input = main_q.lower()   
    if user_input == "a":
        print(g1.center(79), g1o.center(79), quit_program.center(79), sep="\n")
        #  1st question of Geography
        user_ans = input("Your answer: ")
        if user_ans == g1a.lower():
            print(right, g2.center(79), g2o.center(79), quit_program.center(79), sep="\n")
            #  2nd question
            user_ans = input("Your answer: ")
            if user_ans == g2a.lower():
                print(right, g3.center(79), g3o.center(79), quit_program.center(79), sep="\n")
                #  3rd question
                user_ans = input("Your answer: ")
                if user_ans == g3a.lower():
                    print(win)
                
                elif user_ans == str.lower("Q"):
                    print(lose)
                    break
                else:
                    print(wrong)
            
            elif user_ans == str.lower("Q"):
                print(lose)
                break
            else:
                print(wrong)    
        
        elif user_ans == str.lower("Q"):
            print(lose)
            break
        else:
            print(wrong)
    
    elif user_input == "b":
        print(p1.center(79), p1o.center(79), quit_program.center(79), sep="\n")
        #  1st question of physics
        user_ans = input("Your answer: ")
        if user_ans == p1a.lower():
            print(right, p2.center(79), p2o.center(79), quit_program.center(79), sep="\n")
            # 2nd question
            user_ans = input("Your answer: ")
            if user_ans == p2a.lower():
                print(right, p3.center(79), p3o.center(79), quit_program.center(79), sep="\n")
                # 3rd question
                user_ans = input("Your answer: ")
                if user_ans == p3a.lower():
                    print(win)
                elif user_ans == str.lower("Q"):
                    print(lose)
                    break
                else:
                    print(wrong)
            elif user_ans == str.lower("Q"):
                print(lose)
                break
            else:
                print(wrong)    
        elif user_ans == str.lower("Q"):
            print(lose)
            break
        else:
            print(wrong)
    elif user_input == "c":
        print(c1.center(79), c1o.center(79), quit_program.center(79), sep="\n")
        # 1st question of chemistry
        user_ans = input("Your answer: ")
        if user_ans == c1a.lower():
            print(right, c2.center(79), c2o.center(79), quit_program.center(79), sep="\n")
            # 2nd question
            user_ans = input("Your answer: ")
            if user_ans == c2a.lower():
                print(right, c3.center(79), c3o.center(79), quit_program.center(79), sep="\n")
                # 3rd question
                user_ans = input("Your answer: ")
                if user_ans == c3a.lower():
                    print(win)
                elif user_ans == str.lower("Q"):
                    print(lose)
                    break
                else:
                    print(wrong)
            elif user_ans == str.lower("Q"):
                print(lose)
                break
            else:
                print(wrong)    
        elif user_ans == str.lower("Q"):
            print(lose)
            break
        else:
            print(wrong)
    elif user_input == "d":
        print(m1.center(79), m1o.center(79), quit_program.center(79), sep="\n")
        # 1st question of mathematics
        user_ans = input("Your answer: ")
        if user_ans == m1a.lower():
            print(right, m2.center(79), m2o.center(79), quit_program.center(79), sep="\n")
            # 2nd question
            user_ans = input("Your answer: ")
            if user_ans == m2a.lower():
                print(right, m3.center(79), m3o.center(79), quit_program.center(79), sep="\n")
                # 3rd question
                user_ans = input("Your answer: ")
                if user_ans == m3a.lower():
                    print(win)
                elif user_ans == str.lower("Q"):
                    print(lose)
                    break
                else:
                    print(wrong)
            elif user_ans == str.lower("Q"):
                print(lose)
                break
            else:
                print(wrong)    
        elif user_ans == str.lower("Q"):
            print(lose)
            break
        else:
            print(wrong)
    else:
        print("Please try again and enter a valid input")
        break
    i += 1