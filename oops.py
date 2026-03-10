class Factory:
    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def __str__(self):
        return f"Factory(material={self.material}, zips={self.zips}, pockets={self.pockets})"


rebook = Factory("leather", 3, 2)
print(rebook)