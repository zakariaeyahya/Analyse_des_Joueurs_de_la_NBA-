import copy
import math
import numpy as np
import matplotlib.pyplot as plt
def load_house_data():
    data = np.loadtxt("houses.csv", delimiter=',', skiprows=1)
    X = data[:, :4]
    y = data[:, 4]
    return X, y
X_train, y_train = load_house_data()
X_features = ['size(sqft)', 'bedrooms', 'floors', 'age']
fig, ax = plt.subplots(1, 4, figsize=(12, 3), sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:, i], y_train)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("Price (1000's)")
plt.show()
def compute_cost(X, y, w, b):

  m = X.shape[0]
  cost = 0.0
  for i in range(m):
     f_wb_i = w*X[i]+b
     cost +=(f_wb_i - y[i])**2
  cost = (1/2*m)*cost 
  return cost

def compute_gradient(X, y, w, b):

   m, n = X.shape # (number of examples, number of features)
   dj_dw = np.zeros((n,))
   dj_db = 0.
   for i in range(m):
      err =np.dot(X[i],w)+b-y[i]
      for j in range(n):
           dj_dw[j] += err*X[i][j]
      dj_db += err
   dj_dw = dj_dw / m
   dj_db = dj_db / m
   return dj_db, dj_dw
def gradient_descent(X, y, w_in, b_in, cost_function, gradient_function,alpha, num_iters):
    m = len(X)
    hist = {}
    hist["cost"] = [];
    hist["params"] = [];
    hist["grads"] = [];
    hist["iter"] = [];
    w = copy.deepcopy(w_in) 
    b = b_in # avoid modifying global w within function
    save_interval = np.ceil(num_iters / 10000) # prevent resource
    print( f"Iteration Cost w0 w1 w2 w3 b djdw0 djdw1 djdw2 djdw3 djdb ")
    print(f"---------------------|--------|--------|--------|--------|----- ---|--------|--------|--------|--------|--------|")
    for i in range(num_iters):
    # Calculate the gradient and update the parameters
        dj_db, dj_dw = compute_gradient(X, y, w, b)
        # Update Parameters using w, b, alpha and gradient
        w = w - alpha * dj_dw
        b = b - alpha * dj_db
    # Save cost J,w,b at each save interval for graphing
    if i == 0 or i % save_interval == 0:
        hist["cost"].append(compute_cost(X, y, w, b))
        hist["params"].append([w, b])
        hist["grads"].append([dj_dw, dj_db])
        hist["iter"].append(i)
    if i % math.ceil(num_iters / 10) == 0:
        cst = cost_function(X, y, w, b)
        print(
    str(i)
    + " "
    + format(float(cst[0]), '0.5e')
    + " "
    + " ".join([format(val, '0.1e') for val in w])
    + " "
    + format(b, '0.1e')
    + " "
    + " ".join([format(val, '0.1e') for val in dj_dw])
    + " "
    + format(dj_db, '0.1e')
)
    return w, b, hist # return w,b and history for graphing
def run_gradient_descent(X, y, iterations=1000, alpha=1e-6):
    m, n = X.shape
    # initialize parameters
    initial_w = np.zeros(n)
    initial_b = 0
    # run gradient descent
    w_out, b_out, hist_out = gradient_descent(X, y, initial_w, initial_b,
    compute_cost,
    compute_gradient, alpha, iterations)
    print(f"w,b found by gradient descent: w: {w_out}, b: {b_out:0.2f}")
    return (w_out, b_out, hist_out)
_,_,hist = run_gradient_descent(X_train, y_train, 10, alpha = 9.9e-7)
_,_,hist = run_gradient_descent(X_train, y_train, 10, alpha = 9e-7)
_,_,hist = run_gradient_descent(X_train, y_train, 10, alpha = 1e-7)
def zscore_normalize_features(X):
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X_norm = (X - mu) / sigma
    return (X_norm, mu, sigma)
mu = np.mean(X_train,axis=0)
sigma = np.std(X_train,axis=0)
X_mean = (X_train - mu)
X_norm = (X_train - mu)/sigma
fig,ax=plt.subplots(1, 3, figsize=(12, 3))
ax[0].scatter(X_train[:,0], X_train[:,3])
ax[0].set_xlabel(X_features[0]); ax[0].set_ylabel(X_features[3]);
ax[0].set_title("unnormalized")
ax[0].axis('equal')
ax[1].scatter(X_mean[:,0], X_mean[:,3])
ax[1].set_xlabel(X_features[0]); ax[0].set_ylabel(X_features[3]);
ax[1].set_title(r"X - $\mu$")
ax[1].axis('equal')
ax[2].scatter(X_norm[:,0], X_norm[:,3])
ax[2].set_xlabel(X_features[0]); ax[0].set_ylabel(X_features[3]);
ax[2].set_title(r"Z-score normalized")
ax[2].axis('equal')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
fig.suptitle("distribution of features before, during, afternormalization")
plt.show()
X_norm, X_mu, X_sigma = zscore_normalize_features(X_train)
fig,ax=plt.subplots(1, 4, figsize=(12, 3))
from scipy.stats import norm
def norm_plot(ax, data):
    scale = (np.max(data) - np.min(data)) * 0.2
    x = np.linspace(np.min(data) - scale, np.max(data) + scale, 50)
    _, bins, _ = ax.hist(data, x, color="xkcd:azure")
    # ax.set_ylabel("Count")
    mu = np.mean(data);
    std = np.std(data);
    dist = norm.pdf(bins, loc=mu, scale=std)
    axr = ax.twinx()
    axr.plot(bins, dist, color="orangered", lw=2)
    axr.set_ylim(bottom=0)
    axr.axis('off')
for i in range(len(ax)):
    norm_plot(ax[i],X_train[:,i],)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("count");
fig.suptitle("distribution of features before normalization")
plt.show()
fig,ax=plt.subplots(1,4,figsize=(12,3))
for i in range(len(ax)):
    norm_plot(ax[i],X_norm[:,i],)
    ax[i].set_xlabel(X_features[i])
ax[0].set_ylabel("count");
fig.suptitle("distribution of features after normalization")
plt.show()
w_norm, b_norm, hist = run_gradient_descent(X_norm, y_train, 1000, 1.0e-1,)
m = X_norm.shape[0]
yp = np.zeros(m)
for i in range(m):
    yp[i] = np.dot(X_norm[i], w_norm) + b_norm
    # plot predictions and targets versus original features
fig,ax=plt.subplots(1,4,figsize=(12, 3),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],y_train, label = 'target')
    ax[i].set_xlabel(X_features[i])
    ax[i].scatter(X_train[:,i],yp,color="orangered", label = 'predict')
ax[0].set_ylabel("Price"); ax[0].legend();
fig.suptitle("target versus prediction using z-score normalized model")
plt.show()
# First, normalize our example.
x_house = np.array([1200, 3, 1, 40])
x_house_norm = (x_house - X_mu) / X_sigma
print(x_house_norm)
x_house_predict = np.dot(x_house_norm, w_norm) + b_norm
print(f" predicted price of a house with 1200 sqft, 3 bedrooms, 1 floor, 40years old = ${x_house_predict*1000:0.0f}")