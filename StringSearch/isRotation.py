import sys

def isSubstring(string_a, string_b):
    if string_b.find(string_a) == -1:
        return False
    else:
        return True


def isRotation(rotated_string, original_string):
    if len(rotated_string) == len(original_string):
        original_string = original_string + original_string
        return isSubstring(rotated_string, original_string)
    else:
        return False

original_string = "waterbottle"
rotated_string = "ottlewaterb"

if len(sys.argv) < 3:
    print("testing algorithm with: " + original_string + " and : " + rotated_string)
else:
    original_string = sys.argv[1]
    rotated_string = sys.argv[2]

print(isRotation(rotated_string, original_string))