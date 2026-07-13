max_world = ''
max_n = 0
world = 0
for i in range(4):
    s = input()
    for j in range (len(s)):
        world += ord(s[j])
    if world > max_n:
        max_n = world
        max_world = s
    world = 0
print(max_world)