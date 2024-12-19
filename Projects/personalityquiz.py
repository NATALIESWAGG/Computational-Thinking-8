# Beginning

summer_points = 0
fall_points = 0

#Middle/questions

answer = input("Would you rather eat A) Ice Cream, or B) Apple Pie?\n")
if answer == "A":
    summer_points += 1
elif answer == "B":
    fall_points += 1

answer = input("Which bird is better A) Flamingo, or B) Owl?\n")
if answer == "A":
    summer_points += 1
elif answer == "B":
    fall_points += 1

answer = input("What do you prefer to wear A) Tank Tops/T-Shirts, or B) Sweaters/Hoodies?\n")
if answer == "A":
    summer_points += 1
elif answer == "B":
    fall_points += 1       

answer = input("Which type of movie would you rather watch A) Comedy, or B) Horror?\n")   
if answer == "A":
    summer_points += 1
elif answer == "B":
    fall_points += 1

answer = input("Which color scheme is prettier A) Teal Hot Pink and Green, or B) Orange Red and Yellow?\n")
if answer == "A":
    summer_points += 1
if answer == "B":
    fall_points += 1

answer = input("Do you like to A) go outside and swim, or B) stay inside and read or watch tv?\n")
if answer == "A":
    summer_points += 1
if answer == "B":
    fall_points += 1

answer = input("Would you rather drink A) lemonade and iced tea, or B) hot chocolate and chai?\n")
if answer == "A":
    summer_points += 1
if answer == "B":
    fall_points += 1

answer = input("Lastly, do you like A) hot and sunny weather, or B) cold and cloudy weather?\n")
if answer == "A":
    summer_points += 1
if answer == "B": 
    fall_points += 1


#Ending/results

if summer_points > fall_points:
    print("You are a summer person!")    
elif fall_points > summer_points:
    print("You are a fall person!")
elif summer_points == fall_points:
    print("You like fall and summer the same amount!")