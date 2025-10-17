
from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal('Sharo', 'dog', 'woof')

    def test_init(self):
        self.assertEqual('Sharo', self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('woof', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_make_sound_mammal_returns_correct_sound(self):

        new_return = self.mammal.make_sound()

        self.assertEqual('Sharo makes woof', new_return)

    def test_get_kingdom_returns_correct_kingdom(self):
        new_return = self.mammal.get_kingdom()
        self.assertEqual('animals', new_return)

    def test_info_returns_correct_info(self):
        new_return = self.mammal.info()
        self.assertEqual('Sharo is of type dog', new_return)


if __name__ == '__main__':
    main()
