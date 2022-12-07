from typing import List
from enum import Enum


class Direction(Enum):
    LEFT = 0  # Sun的value被设定为0
    RIGHT = 1
    BOTH = 2


def fill_char_by_width(sentence: str, width: int, character: str, direction: Direction) -> str:
    length = len(sentence)
    count = width - length

    result = ""
    if direction == Direction.LEFT:
        if count > 0:
            for i in range(0, count):
                result += character
        result += sentence
    elif direction == Direction.RIGHT:
        result += sentence
        if count > 0:
            for i in range(0, count):
                result += character
    else:
        left_count = int(count / 2);
        right_count = count - left_count;
        if left_count > 0:
            for i in range(0, left_count):
                result += character

        result += sentence

        if right_count > 0:
            for i in range(0, right_count):
                result += character

    return result


class Category:
    name: str;
    ledger: List[dict];
    deposit: 0
    balance: 0
    spend: 0

    def __init__(self, name):
        self.ledger = []
        self.name = name
        self.balance = 0
        self.spend = 0

    def deposit(self, amount, desc=""):
        self.ledger.append({"amount": amount, "description": desc})
        self.deposit = amount;
        self.balance += amount;

    def withdraw(self, amount, desc="") -> bool:

        balance = self.balance - amount;
        if balance > 0:
            self.ledger.append({"amount": -amount, "description": desc})
            self.spend += amount
            self.balance = balance
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount, other) -> bool:
        if self.balance > amount:
            other.deposit(amount, "Transfer from " + self.name)
            self.withdraw(amount, "Transfer to " + other.name)
            return True
        else:
            return False

    def check_funds(self, amount) -> bool:
        if self.balance >= amount:
            return True;
        else:
            return False;

    def __str__(self) -> str:
        result = ""
        result = result + fill_char_by_width(self.name, 30, "*", Direction.BOTH) + "\n"
        for i, val in enumerate(self.ledger):
            desc = val['description']
            amount_str = format(val['amount'], '.2f')
            if len(desc) > 23:
                desc = desc[0:23]
            result = result + fill_char_by_width(desc, 23, " ", Direction.RIGHT)
            result = result + fill_char_by_width(amount_str, 7, " ", Direction.LEFT)
            result += "\n"
        result += ("Total: " + str(self.balance))
        return result


def create_spend_chart(categories):
    res = ""
    res += "Percentage spent by category\n"
    y_array = [];
    percent_array = [];
    total_spend = 0;
    for category in categories:
        total_spend += category.spend;

    for i in range(10, -1, -1):
        s = fill_char_by_width(str(i * 10) + "|", 4, " ", Direction.LEFT)
        y_array.append(s)

    for category in categories:
        percent = int(category.spend / total_spend * 100)
        real_percent = (int)(percent / 10)
        temp_list = []
        for i in range(10, -1, -1):
            if i <= real_percent:
                temp_list.append("o")
            else:
                temp_list.append(" ")
        percent_array.append(temp_list)

    for i in range(0, 11):
        res += str(y_array[i])
        res += " "
        for array in percent_array:
            res += array[i]
            res += "  "
        res += "\n"

    horizontal_lines_width = len(categories) * 3 + 1
    total_width = horizontal_lines_width + 4
    divider_str = ""
    for i in range(1, total_width - horizontal_lines_width + 1):
        divider_str += " "
    for i in range(1, horizontal_lines_width + 1):
        divider_str += "-"

    res = res + divider_str + "\n"

    names_array = [];
    max_name_len = 0
    for x in categories:
        if len(x.name) > max_name_len:
            max_name_len = len(x.name)

    for x in categories:
        full_name = fill_char_by_width(x.name, max_name_len, " ", Direction.RIGHT)
        names_array.append(full_name)

    for i in range(0, max_name_len):
        is_last = i == max_name_len - 1
        res += "     "
        for x in names_array:
            res = res + x[i] + "  "
        if not is_last:
            res += "\n"
    return res
