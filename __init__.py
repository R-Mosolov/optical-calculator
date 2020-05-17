from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt

from lib.models.RefractionLightClass import RefractionLightClass

app = Flask(__name__,
            static_folder='/Users/r.v.mosolov/Desktop/webstorm-projects/projects/small-projects/optical-calculator/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    # Integrating Python code with HTML
    angle = float(request.form['angle'])
    medium_one = request.form['medium-one']
    medium_two = request.form['medium-two']
    media = request.form['media']
    refraction = RefractionLightClass()

    # MAIN CALCULATOR

    # 1. Building refraction schema
    s = pd.Series([1, 2, 3])
    figure, ax = plt.subplots()
    s.plot.bar()
    figure.savefig('./static/refraction_plot.png')

    # 2. Calculating refraction angle
    refraction_angle = refraction.get_angle_refraction(angle, medium_one, medium_two)

    # 3. Getting refractive index
    refractive_index = refraction.get_refractive_index(media)

    # Rendering result that a user inserted
    return render_template(
        # Defining a page to render result
        'result.html',

        # Rendering a refraction angle
        angle=angle,
        medium_one=medium_one,
        medium_two=medium_two,
        refraction_angle=refraction_angle,

        # Rendering a refractive index
        media=media,
        refractive_index=refractive_index
    )


if __name__ == '__main__':
    app.run(debug=True)
