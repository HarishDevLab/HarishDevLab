#BFS
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)
    result = []

    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return result

# Sample graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F']

#UCS
import heapq

def ucs(graph, start, goal):
    # Priority queue: (cost, node, path)
    pq = [(0, start, [start])]
    # Minimum cost to reach each node
    cost_so_far = {start: 0}

    while pq:
        cost, node, path = heapq.heappop(pq)

        # Goal test on expansion (guaranteed optimal)
        if node == goal:
            return path, cost

        for neighbor, weight in graph[node]:
            new_cost = cost + weight
            if new_cost < cost_so_far.get(neighbor, float('inf')):
                cost_so_far[neighbor] = new_cost
                heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return None, float('inf')

# Sample weighted graph (adjacency list)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

path, cost = ucs(graph, 'A', 'D')
print(f"Shortest path: {path}, Cost: {cost}")
# Output: Shortest path: ['A', 'B', 'C', 'D'], Cost: 4

dls

def dls(graph, node, goal, depth_limit, depth=0, visited=None):
    if visited is None:
        visited = set()

    if depth > depth_limit:
        return "cutoff", []          # reached limit, no result here

    visited.add(node)

    if node == goal:
        return "success", [node]     # goal found

    cutoff_occurred = False

    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result, path = dls(graph, neighbor, goal, depth_limit, depth+1, visited)
            if result == "success":
                return "success", [node] + path
            if result == "cutoff":
                cutoff_occurred = True

    visited.remove(node)            # backtrack (for correct path search)
    return "cutoff" if cutoff_occurred else "failure", []

# Sample graph (same unweighted adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

# Test: find 'G' with limit 2 (depth of G is 3, so should fail)
status, path = dls(graph, 'A', 'G', 2)
print(status, path)   # Output: cutoff []

# Test: find 'G' with limit 3 (should succeed)
status, path = dls(graph, 'A', 'G', 3)
print(status, path)   # Output: success ['A', 'B', 'D', 'G']

ids
def iterative_deepening(graph, start, goal, max_depth=50):
    for depth_limit in range(max_depth + 1):
        status, path = dls(graph, start, goal, depth_limit)
        if status == "success":
            return path
        if status == "failure":      # no more nodes, graph exhausted
            return None
    return None                      # exceeded max_depth

# Reuse the same DLS function from earlier (copied here for completeness)
def dls(graph, node, goal, depth_limit, depth=0, visited=None):
    if visited is None:
        visited = set()
    if depth > depth_limit:
        return "cutoff", []
    visited.add(node)
    if node == goal:
        return "success", [node]
    cutoff_occurred = False
    for neighbor in graph.get(node, []):
        if neighbor not in visited:
            result, path = dls(graph, neighbor, goal, depth_limit, depth+1, visited)
            if result == "success":
                return "success", [node] + path
            if result == "cutoff":
                cutoff_occurred = True
    visited.remove(node)
    return "cutoff" if cutoff_occurred else "failure", []

# Sample graph (unweighted)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

path = iterative_deepening(graph, 'A', 'G')
print("Path:", path)   # Output: Path: ['A', 'B', 'D', 'G']


DFS

# ----- Recursive DFS -----
def dfs_recursive(graph, node, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    if node == goal:
        return [node]
    for neighbor in graph[node]:
        if neighbor not in visited:
            path = dfs_recursive(graph, neighbor, goal, visited)
            if path:
                return [node] + path
    return None

# ----- Iterative DFS (using stack) -----
def dfs_iterative(graph, start, goal):
    stack = [(start, [start])]
    visited = set()
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == goal:
                return path
            # Push neighbours (reverse for left-to-right order)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return None

# Sample graph (same as earlier)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['G'],
    'E': [],
    'F': [],
    'G': []
}

print("Recursive path:", dfs_recursive(graph, 'A', 'G'))
# Output: ['A', 'B', 'D', 'G']

print("Iterative path:", dfs_iterative(graph, 'A', 'G'))
# Output: ['A', 'B', 'D', 'G']



 Greedy Best‑First Search

import heapq

def greedy_best_first(graph, start, goal, heuristic):
    pq = [(heuristic[start], start, [start])]   # (h, node, path)
    visited = set()

    while pq:
        h_val, node, path = heapq.heappop(pq)
        if node == goal:
            return path
        if node in visited:
            continue
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(pq, (heuristic[neighbor], neighbor, path + [neighbor]))
    return None

# Sample graph (weighted or unweighted, we need coordinates for heuristic)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Straight-line distance heuristic to goal 'F'
heuristic = {
    'A': 5,
    'B': 4,
    'C': 3,
    'D': 6,
    'E': 2,
    'F': 0
}

