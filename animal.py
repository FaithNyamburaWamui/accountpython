class Animal:
    def move(self):
        pass
    def make_sound(self):
        pass

    class Bird:
        def move(self):
            print("Flying")

        def make_sound(self):
            print("Chirp")

    class Cat:
        def move(self):
            print("Runninng")

        def make_sound(self):
            print("meow")

    class Fish:
        def move(self):
            print("Swimming")
        def make_sound(self):
            print("Bop")