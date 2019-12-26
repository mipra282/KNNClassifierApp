from flask import Flask,render_template,request
from sklearn.externals import joblib


app = Flask(__name__)




@app.route('/', methods=['GET'])
def homepage():
	return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
	import numpy as np


	'''sepal_length = request.form['sepal_length']
	sepal_width = request.form['sepal_width']
	petal_length = request.form['petal_length']
	petal_width = request.form['petal_width']

	
	#arr = np.array(arr).astype(np.float16())
	#[sepal_length,sepal_width,petal_length,petal_width]
	float_features = [x for x in request.form.values()]
	final_features = [np.array(float_features)]

	#if (type(sepal_length) == float  and  type(sepal_width) == float and  type(petal_length) == float and  type(petal_width) == float):
	knn_classifier = joblib.load("knn_model.pkl")

	predicted_class = knn_classifier.predict(final_features)
	print(predicted_class)'''
	predicted_class = ['Iris']

	#else:
		#predicted_class = ["Please enter float!"]

	return render_template("result.html",predicted = str(predicted_class[0]))

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=3000,debug=True)