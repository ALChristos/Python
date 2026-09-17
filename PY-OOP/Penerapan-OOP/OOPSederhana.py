class Hero:
    def __init__(self, Nama, Health, Deffence, Attack):
        self.Nama = Nama
        self.Health = Health
        self.Deffence = Deffence
        self.Attack = Attack
        
    def menyerang(self, lawan):
        print(f"{self.Nama} Menyerang {lawan.Nama}")
        lawan.diserang(self)
        
    def diserang(self, lawan):
        print(f"{self.Nama} Diserang {lawan.Nama}")
        AttackImpact = lawan.Attack/(self.Deffence/2)
        print(f"DMG yang diterima {AttackImpact}")
        self.Health -= AttackImpact
        print(f"HP {self.Nama} Sekarang = {self.Health}")
        
alucard = Hero("Alucard", 100, 30, 30)
aldous = Hero("Aldous", 150, 40, 30)

aldous.menyerang(alucard)
print("\n")
alucard.menyerang(aldous)