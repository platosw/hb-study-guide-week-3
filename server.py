"""A simple Flask app."""

from flask import Flask, render_template, session, request, redirect
import jinja2

app = Flask(__name__)
app.secret_key = "RANDOM SECRET KEY"

@app.route('/')
def show_homepage():
    """Show homepage."""
    return render_template('homepage.html')


@app.route('/save-name')
def save_name():
    session['name'] = request.args.get('name')

    return redirect('/')


@app.route('/remove-name')
def remove_name():
    del session['name']

    return redirect('/')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    """Show form with message options."""
    return render_template('form.html')

@app.route('/results', methods=["POST"])
def show_results():
    """Show resulting message."""
    cheery = request.form.get('cheery')
    honest = request.form.get('honest')
    dreary = request.form.get('dreary')

    values = [cheery, honest, dreary]

    return render_template('results.html', values=values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
