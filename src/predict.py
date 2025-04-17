import data_loader as dl
import model as m
from sklearn.model_selection import train_test_split

def predict():
    data = dl.fetch_data()
    X = data[["Open", "High", "Low", "Volume"]]
    y = data[("Close","AAPL")]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=45, shuffle=False)
    model = m.train_model(X_train, y_train)
    print("Model evaluation results: ", m.evaluate_model(model, X_test, y_test))
    predicted_vals = model.predict(X_test.iloc[-1:])
    print(predicted_vals[0])

if __name__ == "__main__":
    predict()