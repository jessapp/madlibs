from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

AVAILABLE = ["madlibs.html", "madlibs1.html"]


@app.route('/')
def start_here():
    """Homepage."""

    return render_template("index.html")


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    name = request.args.get("name")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           name=name,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """Initiate game."""

    choice = request.args.get("choice")

    if choice == "yes":
        return render_template('game.html')

    else:
        return render_template("goodbye.html")


@app.route('/madlibs', methods=["POST"])
def play_madlibs():
    """Play game."""

    color = []

    color = request.form.getlist("color")

    if len(color) == 1:
        color_string = str(color[0])

    elif len(color) == 2:
        color_string = " and ".join(color)
    elif len(color) > 2:
        color_string = ", ".join(color[:-1])
        color_string = color_string + ", and " + color[-1]

    person = request.form.get("person")
    adjective = request.form.get("adjective")
    noun = request.form.get("noun")

    return render_template(choice(AVAILABLE),
                           person=person,
                           color=color_string,
                           adjective=adjective,
                           noun=noun)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
