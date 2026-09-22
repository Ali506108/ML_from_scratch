import numpy as np

class LinearRegression:
    "Linear Regression model"
    def compute_linear_model(self , x , w , b) :
        return np.dot(x,w) +b

    def compute_cost(self , X , y , w , b):

        m = X.shape[0]
        f_wb = self.compute_linear_model(X, w, b)
        cost = (f_wb - y)**2
        total_cost = np.sum(cost) / (2*m)
        return total_cost

    def compute_gradient(self , x , y, w , b):
        m = x.shape[0]
        f_wb = self.compute_linear_model(x, w, b)
        err = f_wb - y
        dj_dw = np.dot(x.T ,err) / m
        dj_db = np.sum(err) / m
        #for i in range(m):
        #    dj_dw_i = (f_wb - y[i])*x[i]
        #    dj_db_i = (f_wb - y[i])
        #    dj_dw += dj_dw_i
        #    dj_db += dj_db_i
        #dj_dw = dj_dw/m
        #dj_db = dj_db/m

        return dj_dw , dj_db

    def gradient_descent(self , x , y , w_in ,b_in , alpha , num_iters):

        w = w_in
        b = b_in
        j_hist = []

        for i in range(num_iters):
            # 1. formula
            dj_dw , dj_db = self.compute_gradient(x , y ,w , b)

            # 2. etap
            w = w - alpha*dj_dw
            b = b - alpha*dj_db

            if i < 100_000:
                j_hist.append(self.compute_cost(x , y , w ,b))

            if i % (num_iters // 10) == 0 :
                print(f"Iteration : {i}, Cost : {j_hist[-1]:8.2f} | w: {w:8.3f}, b: {b:8.3f}")

        return w ,b , j_hist
