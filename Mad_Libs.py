# Author : Avish Shah
# Date and Time of Creation : 17 June 2020 || 22:10
# Description : Mad Libs is a phrasal template word game where one player prompts others for a list of words to substitute for blanks in a story before reading aloud. 
#               The game is frequently played as a party game or as a pastime. 

def Mad_Libs():
	name = input("Enter your friend's name: ")                      
	hours = input("Enter number of hours you traveled: ")
	vehicle = input("Enter the name of you vehicle: ")
	adj_1 = input("Enter adjective 1: ")
	adj_2 = input("Enter adjective 2: ")
	verb_1 = input("Enter verb(ing): ")
	animal = input("Enter the name of the animal: ")
	adj_3 = input("Enter adjective 3: ")
	past_verb_1 = input("Enter past tense verb 1: ")
	past_verb_2 = input("Enter past tense verb 2: ")

	print("Last month, I went to Disney World with " + name +"." 
		  " We traveled for " + hours + " hours by " + vehicle +"."
		  " Finally, we got there and it was very " + adj_1 +"."
		  " There were " + adj_2 + " people " + verb_1 + " everywhere." 
		  " There were people dressed up in " + animal + " costumes."
 		  " We also went on some " + adj_3 + " rides, called Magic Noun." 
 		    + name + " nearly fell off a ride and had to be " + past_verb_1 + 
		  " Later we went to the hotel and " + past_verb_2 + "." )

Mad_Libs()	