fichero = open('coding_qual_input.txt')
print(fichero.read())

sentence = {}
with open('coding_qual_input.txt', "r") as data:
    for line in data:
        number,word = line.strip().split(" ", maxsplit=1)
        sentence[number]=word
        
print(sentence)
print(sentence['234'])