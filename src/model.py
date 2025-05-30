from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

def train_model(X_train, y_train):
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    metrics = {
        "Mean squared error": mean_squared_error(y_test, y_pred),
        "R2 score": r2_score(y_test, y_pred)
    }
    return metrics