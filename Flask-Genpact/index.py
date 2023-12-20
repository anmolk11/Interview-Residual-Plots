from flask import Flask, render_template, request, redirect, url_for
import pandas as pd 

from plot import make_plot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/plot', methods=['POST'])
def plot():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        df = pd.read_csv(file)
        plot_image = make_plot(df, target = 'y')
        return render_template('plot.html', plot_image = plot_image)


if __name__ == '__main__':
    app.run(debug=True)
