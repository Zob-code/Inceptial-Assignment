# this is the composition part
class Parent(object):

    def altered(self):
        print("parent Altered")

class Child(Parent):

    def altered(self):
        print("Child Altered")
        super(Child, self).altered()
        print("Child, after altered!")

dad = Parent()
son = Child()

dad.altered()
son.altered()
