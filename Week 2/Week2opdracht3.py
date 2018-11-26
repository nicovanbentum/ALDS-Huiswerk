from Week2opdracht2 import *

def syntaxCorrect(string):
    chars_to_save = ['<', '(', '[']
    chars_cancel_out = ['>', ')', ']']
    last_pushed_char = ''

    char_stack = mystack()
    for char in string:
        if char in chars_to_save:
            char_stack.push(char)

        elif char in chars_cancel_out:
            last_pushed_char = char_stack.pop()

            if last_pushed_char == '<' and char != '>':
                return False
            elif last_pushed_char == '(' and char != ')':
                return False
            elif last_pushed_char == '[' and char != ']':
                return False
            else:
                continue
                
    return True

testchars1 = "((<>))" #should return true
print(testchars1 + " correct: " + str(syntaxCorrect(testchars1)))

testchars2 = "([)]" #should return false
print(testchars2 + " correct: " + str(syntaxCorrect(testchars2)))

testchars3 = "[<(())>]" # should return true
print(testchars3 + " correct: " + str(syntaxCorrect(testchars3)))

testchars4 = "(<>)[[<>]]" #should return true
print(testchars4 + " correct: " + str(syntaxCorrect(testchars4)))

testchars5 = "(<<[)<]])" #should return false
print(testchars5 + " correct: " + str(syntaxCorrect(testchars5)))





        