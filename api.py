from flask import Flask,render_template,request




app = Flask(__name__)




@app.route('/', methods=['GET'])
def homepage():
	return render_template("home.html")

@app.route('/predict', methods=['POST'])
def predict():
	import numpy as np
	#from sklearn.externals import joblib
	import os
	import time
	import pickle


	'''sepal_length = request.form['sepal_length']
	sepal_width = request.form['sepal_width']
	petal_length = request.form['petal_length']
	petal_width = request.form['petal_width']

	
	
	float_features = [x for x in request.form.values()]
	final_features = [np.array(float_features)]'''
    
	final_features = [np.array([12,22,13,44])]

	knn_classifier = None
	
	#knn_classifier = joblib.load(os.path.join(os.getcwd(),"knn_model.pkl"))
	with open(os.path.join(os.getcwd(),"knn_model.pkl"), 'rb') as file:
		knn_classifier = pickle.load(file)

    	
	print(type(knn_classifier))
	
	predicted_class = knn_classifier.predict(final_features)
	
	

	return render_template("result.html",predicted = str(predicted_class[0]))

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=3000,debug=True)