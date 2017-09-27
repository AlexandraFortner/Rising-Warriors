from collections import namedtuple


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
        type='Gunman/Sniper',
        age=32,
        img_path=
        '/home/basecamp/RisingWarriors/static/pictures/CroppedGunman.png',
        description=
        ('Shigeru Matsuo lived a quiet, wealthy life, residing in a large, traditional home, beside 鏡の池(Mirror Pond) '
         ''))
]
# Book(
# id=1,
# title='Get Programming with F#',
# authors=['Isaac Abraham'],
# price=35.99,
# img_path='/static/images/get_programming_with_fsharp.png',
# description=
# ('Get Programming with F#: A guide for .NET Developers shows you how to upgrade your .NET development skills '
#  'by adding a touch of functional programming in F#. In just 43 bite-size chunks, you\'ll learn to use F# to '
#  'tackle the most common .NET programming tasks. You\'ll start with the basics of F# and functional programming, '
#  'building on your existing skills in the .NET framework. Examples use the familiar Visual Studio environment, '
#  'so you\'ll be instantly comfortable. Packed with enlightening examples, real-world use cases, and plenty of '
#  'easy-to-digest code, this easy-to-follow tutorial will make you wonder why you didn\'t pick up F# years ago!'
#  ))