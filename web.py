from flask import Flask, render_template, redirect, request
import core
app = Flask(__name__)

game = core.Game()


@app.route('/')
def main_menu():
    return render_template('/home/basecamp/RisingWarriors/main_menu.html')


@app.route('/index')
def index():
    return render_template('/home/basecamp/RisingWarriors/index.html')


@app.route('/character_menu')
def character_menu():
    return render_template('/home/basecamp/RisingWarriors/character_menu.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()