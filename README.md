# 🌲 Forest Cover Type Prediction

A Machine Learning project that predicts the **type of forest cover** based on cartographic variables such as elevation, slope, soil type, and distances to hydrology or roads.

This project demonstrates an **end-to-end ML workflow**, including data preprocessing, model training, handling class imbalance, model evaluation, and deploying a **Streamlit web application** for predictions.

---

# 📌 Project Overview

Forest cover classification is an important problem in environmental science and forestry management. The goal of this project is to **predict the dominant forest cover type** for a given region using cartographic variables.

The model is trained on the **Forest Cover Type dataset**, which contains geographical and environmental attributes of forested areas.

The final solution includes:

* Data preprocessing and feature engineering
* Handling class imbalance using SMOTE
* Training multiple machine learning models
* Selecting the best-performing model
* Saving the trained model and encoders
* Deploying an interactive **Streamlit web application**

---

# 📂 Project Structure

```
EcoType Forest Cover Classification/
│
├── data/
│   └── cover_type.csv
│
├── models/
│   ├── best_model.pkl
│   ├── target_encoder.pkl
│   └── feature_names.pkl
│
├── notebooks/
│   └── forest_cover_training.ipynb
│
├── app.py
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

Dataset used: **Forest Cover Type Dataset**

The dataset contains **cartographic variables** collected from US Forest Service data.

### Feature Examples

* Elevation
* Aspect
* Slope
* Horizontal Distance to Hydrology
* Vertical Distance to Hydrology
* Horizontal Distance to Roadways
* Hillshade (9am, Noon, 3pm)
* Wilderness Area
* Soil Type

### Target Variable

**Cover_Type**

The dataset contains **7 forest cover classes**:

| Label | Forest Cover Type |
| ----- | ----------------- |
| 1     | Spruce/Fir        |
| 2     | Lodgepole Pine    |
| 3     | Ponderosa Pine    |
| 4     | Cottonwood/Willow |
| 5     | Aspen             |
| 6     | Douglas-fir       |
| 7     | Krummholz         |

---

# ⚙️ Technologies Used

### Programming Language

* Python

### Libraries

**Data Processing**

* Pandas
* NumPy

**Visualization**

* Matplotlib
* Seaborn

**Machine Learning**

* Scikit-learn
* XGBoost
* Imbalanced-Learn (SMOTE)

**Deployment**

* Streamlit

---

# 🧠 Machine Learning Pipeline

The workflow used in this project:

1. Data Loading
2. Duplicate Removal
3. Missing Value Handling
4. Feature Transformation
5. Encoding categorical variables
6. Handling class imbalance using **SMOTE**
7. Train-Test split
8. Model training and evaluation
9. Model selection
10. Saving trained model and encoders

---

# 🤖 Models Used

Multiple classification algorithms were trained and compared:

* Random Forest Classifier
* Decision Tree Classifier
* Logistic Regression
* K-Nearest Neighbors
* XGBoost Classifier

The **best performing model** was saved and used in the Streamlit application.

---

# 📈 Model Evaluation

Models were evaluated using:

* Accuracy Score
* Confusion Matrix
* Classification Report

Example metrics used:

```
Accuracy
Precision
Recall
F1-score
```

---

# 💾 Saved Artifacts

The project saves important objects for deployment:

| File               | Description                        |
| ------------------ | ---------------------------------- |
| best_model.pkl     | Trained machine learning model     |
| target_encoder.pkl | Label encoder for target variable  |
| feature_names.pkl  | Feature order used during training |

Saving these ensures the **Streamlit application uses the same pipeline as training**.

---

# 🚀 Running the Project

## 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/forest-cover-prediction.git
cd forest-cover-prediction
```

---

## 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Mac/Linux:

```
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 4️⃣ Run Streamlit App

```
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

# 🖥️ Streamlit Application

The Streamlit application allows users to:

* Input environmental features
* Predict forest cover type
* View the predicted class instantly

The app dynamically loads **feature names and model artifacts** to ensure predictions are consistent with the trained model.

---

# 📌 Future Improvements

Possible improvements for this project:

* Hyperparameter tuning for better model performance
* Feature importance analysis
* Better UI with grouped inputs
* Model explainability using SHAP
* Deployment on cloud platforms (AWS / GCP / Streamlit Cloud)
* API deployment using FastAPI

---

# 📜 License

This project is for **educational and learning purposes**.

---

# 👨‍💻 Author

**Vasu Gadde**

Data Analyst | Python Developer | Machine Learning Enthusiast

---