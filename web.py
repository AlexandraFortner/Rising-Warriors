from flask import Flask, render_template, redirect, request
import core
app = Flask(__name__)

game = core.Game()


@app.route('/menu')
def main_menu():
    return render_template('index.html')


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()