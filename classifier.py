import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: Load the labeled dataset
df = pd.read_csv('news_data.csv')

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Content'], df['Classification'], test_size=0.2, random_state=42)

# Step 3: Feature extraction (Convert text data into numerical features)
vectorizer = CountVectorizer(stop_words='english')
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Step 4: Train the Multinomial Naive Bayes classifier
model = MultinomialNB()
model.fit(X_train_vectorized, y_train)

# Step 5: Evaluate the model on the test set
predictions = model.predict(X_test_vectorized)

accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

print('\nClassification Report:')
print(classification_report(y_test, predictions))

# Step 6: Predictions for new articles
new_articles = ["This is a breaking news article.", "A new study on climate change has been published."]

# Vectorize the new articles
new_articles_vectorized = vectorizer.transform(new_articles)

# Predict the categories
predictions_new_articles = model.predict(new_articles_vectorized)

print('\nPredictions for New Articles:')
for article, prediction in zip(new_articles, predictions_new_articles):
    print(f"Article: {article}")
    print(f"Predicted Classification: {prediction}")
    print("-" * 50)