path = greedy_best_first(graph, 'A', 'F', heuristic)
print("Path:", path)   # Output: Path: ['A', 'C', 'F']


 A*

import heapq

def a_star(graph, start, goal, heuristic):
    pq = [(0 + heuristic[start], 0, start, [start])]  # (f, g, node, path)
    best_g = {start: 0}  # best known g to each node

    while pq:
        f, g, node, path = heapq.heappop(pq)
        if node == goal:
            return path, g
        if g > best_g.get(node, float('inf')):
            continue  # skipped: already expanded with better g

        for neighbor, weight in graph[node]:
            new_g = g + weight
            if new_g < best_g.get(neighbor, float('inf')):
                best_g[neighbor] = new_g
                new_f = new_g + heuristic[neighbor]
                heapq.heappush(pq, (new_f, new_g, neighbor, path + [neighbor]))
    return None, None

# Sample graph (weighted edges)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

# Heuristic: straight-line distances to goal 'D'
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}

path, cost = a_star(graph, 'A', 'D', heuristic)
print("Path:", path, "Cost:", cost)
# Output: Path: ['A', 'B', 'C', 'D'] Cost: 4


 Naïve Bayes 

import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# 1. Load data
df = pd.read_excel("weather_data.xlsx")

# 2. Encode all columns (features + target) to integers
encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    encoders[col] = le

# 3. Split features (X) and target (y)
X = df[['Outlook', 'Temperature', 'Humidity', 'Windy']]
y = df['Play']

# 4. Train Categorical Naïve Bayes
model = CategoricalNB()
model.fit(X, y)

# 5. Predict a new instance (must be encoded the same way)
test = [[
    encoders['Outlook'].transform(['Rainy'])[0],
    encoders['Temperature'].transform(['Cool'])[0],
    encoders['Humidity'].transform(['High'])[0],
    encoders['Windy'].transform([True])[0]
]]
pred = model.predict(test)

# 6. Decode prediction back to original label
result = encoders['Play'].inverse_transform(pred)
print("Play?", result[0])   # e.g., Yes or No

Linear Regression Coefficient


import numpy as np
import matplotlib.pyplot as plt

# Data
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# Means
x_mean = np.mean(x)
y_mean = np.mean(y)

# Regression y on x (y ~ x)
b_yx = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2)
a_yx = y_mean - b_yx * x_mean
y_pred = a_yx + b_yx * x

# Regression x on y (x ~ y)
b_xy = np.sum((x - x_mean) * (y - y_mean)) / np.sum((y - y_mean) ** 2)
a_xy = x_mean - b_xy * y_mean
x_pred = a_xy + b_xy * y

print(f"y on x: y = {a_yx:.2f} + {b_yx:.2f} * x")
print(f"x on y: x = {a_xy:.2f} + {b_xy:.2f} * y")

# Plotting (two lines with same scatter)
plt.figure(figsize=(8,6))
plt.scatter(x, y, color='blue', label='Data')
plt.plot(x, y_pred, 'g-', label='y on x')
# For x on y, plot x_pred against y (swap axes)
sorted_idx = np.argsort(y)
plt.plot(x_pred[sorted_idx], y[sorted_idx], 'r-', label='x on y')
plt.xlabel('x'); plt.ylabel('y')
plt.title('Both Regression Lines')
plt.legend(); plt.grid(True)
plt.show()

Logistic Regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Load data
data = pd.read_excel('your_dataset.xlsx')

# 2. Features (X) and target (y)
X = data[['GPA', 'SAT_Score', 'Extracurriculars']]
y = data['Admission']

# 3. Train‑test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# 4. Train logistic regression
model = LogisticRegression()
model.fit(X_train, y_train)

# 5. Look at coefficients & intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# 6. Predict probabilities and classes
probs = model.predict_proba(X_test)   # probability for classes 0 and 1
preds = model.predict(X_test)         # class labels

# 7. Plot (GPA vs SAT only, showing admission)
plt.figure(figsize=(8,6))
scatter = plt.scatter(
    data['GPA'], data['SAT_Score'],
    c=data['Admission'], cmap='coolwarm', edgecolor='k'
)
plt.xlabel('GPA')
plt.ylabel('SAT Score')
plt.title('Admission by GPA & SAT')
plt.colorbar(scatter, label='0 = No, 1 = Yes')
plt.grid(True)
plt.show()



Decision Trees

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# 1. Sample data (often you'd load from CSV/Excel)
data = {
    'Age': ['Youth','Youth','Middle-aged','Senior','Senior', ...],
    'Income': [...],
    'Student': [...],
    'Credit_rating': [...],
    'Buys_computer': ['No','No','Yes','Yes','Yes', ...]
}
df = pd.DataFrame(data)

