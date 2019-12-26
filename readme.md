## KNN Classification App on Iris Dataset

App Url : https://knn-iris-classification.herokuapp.com/

**Iris Dataset**
The Iris flower data set or Fisher's Iris data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis.  
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). Four features were measured from each sample: the length and the width of the sepals and petals, in centimeters. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other.

**Attribute Information:**

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
5. class:
   -- Iris Setosa
   -- Iris Versicolour
   -- Iris Virginica

### About the Application

This application uses a pretrained model on the iris flower dataset to make the class prediction.The model is stored in the form of pickle file which is loaded using python pickle library.
The application has a simple user inerface where one needs to enter the sepal length,sepal width,petal length and petal width in centimeters.On clicking the predic class button the application predicts the output class and shows on the page.

**Some of the python libraries used are**

- Scikit-learn
- flask
- numpy
- pickle
