class Parent:
    def drinking():
        print('drinking water')

class Child(Parent):
    def drinking():
        print('drinking milk')

    def playing():
        print('playing with toys')


c=Child
c.drinking
c.playing()
