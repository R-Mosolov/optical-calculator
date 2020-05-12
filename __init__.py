from flask import Flask, render_template, request

app = Flask(__name__, static_folder='/Users/R.V.Mosolov/Desktop/lib_optics-master/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():

    # Integrating Python code with HTML
    dist_subject = request.form['dist-subject']
    focal_length = request.form['focal-length']
    height_subject = request.form['height-subject']

    # Rendering result that a user inserted
    return render_template(
        'result.html',
        dist_subject_result=dist_subject,
        focal_length_result=focal_length,
        height_subject_result=height_subject
    )


if __name__ == '__main__':
    app.run(debug=True)