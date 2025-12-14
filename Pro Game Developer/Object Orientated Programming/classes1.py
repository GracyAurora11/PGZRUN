class Dog:
    eyes=2
    legs=4
    tail=1
    ears='fluffy'
    skin='smooth'
    can_fly=False

    def bark(self):
        print('woof-woof')

    def wag_tail(self):
        print('dog is wagging its tail!')
    
golden_retriever=Dog()
husky=Dog()
pomeranian=Dog()
labrador=Dog()
poodle=Dog()

print(poodle.tail)

print(golden_retriever.legs)

print(husky.eyes)

print(pomeranian.ears)

poodle.bark()

labrador.wag_tail()