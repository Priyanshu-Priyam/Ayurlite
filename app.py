from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import pickle
from model import extract_features

""""
from model import extract_features
from model import DecisionTreeClassifier
from model import X_test
from model import X_train

"""




app = Flask(__name__)
classifier = pickle.load(open('model.pkl', 'rb'))

app.config["UPLOAD_FOLDER"] = "static/"

@app.route('/')
def upload_file():
    return render_template('index.html')


@app.route('/display', methods = ['GET', 'POST'])



def save_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)
        
        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"r")
        #content = file.read()

        import numpy as np
        #fn=input("Enter the name of the file")ß
        x_user = extract_features(filename)
    
        prediction = classifier.predict(x_user)

        content= prediction 


    return render_template('content.html', content=content) 



"""


 
"""
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug = True)

   