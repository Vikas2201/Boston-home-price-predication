from flask import Flask, render_template, request
from flask_cors import cross_origin
import pickle
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

application = Flask(__name__)
app = application
@app.route('/',methods=['GET'])
@cross_origin()
def home_page():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET'])
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            INDUS = float(request.form['INDUS'])
            NOX = float(request.form['NOX'])
            RM = float(request.form['RM'])
            PTRATIO = float(request.form['PTRATIO'])
            LSTAT = float(request.form['LSTAT'])
            filename = 'final_model.pickle'
            model = pickle.load(open(filename, 'rb'))
            prediction = model.predict([[INDUS,NOX,RM,PTRATIO,LSTAT]])
            print('prediction value is ', prediction)
            # showing the prediction results in a UI
            return render_template('results.html', prediction=round(prediction[0],3))

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)



