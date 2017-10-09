from collections import namedtuple


class Game():
    '''Current state of the game.'''

    def set_up(self, Warrior_1, Warrior_2, turn):
        self.Warrior_1 = Warrior_1
        self.Warrior_2 = Warrior_2
        self.turn = turn


class Character(namedtuple('Character', 'name type age img_path description')):
    @staticmethod
    def get(i):
        return None if i >= len(_Characters) else _Characters[i]

    @staticmethod
    def all():
        return _Characters


_Characters = [
    Character(
        name='Shigeru Matsuo',
        type='Gunman',
        age=32,
        img_path=
        '/home/basecamp/RisingWarriors/static/pictures/CroppedGunman.png',
        description=
        ('Shigeru Matsuo lived a quiet, calm life, residing in a large, traditional home, beside a rice farm his parents worked at throughout his childhood '
         'until his father\'s murder in 1560. An armor-clad Ronin had slit his throat in broad daylight for speaking against him in the fields,'
         'in front of Shigeru and his mother. Once Shigeru had calmed his mother and gotten over the initial shock, he has taken a similar Bushido '
         'to his uncle Tohiro, an honorable Samurai. Instead of wakizashi(short swords) and tantos(daggers), '
         'he would use his Matchlock gun and his quick wit. He\'s trained for four years, becoming an excellent shot before searching '
         'for his Father\'s murderer. As we find him now, he is still searching and sending money to his mother that '
         'he earns on the path to avenge his father.')),
    Character(
        name='Yoshio No Kudo',
        type='Sōhei',
        age=47,
        img_path='/home/basecamp/RisingWarriors/static/pictures/Ninja.png',
        description=
        ('As a child, Yoshio often visited 鏡の池(Mirror Pond), his late mother\'s favorite sanctuary for finding peace. His mother once told him '
         'that if he wanted to truly change the world, and become a man, he would look into the pond and say, "I want achieve peace. Help me." '
         'At such a young age, this frightened Yoshio. But he promised his mother that he would follow the path to peace and righteousness. And that '
         'could only begin with facing his fear, and looking to his future. '
         )),
    Character(
        name='Chiasa Watani',
        type='Samurai',
        age=44,
        img_path='',
        description=('')),
    Character(
        name='Hironobu Takahashi',
        type='Artisan',
        age=22,
        img_path='',
        description=(''
                     '')),
    Character(
        name='Takao Hara',
        type='Mechanist',
        age='31',
        img_path='',
        description=(''
                     '')),
    Character(
        name='Miyuki Azami',
        type='Maiko',
        age='__',
        img_path='',
        description=(''
                     '')),
    Character(
        name='Ayame Chiyoko',
        type='Assassin',
        age='__',
        img_path='',
        description=(''
                     '')),
    Character(
        name='Suki Kaibo',
        type='Onmyōji',
        age='__',
        img_path='',
        description=(''
                     '')),
    Character(
        name='Juuzou Kaibo',
        type='Tennô',
        age='__',
        img_path='',
        description=(''
                     '')),
    Character(
        name='Naze Kiyoshi',
        type='Ninja',
        age='__',
        img_path='',
        description=(''
                     ''))
]