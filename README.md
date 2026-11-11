# 🏠 House Price Prediction Using Machine Learning

A Machine Learning project that predicts the price of a house based on different property features such as bedrooms, bathrooms, living area, lot size, number of floors, waterfront availability, view quality, house condition, construction grade, basement area, and year built.

The trained model is integrated with a **Streamlit web application**, allowing users to enter house details and receive a predicted house price.

---

## 📌 Project Overview

The main objective of this project is to build a regression-based Machine Learning model that can estimate house prices from property characteristics.

The project includes:

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Outlier handling
- Correlation analysis
- Feature scaling
- Multiple regression models
- Model evaluation using R² score
- Model serialization using Pickle
- Streamlit web application for prediction

---

## 📂 Project Structure

```text
House-Price-Prediction/
│
├── house_data.csv
├── work.ipynb
├── stream.py
├── model.sav
├── scaler.sav
├── README.md
└── requirements.txt
```

### File Description

| File | Description |
|---|---|
| `house_data.csv` | Dataset used for training |
| `work.ipynb` | Complete data analysis, preprocessing, model training and evaluation |
| `stream.py` | Streamlit application for house price prediction |
| `model.sav` | Saved trained Random Forest regression model |
| `scaler.sav` | Saved `StandardScaler` used during model training |
| `README.md` | Project documentation |
| `requirements.txt` | Required Python packages |

---

## 📊 Dataset

The project uses a house-price dataset containing property-related information.

The original dataset contains features such as:

- Number of bedrooms
- Number of bathrooms
- Living area
- Lot area
- Number of floors
- Waterfront
- View
- Condition
- Grade
- Above-ground living area
- Basement area
- Year built
- Year renovated
- House price

During preprocessing, unnecessary columns such as ID, date, latitude, longitude, zipcode, and some duplicate living/lot area features were removed.

---

## 🧹 Data Preprocessing

Several preprocessing steps were performed before training the models.

### Removed unnecessary columns

The following columns were removed:

```text
id
date
lat
long
sqft_living15
sqft_lot15
zipcode
```

### Duplicate removal

Duplicate records were identified and removed.

### Year Renovated

The `yr_renovated` feature was converted into a binary feature:

```text
0 → Not renovated
1 → Renovated
```

### Bathrooms

Bathroom values were converted to integer values.

### Bedrooms

Bedroom values were filtered to remove invalid/extreme values.

The final condition used was:

```text
bedrooms <= 9
bedrooms > 0
```

---

## 🔎 Exploratory Data Analysis

The project performs several EDA steps to understand the dataset.

These include:

- Checking dataset information
- Checking missing values
- Checking duplicate values
- Checking unique values
- Detecting potential outliers using boxplots
- Examining bedroom distributions
- Correlation analysis
- House condition analysis
- House grade analysis

A correlation heatmap was also used to understand relationships between numerical features.

---

## 🧠 Machine Learning Models

Several regression algorithms were trained and evaluated.

### 1. Decision Tree Regressor

```python
DecisionTreeRegressor(
    max_depth=20,
    min_samples_split=3,
    min_samples_leaf=4,
    max_features='sqrt',
    random_state=42
)
```

### 2. K-Nearest Neighbors Regressor

```python
KNeighborsRegressor(n_neighbors=5)
```

### 3. Linear Regression

```python
LinearRegression()
```

### 4. Random Forest Regressor

The final model used for the application is a Random Forest Regressor:

```python
RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    min_samples_split=5,
    min_samples_leaf=2,
    max_features='log2'
)
```

The models were evaluated using the **R² (R-squared) score**.

---

## ⚙️ Feature Scaling

Before training, the input features were standardized using `StandardScaler`.

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
x = scaler.fit_transform(x)
```

The fitted scaler was saved for use during prediction:

```python
p.dump(scaler, open('scaler.sav', 'wb'))
```

This is important because the Streamlit application must apply the **same scaling process** to new user input before sending it to the trained model.

---

## 💾 Model Saving

The trained Random Forest model was saved using Pickle:

```python
p.dump(random, open('model.sav', 'wb'))
```

Two important files are therefore required by the Streamlit application:

```text
model.sav
scaler.sav
```

---

## 🖥️ Streamlit Application

The project includes a Streamlit interface where users can enter property information.

The application accepts inputs such as:

- Bedrooms
- Bathrooms
- Living area
- Lot size
- Floors
- Waterfront
- View quality
- House condition
- Construction/design grade
- Above-ground living area
- Basement area
- Year built
- Renovation status

The Streamlit application converts categorical inputs into numerical values before prediction.

For example:

```text
Waterfront:
Yes → 1
No  → 0
```

View quality:

```text
No view       → 0
Fair view     → 1
Good view     → 2
Very good view→ 3
Excellent view→ 4
```

House condition:

```text
Poor      → 1
Fair      → 2
Average   → 3
Good      → 4
Excellent → 5
```

---

## 🔄 Prediction Workflow

The complete prediction workflow is:

```text
User enters house details
          ↓
Streamlit collects input
          ↓
Categorical values converted to numbers
          ↓
Input arranged in correct feature order
          ↓
Saved StandardScaler transforms input
          ↓
Saved Random Forest model receives input
          ↓
House price prediction
          ↓
Predicted price displayed to user
```

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd House-Price-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv env
```

### 3. Activate the environment

#### Windows

```bash
env\Scripts\activate
```

#### Linux/macOS

```bash
source env/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Start the Streamlit application

```bash
streamlit run stream.py
```

The application will open in your browser.

---

## 📦 Requirements

Example `requirements.txt`:

```text
streamlit
pandas
numpy
scikit-learn
matplotlib
seaborn
```

---

## 🧪 Example Input

A user can provide information such as:

```text
Bedrooms       : 3
Bathrooms      : 2
Living Area    : 1800 sq ft
Lot Size       : 5000 sq ft
Floors         : 1
Waterfront     : No
View           : Good view
Condition      : Good
Grade          : 7
Above Ground   : 1800 sq ft
Basement       : 0 sq ft
Year Built     : 2005
Renovated      : No
```

The application then processes these values and generates an estimated house price.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- Random Forest Regression
- Decision Tree Regression
- KNN Regression
- Linear Regression

### Data Processing

- Pandas
- NumPy

### Data Visualization

- Matplotlib
- Seaborn

### Web Application

- Streamlit

### Model Serialization

- Pickle

---

## 📈 Model Evaluation

The models were evaluated using the **R² score**.

R² measures how well the model explains the variation in house prices.

A value closer to `1.0` indicates better predictive performance.

The notebook evaluates both training and testing performance for the different regression models.

---

## 🔮 Future Improvements

Possible improvements for this project include:

- Hyperparameter tuning
- Cross-validation
- Additional feature engineering
- Comparing more regression algorithms
- Improving the Streamlit UI
- Adding prediction confidence or an estimated price range
- Adding interactive charts
- Deploying the application online
- Using a more advanced ensemble model
- Adding model performance comparison to the Streamlit application

---

## ⚠️ Disclaimer

The predicted price is an **estimated value generated by a Machine Learning model**. It should not be considered an official property valuation.

Actual property prices can vary depending on location, market conditions, property age, neighborhood, construction quality, demand, and other factors.

---

## 👨‍💻 Author

**Kripank MS**

This project was developed as a Machine Learning project to demonstrate data preprocessing, exploratory data analysis, regression modeling, model evaluation, and deployment using Streamlit.