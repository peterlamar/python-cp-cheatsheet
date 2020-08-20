def find_uppercase_recursive(input_str, idx=0):
    if input_str[idx] == input_str[idx].upper():
        return input_str[idx]
    if idx >= len(input_str) - 1:
        return "No uppercase character found"
    return find_uppercase_recursive(input_str, idx + 1)

input_str_1 = "lucidProgramming"
input_str_2 = "LucidProgramming"
input_str_3 = "lucidprogramming"

print(find_uppercase_recursive(input_str_1))
print(find_uppercase_recursive(input_str_2))
print(find_uppercase_recursive(input_str_3))