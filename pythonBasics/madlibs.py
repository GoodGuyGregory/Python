# MadLibs - Practice Input and Output
#
#Template:
#   I enjoy practice! I find it helps me to __(Verb)__ better.  
#   Without practice, my --(noun)__ would probably not even work.
#   My code is getting me __(adjective)__ every single day!

#TODO: Prompt the user for parts of speecg and store them in variables
print("I would like to play Madlibs with you!")
print("let's begin!")
print("=========================================================")
chosen_verb = input("Choose a Verb ")
chosen_noun = input("Now give me a noun ")
chosen_adjective = input("Last one, provide an adjective ")
#TODO: Output the template to the screen with the blankes filled out with what the user stated.
print("Alright weirdo, here is what you came up with:")
print("=========================================================")
print( "I enjoy practice! I find it helps me to", chosen_verb, "better.") 
print("Without practice my", chosen_noun, "would probably not even work.")
print("My code is getting me", chosen_adjective, "every single day!")