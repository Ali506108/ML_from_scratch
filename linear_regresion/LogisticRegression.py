import numpy as np

class LogisticRegression:
    def __init__(self , learning_rate = 0.1 , num_iters = 2000):
        self.learning_rate = learning_rate
        self.num_iters = num_iters
        self.weights = []
        self.bias = 0

    def initialize_weights(self , dim):
        w = np.zeros((dim,1))
        b = 0

        return w ,b

    def sigmoid(self,z):
        s = 1/(1+np.exp(-z))
        return s

    def hypothesis(self , w ,x,b):
        """
        H = w^T * x + b
        :param w: weight vector
        :param x: the input vector
        :param b: the bias vector
        :return:
        """
        H = self.sigmoid(np.dot(w.T,x)+b)
        return H

    def cost_function(self ,H , y,m):
        """
        This function calculates the cost of hypothesis

        :param H: The hypothesis vector
        :param y: The output
        :param m: Number of training examples
        :return:
        """

        cost = -np.sum(y*np.log(H) + (1-y)*np.log(1-H))
        cost = np.squeeze(cost)
        return cost


    def call_gradient(self, w,H,X,Y):
        """
        Calculate gradient of the given model in learning space
        """

        m = H.shape[1]
        dw = np.dot(X,(H-Y).T)/m
        db = np.sum(H-Y)/m
        grads = {
            "dj_dw":dw,
            "dj_db":db
        }
        return grads


    def gradient_position(self , w,b,X,Y):

        m = X.shape[1]
        H = self.hypothesis(w,X,b)
        cost = self.cost_function(H,Y,m)
        grads = self.call_gradient(w,H,X,Y)
        return grads,cost


    def gradient_descent(self , w,b,x,y,print_cost=False):

        costs = []

        for i in range(self.num_iters):
            grads , cost = self.gradient_position(w,b,x,y)

            dw = grads["dj_dw"]
            db = grads["dj_db"]


            w = w-(self.learning_rate * dw)
            b = b-(self.learning_rate * db)

            if i % 100 == 0 :
                costs.append(cost)

            if print_cost and i % 100 == 0 :
                print(f"Cost after iteration {i}: {cost}")

        params = {
            "w": w,
            "b": b
        }

        return params , grads, costs


    def predict(self, X):
        X = np.array(X)
        w = self.weights.reshape(X.shape[0],1)
        b = self.bias


        H = self.hypothesis(w,X,b)
        Y_pred = (H>=0.5).astype(int)

        return Y_pred

    def train_model(self, X_train , y_train , X_test , y_test , print_cost = False):
        dim = X_train.shape[0]
        w,b = self.initialize_weights(dim)

        param , grads,cost = self.gradient_descent(w,b,X_train,y_train,print_cost)
        self.weights = param["w"]
        self.bias = param["b"]

        Y_pred_test = self.predict(X_test)
        Y_pred_train = self.predict(X_train)

        # Print train/test Errors
        train_score = 100 - np.mean(np.abs(Y_pred_train - y_train)) *100
        test_score = 100 - np.mean(np.abs(Y_pred_test - y_test)) *100

        d = {
        "cost": cost,
        "Y_prediction_test": Y_pred_test,
        "Y_prediction_train": Y_pred_train,
        "w": self,
        "b": self.b,
        "learning_rate": self.learning_rate,
        "num_iterations": self.num_iterations,
        "train accuracy": train_score,
        "test accuracy": test_score
        }

        return d

if __name__ == "__main__":

    X_train = np.array([[5, 6, 1, 3, 7, 4, 10, 1, 2, 0, 5, 3, 1, 4],
                        [1, 2, 0, 2, 3, 3, 9, 4, 4, 3, 6, 5, 3, 7]])

    Y_train = np.array([[0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]])

    X_test = np.array([[2, 3, 3, 3, 2, 4],
                       [1, 1, 0, 7, 6, 5]])

    Y_test = np.array([[0, 0, 0, 1, 1, 1]])

    clf = LogisticRegression(learning_rate=0.1, num_iters=2000)

    metrics = clf.train_model(X_train, Y_train, X_test, Y_test, print_cost=True)

    print(f"\nTrain Accuracy: {metrics['train accuracy']:.2f}%")
    print(f"Test Accuracy:  {metrics['test accuracy']:.2f}%")