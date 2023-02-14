# Tweet Sentiment Analysis

## Goal of the Analysis

The point of this analysis was to classify tweets based on the writer's sentiment. The tweets were classified on the 13 different sentiments listed below, using Bag-of-Words:

+ neutral
+ worry
+ happiness
+ sadness
+ love
+ surprise
+ fun
+ relief
+ hate
+ empty
+ enthusiasm
+ boredom
+ anger

## Models Tested

The models tested were:

+ SVM
+ KNN
+ Decision Trees
+ Random Forest
+ AdaBoost
+ Naive Bayes

## Requirements

The file 'requirements.txt' contains a full list of the requirements to run the jupyter notebook that contains most of the code, and the file 'demo.py' that contains the demonstration code.

In summary, the entire project was created in Python 3.10, and the libraries used were Pandas, NumPy, Sklearn and Matplotlib among others.

## How to run the models

The models and the preparation of the data are contained in the 'final-sentiment-analysis.ipynb' notebook located in the 'src' folder. This notebook contains the code for the hyperparameter tuning and the training of each model.

## How to test your own Tweets

The code 'demo.py' contains a code that lets the user test a tweet of his choice and get a sentiment classification. The current iteration reads the model from the folder 'models' and gives a prediction based on that. At this point, the model used is a knn classifier.

'demo.py' reads from the file 'tweet.txt' so the tweet has to be entered as a string in that file.

The code runs from the command line. When in the same folder as the 'demo.py' file, run the command 'python demo.py' and the code will return the given tweet and the prediction for the sentiment.
