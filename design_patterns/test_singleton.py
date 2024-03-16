class Cat:
    instance = None

    def __init__(self):
        if Cat.instance:
            raise Exception("Cat is singleton")
        else:
            Cat.instance = self

    @staticmethod
    def get_instance():
        if not Cat.instance:
            Cat.instance = Cat()
        return Cat.instance


# cat = Cat.get_instance()
#
cat2 = Cat()
cat1 = Cat.get_instance()
# print(cat)
# print(cat1)
