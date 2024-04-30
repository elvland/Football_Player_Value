from flask import Flask, render_template, request
import numpy as np
import joblib

model = joblib.load("/home/elvland/programmering/flaskProject/predict_player/Football_Player_Value/bm.joblib")

app = Flask(__name__, template_folder='', static_folder='static', static_url_path='/static')

@app.route('/', methods = ['GET','POST'])
def home():
   return render_template("PlayerMarketValue.html")


@app.route('/showplayer')
def player_market_value():
    return render_template('showPlayerValue.html')

@app.route("/predict_again", methods = ['GET','POST'])
def predict_again():
    return render_template("PlayerMarketValue.html")

@app.route('/predict', methods=['POST','GET'])
def predict():
    # Extract input features from the request
    feature1 = str(request.form['name'])
    feature2 = float(request.form['age'])
    feature3 = float(request.form['vision'])
    feature4 = float(request.form['dribbling'])
    feature5 = float(request.form['passing'])
    feature6 = float(request.form['shooting'])
    feature7 = float(request.form['reputation'])
    feature8 = float(request.form['mentality'])
    feature9 = float(request.form['shotPower'])
    feature10 = float(request.form['totalPower'])
    feature11 = float(request.form['ballcontroll'])
    feature12 = float(request.form['finishing'])


    features_list = [feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10,
                     feature11, feature12]

    features_array = np.array([features_list])

    # Make predictions using the loaded model
    prediction = model.predict(features_array)


    # Return the rendered template with the prediction result
    return render_template("showPlayerValue.html", prediction=round(np.exp(prediction[0]),2),name = feature1)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
