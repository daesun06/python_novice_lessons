#N1

#I think that in the first one it will add 10 to 10, and then
#in the second one it will return 0.

a = abs(10) + abs(-10)
print(a)
b = abs(-10) + -10
print(b)


# N2

cypher = "этот если способ вы плохо это подходит читаете для что-то шифрования пошло важных не сообщений так"
splited_cypher = cypher.split()

for c in range(0, len(splited_cypher), 2):
    print(splited_cypher[c])

#N3

def save_file(file_to_copy: str, file_name: str):
    file_content = open(file_to_copy).read()
    file_to_paste = open(file_name, 'w')
    file_to_paste.write(file_content)
    file_to_paste.close()

save_file(file_to_copy='copy_me.txt', file_name= "copied_file.txt")