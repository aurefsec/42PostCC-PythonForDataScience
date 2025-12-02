from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
Joffrey.p_eyes = "test"
Joffrey.p_hairs = "test"
print(Joffrey.p_eyes)
print(Joffrey.p_hairs)
print(Joffrey.__dict__)
