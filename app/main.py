from collections import Counter


def char_count_function(input_string: str) -> int:
    string = input_string.lower()
    output_counter: int = 0
    counter = Counter(string)
    for each_item, count in counter.items():
        if count > 1:
            output_counter = output_counter + 1

    return output_counter


user_string = input("Enter your string to have some fun: ")
if not user_string.isalpha():
    print("Not a string. Only strings without spaces are acceptable.")
else:
    result = char_count_function(user_string)
    print(result)