# 2. Convert categorical strings to numbers
label_encoders = {}
for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 3. Separate features and target
X = df.drop('Buys_computer', axis=1)
y = df['Buys_computer']

# 4. Build the tree with entropy (ID3 style)
model = DecisionTreeClassifier(criterion='entropy')
model.fit(X, y)

# 5. Plot the tree
plt.figure(figsize=(12,7))
plot_tree(model, feature_names=X.columns, class_names=['No','Yes'], filled=True)
plt.title("Decision Tree - Buys Computer")
plt.show()

# Bonus: predict a new instance
# new = [[Youth(0), High(0), No(0), Fair(0)]]  # after encoding
# prediction = model.predict(new)
# print(label_encoders['Buys_computer'].inverse_transform(prediction))


Random Forest

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# 1. Load data
df = pd.read_excel('fruit_data.xlsx')

# 2. Encode target manually (or use LabelEncoder)
df['Fruit_Type_Label'] = df['Fruit Type'].map({'Apple':0, 'Orange':1, 'Banana':2})

# 3. Features & target
X = df[['Weight (g)', 'Color (encoded)', 'Size (cm)', 'Shape (encoded)']]
y = df['Fruit_Type_Label']

# 4. Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 5. Build random forest (100 trees, default settings)
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# 6. Evaluate
y_pred = rf.predict(X_test)
print(f'Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%')

# 7. Predict a single fruit
def predict_fruit(weight, color, size, shape):
    pred = rf.predict([[weight, color, size, shape]])
    fruits = {0: 'Apple', 1: 'Orange', 2: 'Banana'}
    print(f'Predicted fruit: {fruits[pred[0]]}')

predict_fruit(160, 1, 6, 1)


SVM 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder

# 1. Load & clean data
df = pd.read_excel('data.xlsx').dropna()
X = df[['Feature1', 'Feature2']]
y = df['Class']

# 2. Encode target labels (if string)
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 3. Train linear SVM
model = SVC(kernel='linear')
model.fit(X, y_encoded)

# 4. Get margin & print
w = model.coef_[0]                      # weight vector
margin = 2 / np.linalg.norm(w)          # margin width = 2/||w||
print(f"Maximum margin: {margin:.4f}")

# 5. Plot decision boundary & support vectors
b = model.intercept_[0]
x_vals = np.linspace(X.iloc[:,0].min(), X.iloc[:,0].max(), 100)
y_vals = -(w[0] * x_vals + b) / w[1]   # decision line: w·x + b = 0

plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=y_encoded, cmap='bwr')
plt.plot(x_vals, y_vals, 'k--', label='Decision Boundary')
# Highlight support vectors
sv = model.support_vectors_
plt.scatter(sv[:,0], sv[:,1], facecolors='none', edgecolors='black',
            s=100, linewidths=1.5, label='Support Vectors')
plt.xlabel('Feature1'); plt.ylabel('Feature2')
plt.title('Linear SVM with Support Vectors')
plt.legend(); plt.grid(True)
plt.show()



K‑Means Clustering

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Load data (header=1 means first row is not data, adjust as needed)
df = pd.read_excel('student_marks.xlsx', header=1)
print(df)

# 2. Features (numeric columns only)
X = df[['Maths', 'Science']]

# 3. Create K‑Means (here K=2)
kmeans = KMeans(n_clusters=2, random_state=0)
kmeans_labels = kmeans.fit_predict(X)   # fit and get cluster labels

# 4. Add cluster labels to dataframe
df['Cluster'] = kmeans_labels

# 5. Plot clusters and centroids
plt.figure(figsize=(8,6))
# Scatter each cluster
plt.scatter(df[df['Cluster']==0]['Maths'], df[df['Cluster']==0]['Science'],
            s=100, c='blue', label='Cluster 0')
plt.scatter(df[df['Cluster']==1]['Maths'], df[df['Cluster']==1]['Science'],
            s=100, c='red', label='Cluster 1')
# Centroids (marked with X)
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], s=200, c='red', marker='X', label='Centroids')
plt.xlabel('Maths Marks'); plt.ylabel('Science Marks')
plt.title('Student Clusters Based on Marks')
plt.legend(); plt.grid(True)
plt.show()


DEEP LEARNING MODELS

import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split

# 1. Load data
dataset = pd.read_excel("dataset_features.xlsx")
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# 2. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Build model
model = Sequential([
    Dense(128, input_dim=X_train.shape[1], activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='sigmoid')          # binary output
])

# 4. Compile
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 5. Train
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=32,
    validation_data=(X_test, y_test)
)

# 6. Evaluate
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy*100:.2f}%")

# 7. Inspect weights (optional)
weights = model.get_weights()
print("First layer weights shape:", weights[0].shape)

# 8. Plot learning curves
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Val Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()
plt.grid(True)
plt.show()