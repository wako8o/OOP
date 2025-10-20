from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self):

         self.hero = Hero('Wor_God', 100, 200.5, 50.5)
         self.enemy_hero = Hero('Enemy', 90, 150.5, 40.5)

    def test_attributes_class(self):
        self.assertTrue(isinstance(self.hero.username, str))
        self.assertTrue(isinstance(self.hero.health, float))
        self.assertTrue(isinstance(self.hero.damage, float))
        self.assertTrue(isinstance(self.hero.level, int))

    def test_init(self):
        self.assertEqual('Wor_God', self.hero.username)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(200.5, self.hero.health)
        self.assertEqual(50.5, self.hero.damage)

    def test_battle_lifting_in_case_of_a_tied_result(self):
        self.hero.username = self.enemy_hero.username
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raise_on_loss_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_raise_on_enemy_health(self):
        self.enemy_hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

        self.enemy_hero.health = -1
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy_hero)
        self.assertEqual(f"You cannot fight {self.enemy_hero.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):

        result = self.hero.battle(self.enemy_hero)
        self.assertEqual(100, self.hero.level)
        self.assertEqual(-3444.5, self.hero.health)
        self.assertEqual(50.5, self.hero.damage)

        self.assertEqual(90, self.enemy_hero.level)
        self.assertEqual(-4899.5, self.enemy_hero.health)
        self.assertEqual(40.5, self.enemy_hero.damage)

        self.assertEqual('Draw', result)

    def test_battle_win(self):
        enemy = Hero('Enemy', 1, 1, 1)
        result = self.hero.battle(enemy)

        self.assertEqual(101, self.hero.level)
        self.assertEqual(55.5, self.hero.damage)
        self.assertEqual(204.5 , self.hero.health)
        self.assertEqual("You win", result)

        self.assertEqual(1, enemy.level)
        self.assertEqual(1, enemy.damage)
        self.assertEqual(-5049.0, enemy.health)

    def test_battle_lose(self):
        self.hero = Hero('Wor_God', 100, 200.5, 1)
        enemy = Hero('Enemy', 300, 300, 300)
        result = self.hero.battle(enemy)

        self.assertEqual(100, self.hero.level)
        self.assertEqual(1, self.hero.damage)
        self.assertEqual(-89799.5, self.hero.health)
        self.assertEqual("You lose", result)

        self.assertEqual(301, enemy.level)
        self.assertEqual(305, enemy.damage)
        self.assertEqual(205, enemy.health)

    def test_str_representation(self):

        result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                 f"Health: {self.hero.health}\n" \
                 f"Damage: {self.hero.damage}\n"
        self.assertEqual(result, str(self.hero))

if __name__ == '__main__':
    main()