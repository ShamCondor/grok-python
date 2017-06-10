

class ClassA:

    age = 17

    def __init__(self):
        self.name = 'lilei'


class ClassB(ClassA):

    def get_name(self):
        # 可以访问到父类的类属性age
        print(super().age)
        # 不能访问name,因为name是父类实例的属性,和子类没什么关系
        # print(super_().name)


if __name__ == '__main__':

    class_b = ClassB()
    class_b.get_name()
