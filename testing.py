from sklearn.externals import joblib
import numpy as np

knn_classifier = joblib.load("knn_model.pkl")

predicted_class = knn_classifier.predict(np.array([[-1,-2.6,-0.5,-0.26]]))

print(predicted_class[0])