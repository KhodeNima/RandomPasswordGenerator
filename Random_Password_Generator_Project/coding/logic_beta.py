from database.data import randint


characters_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

characters_list = list(characters_list)
length_of_characters = len(characters_list)
random_result = []

user_desired_lengh = input( "> ")
user_desired_lengh = int(user_desired_lengh)


while len(random_result) < user_desired_lengh :
    random_number = randint(0,length_of_characters) - 1
    random_number2 = randint(0 , length_of_characters) - 1

    if random_number2 == random_number:

        try:
            random_result.append(characters_list[random_number])
        except IndexError:
            print(random_number2)
            print(random_number)


random_result_string = ""
for character in random_result:
    random_result_string += character

print(random_result_string)
    