import random

def fire_at(self, enemy):
        if self.ammo >=1:
            self.ammo -=1
            print(self.name, "fires on", enemy.name)
            enemy.hit()
        else:
            print(self.name, "has no shells!")

    def hit(self):
        self.armor -=20
        print(self.name, "is hit")
        if self.armor <=0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explodes!")

meuTanque1 = Tank("Bob")
meuTanque2 = Tank("Jack")
meuTanque3 = Tank("Wesley")
meuTanque4 = Tank("Natalia")
meuTanque5 = Tank("Xuxa")

array = [meuTanque1, meuTanque2, meuTanque3, meuTanque4, meuTanque5]

    while (len(array)!=1):
    T1 = random.randint(0,len(array)-1)
    T2 = random.randint(0,len(array)-1)
    while T2 == T1:
        T2 = random.randint(0,len(array)-1)
    array[T1].fire_at(array[T2])
    if(array[T2].alive!=True):
        array.remove(array[T2])
print ("Parabéns! O vencedor foi ",array[0].name)
