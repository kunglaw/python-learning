from Hero import Hero  # cara import


hero1 = Hero("Mirana", 1000, 400, 340, 230)
hero2 = Hero("Karina", 4000, 700, 440, 300)

# print(hero1.__dict__)
# print(hero2.__dict__)

# print(Hero.__dict__)
# print(Hero.jumlahHero)

hero1.introduce()
hero2.introduce()

hero1.attacking(hero2)
hero2.attacking(hero1)
hero1.attacking(hero2)
hero2.attacking(hero1)

print(hero1.__dict__)
print(hero2.__dict__)

print(Hero.getPrivateJumlah())
print(hero1.getPrivateJumlah())
print(hero2.getPrivateJumlah())
print("classmethod ==> ", Hero.getPrivateJumlah1())

hero1.speed = 356
print(hero1.speed)
del hero1.speed
print(hero1.speed)


# hero1 = Hero()
# hero2 = Hero()

# hero1.name = "Fisrt Sniper"
# hero1.health = 100

# hero2.name = "Sven"
# hero2.health = 200

# print(hero1)
# print(hero1.__dict__)
# print(hero1.name)
