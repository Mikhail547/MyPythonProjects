s = input()
if (
    (s[0] == "@")
    and (5 <= len(s) <= 15)
    and (s[1:].isalnum()) == 1
    and s.islower() == 1
):
    print("Correct")
elif (
    (s[0] == "@")
    and (5 <= len(s) <= 15)
    and (s[1:].isalpha()) == 1
    and s.islower() == 1
):
    print("Correct")
elif ((s[0] == "@")
    and (5 <= len(s) <= 15)
    and s[1:].isdigit()):
    print('Correct')
else:
    print("Incorrect")
