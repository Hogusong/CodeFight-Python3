# A cryptarithm is a mathematical puzzle for which the goal is to find the correspondence
# between letters and digits, such that the given arithmetic equation consisting of letters
# holds true when the letters are converted to digits.
#
# You have an array of strings crypt, the cryptarithm, and an an array containing the mapping
# of letters and digits, solution. The array crypt will contain three non-empty strings that follow
# the structure: [word1, word2, word3], which should be interpreted as the word1 + word2 = word3 cryptarithm.
#
# If crypt, when it is decoded by replacing all of the letters in the cryptarithm with digits using
# the mapping in solution, becomes a valid arithmetic equation containing no numbers with leading zeroes,
# the answer is true. If it does not become a valid arithmetic solution, the answer is false.
#
# Example
#
# For crypt = ["SEND", "MORE", "MONEY"] and
#
# solution = [['O', '0'],
#             ['M', '1'],
#             ['Y', '2'],
#             ['E', '5'],
#             ['N', '6'],
#             ['D', '7'],
#             ['R', '8'],
#             ['S', '9']]
# the output should be
# isCryptSolution(crypt, solution) = true.
#
# When you decrypt "SEND", "MORE", and "MONEY" using the mapping given in crypt, you get 9567 + 1085 = 10652
# which is correct and a valid arithmetic equation.
#
# For crypt = ["TEN", "TWO", "ONE"] and
#
# solution = [['O', '1'],
#             ['T', '0'],
#             ['W', '9'],
#             ['E', '5'],
#             ['N', '4']]
# the output should be
# isCryptSolution(crypt, solution) = false.
#
# Even though 054 + 091 = 145, 054 and 091 both contain leading zeroes, meaning that this is not a valid solution.
#
# Input/Output
#
# [execution time limit] 4 seconds (py3)
#
# [input] array.string crypt
#
# An array of three non-empty strings containing only uppercase English letters.
#
# Guaranteed constraints:
# crypt.length = 3,
# 1 ≤ crypt[i].length ≤ 14.
#
# [input] array.array.char solution
#
# An array consisting of pairs of characters that represent the correspondence between letters
# and numbers in the cryptarithm. The first character in the pair is an uppercase English letter,
# and the second one is a digit in the range from 0 to 9.
#
# Guaranteed constraints:
# solution[i].length = 2,
# 'A' ≤ solution[i][0] ≤ 'Z',
# '0' ≤ solution[i][1] ≤ '9',
# solution[i][0] ≠ solution[j][0], i ≠ j,
# solution[i][1] ≠ solution[j][1], i ≠ j.
#
# It is guaranteed that solution only contains entries for the letters present in crypt
# and that different letters have different values.
#
# [output] boolean
#
# Return true if the solution represents the correct solution to the cryptarithm crypt, otherwise return false.


# answer 1
def getValue(word, solution):
    value = []
    for w in word:
        for i in range(len(solution)):
            if solution[i][0] == w:
                value.append(solution[i][1])
                break
        else:
            return 1000000
    if len(value) > 1 and value[0] == '0':
        return 10000000
    return int(''.join(value))


def isCryptSolution(crypt, solution):
    value_zero = getValue(crypt[0], solution)
    value_one = getValue(crypt[1], solution)
    value_two = getValue(crypt[2], solution)
    return value_zero + value_one == value_two


# answer 2
# def getValue(w, solution):
#     for i in range(len(solution)):
#         if solution[i][0] == w:
#             return solution[i][1]
#     return '0'
#
#
# def isCryptSolution(crypt, solution):
#     code = []
#     for i in range(len(crypt[0])):
#         code.append(getValue(crypt[0][i], solution))
#     if len(code) > 1 and code[0] == '0':
#         return False
#     value_one = int(''.join(code))
#     code = []
#     for i in range(len(crypt[1])):
#         code.append(getValue(crypt[1][i], solution))
#     if len(code) > 1 and code[0] == '0':
#         return False
#     value_two = int(''.join(code))
#     code = []
#     for i in range(len(crypt[2])):
#         code.append(getValue(crypt[2][i], solution))
#     if len(code) > 1 and code[0] == '0':
#         return False
#     value_three = int(''.join(code))
#
#     return value_one + value_two == value_three

