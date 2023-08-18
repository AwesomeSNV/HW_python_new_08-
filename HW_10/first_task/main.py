class Animal:
    def __init__(self, name, age, voice='groal'):
        self.name = name
        self.age = age
        self.voice = voice

    def make_voice(self):
        print(self.voice)


class Fish(Animal):
    def __init__(self, name, age, scales, voice):
        super().__init__(name, age, voice)
        self.scales = scales

    def swim(self):
        print("i'm swimming, oh, it's titan!")


class Dog(Animal):
    def __init__(self, name, age, breed, voice):
        super().__init__(name, age, voice)
        self.breed = breed

    def bark(self):
        print('Bark!')


class Raven(Animal):
    def __init__(self, name, age, color, voice):
        super().__init__(name, age)
        self.voice = voice
        self.color = name

    def fly_around_corpse(self):
        print('oooh, meat....')


class AnimalFabric:
    def animal_(self, animal_type, name, age, voice, color = None, breed = None):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.voice = voice
        self.color = color
        self.breed = breed

        if animal_type == "Fish":
            return Fish(name, age, color, voice)
        elif animal_type == "Dog":
            return Dog(name, age, breed, voice)
        elif animal_type == "Raven":
            return Raven(name, age, color, voice)
        else:
            raise ValueError("Animal type is not supported")


animal = AnimalFabric()
dog = animal.animal_('Dog', 'Pirat', 5, 'woof!', 'Bulldog', )
bird = animal.animal_('Raven', 'Qarasique', 6, 'bravo!', 'white')
fish = animal.animal_('Fish', 'Nemo', 2, 'bul-bul', 'silver' )
animals = [fish, dog, bird]

for i in animals:
    i.make_voice()

fish.swim()
dog.bark()
bird.fly_around_corpse()