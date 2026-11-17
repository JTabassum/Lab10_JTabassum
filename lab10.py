# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens):
    # Outline (write your plan here first):
    # read through the tokens and check for /*-+. 
    # apply the opperators to the numbers previously scene
    nums = []
    for token in tokens:
        if token in "+-*/":
            b = nums.pop()
            a = nums.pop()
            
            if token == "+":
                nums.append(a + b)
            elif token == "-":
                nums.append(a - b)
            elif token == "*":
                nums.append(a * b)
            elif token == "/":
                nums.append(int(a / b))
        else:
            nums.append(int(token))
    return nums[0]
    
    

def decode_string(s):
    # Outline:
    # Read through the string one character at a time.
    # Use a stack for numbers and a stack for text before each "[".
    # When "]" is reached, repeat the text inside the brackets.
    # TODO: decode a string written with the rule k[encoded], meaning `encoded` repeated
    #   k times. The brackets can be nested.
    #   Example: "3[a2[c]]"  ->  "accaccacc"

    count_stack = []
    text_stack = []
    current_text = ""
    current_count = 0

    for character in s:
        if character.isdigit():
            current_count = current_count * 10 + int(character)
        elif character == "[":
            count_stack.append(current_count)
            text_stack.append(current_text)
            current_count = 0
            current_text = ""
        elif character == "]":
            repeat_count = count_stack.pop()
            previous_text = text_stack.pop()
            current_text = previous_text + current_text * repeat_count
        else:
            current_text += character

    return current_text


def daily_temperatures(temps):
    # Outline:
    # Use a stack of indices that are waiting for a warmer temperature.
    # Resolve them whenever a warmer temperature is found.
    # TODO: for each day, return how many days you'd wait for a WARMER temperature.
    #   Put 0 if no warmer day ever comes.
    #   Example: [73,74,75,71,69,72,76,73]  ->  [1,1,4,2,1,1,0,0]

    result = [0] * len(temps)
    unresolved_stack = []

    for index in range(len(temps)):
        while unresolved_stack and temps[index] > temps[unresolved_stack[-1]]:
            previous_index = unresolved_stack.pop()
            result[previous_index] = index - previous_index

        unresolved_stack.append(index)

    return result


def num_islands(grid):   # Part 4 - stretch (optional)
    # Outline:
    #   ...
    # TODO: `grid` is a list of equal-length strings of "1" (land) and "0" (water).
    #   Count the islands - groups of "1"s connected up/down/left/right (not diagonally).
    #   Example: ["11000","11000","00100","00011"]  ->  3
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    # print(eval_rpn(["2", "1", "+", "3", "*"]))   # 9
    pass


if __name__ == "__main__":
    main()
