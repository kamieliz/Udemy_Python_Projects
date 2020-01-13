# Functions may include parameters and return values
# limit functions to one task and include a docstring in the function to provide info
#structure of Functions
# def name_of func(param1, param2):
#   code to perform operations (must be indented)
#   return val

def get_input_from_user():
    return input("Enter your response -> ")


print("Welcome to the program, what is your name?")
name_result = get_input_from_user()

print("What did you think of the food you ate today?")
food_result = get_input_from_user()

print("What tv show ending did you dislike the most ever?")
show_result = get_input_from_user()

print(f"To summarize: Your name is {name_result.capitalize()}, you ate {food_result} food today and hated the ending of {show_result.upper()}")
