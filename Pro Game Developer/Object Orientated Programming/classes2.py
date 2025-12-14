class Laptop:
    colors=5
    on_button=1
    camera=1
    stickers=2
    numbers=20

    def schoolwork(self):
        print('types of homework')

    def games(self):
        print('there are many games on the internet')

dell=Laptop()
hp=Laptop()
lenovo=Laptop()
apple=Laptop()
samsung=Laptop()

print(dell.on_button)
print(samsung.stickers)
print(hp.colors)
print(apple.numbers)
print(lenovo.camera)

dell.games()
apple.schoolwork()