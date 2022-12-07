"""
https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter
"""
from typing import List, Type


def get_length_of_digit(digit: int) -> int:
    return len(str(digit))


def fill_space(digit: int, width: int) -> str:
    length = len(str(digit))
    left = width - length

    result = ""
    if left > 0:
        for i in range(0, left):
            result += " "
    result += str(digit)
    return result


def generate_repeat_str(s: str, count: int) -> str:
    result = ""
    for i in range(0, count):
        result += s;
    return result;


def arithmetic_arranger(array: list[str], print_result: bool = False) -> str:
    if len(array) > 5:
        return "Error: Too many problems."
    all_str_list = list[list[str]]()
    for v in array:
        temp_array = v.split(" ")

        num_str1 = temp_array[0]
        num_str2 = temp_array[2]
        operator_str = temp_array[1]
        if not (operator_str == "-" or operator_str == "+"):
            return "Operator must be '+' or '-'."
        if len(num_str1) > 4 or len(num_str2) > 4:
            return "Error: Numbers cannot be more than four digits."

        if not num_str1.isdigit() or not num_str2.isdigit():
            return "Error: Numbers must only contain digits."

        num_1 = int(num_str1)
        num_2 = int(num_str2)
        num_result = num_1 + num_2 if operator_str == "+" else num_1 - num_2

        # 9999+9999=19998, max_length_digit=19998, max_width=6
        # 1-3801=-3800, max_length_digit=-3800, max_width=6
        num_1_length = get_length_of_digit(num_1)
        num_2_length = get_length_of_digit(num_2)
        max_width = max(num_1_length, num_2_length) + 2

        list_str = list[str]()
        list_str.append(fill_space(num_1, max_width))
        list_str.append(operator_str + fill_space(num_2, max_width - 1))
        list_str.append(generate_repeat_str("-", max_width))
        if print_result:
            list_str.append(fill_space(num_result, max_width))

        all_str_list.append(list_str)

    result = ""
    size = 4 if print_result else 3
    for i in range(0, size):
        for j, list_tmp in enumerate(all_str_list):
            result += list_tmp[i]
            if not j == len(all_str_list) - 1:
                result += "    "
        if not i == size - 1:
           result += "\n"

    return result


assert (generate_repeat_str("-", 2) == "--")
assert (generate_repeat_str("-", 5) == "-----")

assert (fill_space(12, 2) == "12")
assert (fill_space(12, 3) == " 12")
assert (fill_space(12, 5) == "   12")

assert (arithmetic_arranger(["1 * 2"]) == "Operator must be '+' or '-'.")
assert (arithmetic_arranger(["1 / 2"]) == "Operator must be '+' or '-'.")
assert (arithmetic_arranger(["1 ÷ 2"]) == "Operator must be '+' or '-'.")
assert (arithmetic_arranger(["1 x 2"]) == "Operator must be '+' or '-'.")
assert (arithmetic_arranger(["1 × 2"]) == "Operator must be '+' or '-'.")

assert (arithmetic_arranger(["11234 + 2"]) == "Error: Numbers cannot be more than four digits.")
assert (arithmetic_arranger(["1 + 11111"]) == "Error: Numbers cannot be more than four digits.")
assert (arithmetic_arranger(["a + 2"]) == "Error: Numbers must only contain digits.")
assert (arithmetic_arranger(["1 + 2", "1 + 2", "1 + 2", "1 + 2", "1 + 2", "1 + 2"], ) == "Error: Too many problems.")


assert (arithmetic_arranger(["1 + 2"]) ==
        ('  1\n'
         '+ 2\n'
         '---'))

assert (arithmetic_arranger(["1 + 2"], True) ==
        ('  1\n'
         '+ 2\n'
         '---\n'
         '  3'))

assert (arithmetic_arranger(["1111 + 2222"], True) ==
        ('  1111\n'
         '+ 2222\n'
         '------\n'
         '  3333'))

assert (arithmetic_arranger(["1111 + 2222", "2222 + 3333"], True) ==
        ('  1111      2222\n'
         '+ 2222    + 3333\n'
         '------    ------\n'
         '  3333      5555'))

assert (arithmetic_arranger(["2222 - 1111", "3333 - 1111"], True) ==
        ('  2222      3333\n'
         '- 1111    - 1111\n'
         '------    ------\n'
         '  1111      2222'))

assert (arithmetic_arranger(["2222 - 1", "3333 - 1"], True) ==
        ('  2222      3333\n'
         '-    1    -    1\n'
         '------    ------\n'
         '  2221      3332'))

assert (arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"]) ==
        ('  32         1      9999      523\n'
         '+  8    - 3801    + 9999    -  49\n'
         '----    ------    ------    -----'
         ))
assert (arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True) ==
        ('  32         1      9999      523\n'
         '+  8    - 3801    + 9999    -  49\n'
         '----    ------    ------    -----\n'
         '  40     -3800     19998      474'
         ))
