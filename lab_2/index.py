#a = "I`m a iron man :)"
#b = 3 # числова Змінна
#c = ["a", 1, 1.25, "Maks"] # List
#d = {"a": "КНП", "b": 1} # Dict
#e = ("a", ) # Tuple
#f = {"ss", } # Set

#print(a,b,c,d,e,f)
#print(abs(-12.5), f"є рівним {abs(12.5)}")

##letters = ["КНП-120", "КНП-220", "КНП-330"]
##for i in range(len(letters)):
    ##print(f"На позиції {i} знаходиться {letters[i]}")

#A = False
#print("A = false" if False == A else "A = true")
#A = 0
#try:
    #print("Що буде якщо", 10/A, "?")
#except Exception as e:
    #print(e)
#finally:
    #print("А вот воно що!")

#with open("README.md", "r") as f:
    #for line in f:
        #print(line)

this_is_lambda = lambda first, last: f'Цей код написав: {first} {last}'
print("Це просто функція:", this_is_lambda)
print("Це її виклик:", this_is_lambda('Максим', 'Бізнесовский'))