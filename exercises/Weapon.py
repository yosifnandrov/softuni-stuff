class WeaponGun:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):
        if self.bullets:
            self.bullets -= 1
            return "shooting..."
        return "no bullets left"

    def __repr__(self):
        return f"Remaining bullets: {self.bullets}"
weapon = WeaponGun(5)
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
weapon.shoot()
print(weapon)



