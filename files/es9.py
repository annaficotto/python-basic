'''
Crea un file quadrati.txt e scrivi per ogni numero da 1 a 10 il suo quadrato, su righe del tipo:
1  1
2  4
3  9 
4  16
5  25
'''

file = open("files/quadrati.txt", "w", encoding="utf-8")
for i in range(1, 11):
    file.write(str(i) + " " + str(i * i) + "\n")
file.close()