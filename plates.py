def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if max_length(s) and start_with_two_le(s) and start(s) and punct(s) and zero_start(s):
        return True
    else:
        return False

# Check if string start with at least two letters
def start_with_two_le(s):
    if s[0:2].isalpha():
        return True
    else:
        return False

# Check the length of string
def max_length(s):
    if len(s) >= 2 and len(s) < 7:
        return True
    else:
        return False

# Numbers cannot be used in the middle of a plate; they must come at the end.
def start(s):
    if not any(i.isdigit() for i in s): # if string contains no letter -> return True
        return True
    else:
        num="" # create empty string
        for i in range(len(s)):
            num+=s[i]
        if num[-1].isalpha() or num[-2].isalpha(): #if last or second to last character is a letter -> False
            return False
        else:
            return True

# No periods, spaces, or punctuation marks ckecker
def punct(s):
    if any(not c.isalnum() for c in s):
        return False
    else:
        return True

# The first number used cannot be a ‘0’.”
def zero_start(s):
    z = ""
    for i in range(0,len(s)):
        if s[i].isnumeric():
            z += s[i]
    if z=="":
        return True
    elif z[0] == "0":
        return False
    else:
        return True

main()