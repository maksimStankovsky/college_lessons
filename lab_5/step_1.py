#a = input("Введіть слово в нижньому реєстрі: ")
#assert a.islower(), "Потрібно ввести слово в нижньому реєстрі"
#print(f"слово: {a}")

#class Figure:
    #def __init__(self, type, length) -> None:
        #assert length > 0, "Довжина має бути більшою за 0!"
        #assert type in ["квадрат", "прямокутник", "трикутник"], "Дозволені фігури: квадрат, прямокутник, трикутник"
        #self.type = type
        #self.length = length

#a = Figure("трапеція", 12)
#b = Figure("квадрат", 0)
#v = Figure("квадрат", 1)
#a = Figure("прямокутник", 1)
#b = Figure("трикутник", 1)

#print(v)
#print(a)
#print(b)

#class Name:
    #def __init__(self, name, hobbie) -> None:
        #if name not in ["Максим", "Руслан"]:
            #raise ValueError("Дозволені імена: Максим, Руслан")
        #self.name = name
        
        #if hobbie not in ["Музика", "Ігри"]:
            #raise ValueError("Дозволені хобі: Музика, Ігри")
        #self.name = name

#a = Name("Максим", 'Ігри1')