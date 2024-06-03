APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name='Fido', breed='Mastiff'):
        self.name = name
        self.breed = breed

    @property
    def name (self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length."""
        if isinstance(name, str) and 1<=len(name)<=25:
            self._name = name
        else:
            raise ValueError("Name must be string betweeen 1 an 25 characters.")

    @property
    def breed(self):
        """The breed property"""
        return self._breed

    
    @breed.setter
    def breed(self, breed):
        """Breed must be in list of apperoved breeds."""
        if breed in APPROVED_BREEDS:
            self._breed = breed
        else:
            raise ValueError("Breed must be in list of approved breeds.")


butch = Dog("Butch")
print(butch.name)
print(butch.breed)

matata = Dog("Matata", "Beagle")
print(matata.name)
print(matata.breed)

bosco = Dog()
print(bosco.name)

bosco.breed = "Pug"
print(bosco.breed)

# bosco.name = ""

# bosco.breed = "Alsatian"
  