s = input()
bee = 0
for i in range(len(s)):
    bee += ord(s[i]) *3
print (f"Текст сообщения: '{s}'\nСтоимость сообщения: {bee}🐝")