from flask import Flask, render_template, redirect, request
import random

app = Flask(__name__)

rows = 3
cols = 9


# page 272,
def generate_random_fruits():
    fruits = [[] for row in range(rows)]

    for row in range(rows):
        for col in range(cols):
            r = random.randint(0, 8)
            if r < 2:
                fruits[row].append("apple")
            elif r < 4:
                fruits[row].append("banana")
            elif r < 6:
                fruits[row].append("orange")
            elif r < 8:
                fruits[row].append("kiwi")
            else:
                fruits[row].append("dynamite")
    return fruits


# end of page 272,
fruits = generate_random_fruits()

score = 0
game_over = False


@app.route('/')
def index():
    return render_template('index.html',
                           rows=rows, cols=cols, fruits=fruits,
                           game_over=game_over, score=score)


@app.route('/Reset')
def reset():
    global fruits
    fruits = generate_random_fruits()

    global game_over
    game_over = False
    return redirect('/')


def fire(position, start_row, step):
    col = position * (cols - 1) // 100
    row = start_row
    while row >= 0 and row < rows:
        fruit = fruits[row][col]
        if fruit in ['apple', 'banana', 'orange', 'kiwi']:
            global score
            score += 1
            fruits[row][col] = 'empty'
            break
        elif fruit == 'dynamite':
            global game_over
            game_over = True
            break
        row = row + step
    return redirect('/')


@app.route('/FireTop')
def fire_top():
    position = int(request.args['position'])
    return fire(position, 0, 1)


@app.route('/FireBottom')
def fire_bottom():
    position = int(request.args['position'])
    return fire(position, rows - 1, -1)


if __name__ == '__main__':
    app.run()
