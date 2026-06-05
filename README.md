# Hyperspectral-Mycotoxin-Prediction
 

![Spectral Data Prediction]()  
<img width="958" alt="Screenshot 2025-03-13 at 4 54 14 PM" src="https://github.com/user-attachments/assets/868db99d-bc34-4812-a1ba-f0f9bb9b492b" />

🔗 **Live Demo**: [Visit the Website](https://hyperspectral-mycotoxin-prediction-shiva.streamlit.app/)  

---

## ✨ Features  
🔍 **Vomitoxin Prediction**: Predicts vomitoxin levels in spectral data using a deep learning model.  
📊 **Data Preprocessing**: Standardizes input data using **scaling** and **PCA-based dimensionality reduction**.  
🎛️ **Interactive UI**: Built with **Streamlit** for seamless user interaction.  
🧠 **Machine Learning Models**: Utilizes **ANN (Artificial Neural Network)** and **Random Forest** for inference.  
📈 **Visualization & Insights**: Provides spectral reflectance analysis and correlation studies.  

---

## 🛠️ Technologies Used  
- **Python**: Core language for ML and data analysis [🔗 Python](https://www.python.org/)  
- **Streamlit**: Web-based UI framework for easy interaction [🔗 Streamlit](https://streamlit.io/)  
- **TensorFlow/Keras**: Deep learning framework for ANN model [🔗 TensorFlow](https://www.tensorflow.org/)  
- **Scikit-learn**: Machine learning utilities and PCA transformation [🔗 Scikit-learn](https://scikit-learn.org/)  
- **Pandas & NumPy**: Efficient data handling and numerical computations [🔗 Pandas](https://pandas.pydata.org/)  

---

## 🚀 Getting Started  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/yourusername/spectral-data-prediction.git  
cd spectral-data-prediction  
```

### **2️⃣ Install Dependencies**  
Ensure all required packages are installed:  
```bash
pip install -r requirements.txt  
```

### **3️⃣ Ensure Required Files Exist**  
The following files are required for correct execution:  
- `tuned_ann_model.h5` – Pre-trained deep learning model  
- `scaler.pkl` – StandardScaler for input feature scaling  
- `scaler_y.pkl` – StandardScaler for target variable transformation  
- `dimension_reduction_pca.pkl` – PCA model for dimensionality reduction  
- `random_forest_model.pkl` – Alternative ML model  
- `TASK-ML-INTERN.csv` – Sample dataset for testing  

### **4️⃣ Run the Application**  
```bash
streamlit run app.py  
```

---

## 🗂️ Project Structure  
```
📂 spectral-data-prediction  
│── app.py                      # Main Streamlit app  
│── dimension_reduction_pca.pkl  # PCA model for feature reduction  
│── eda.ipynb                    # Exploratory Data Analysis notebook  
│── model.ipynb                   # Model training and evaluation notebook  
│── neuralmodel.ipynb            # ANN-based model development  
│── random_forest_model.pkl       # Pre-trained Random Forest model  
│── requirements.txt              # List of dependencies  
│── scaler_y.pkl                  # Scaler for target variable  
│── scaler.pkl                    # Scaler for input features  
│── TASK-ML-INTERN.csv            # Sample dataset  
│── tuned_ann_model.h5            # Trained ANN model  
│── your-image.png                # Project banner image  
```

---

## 🔬 Data Preprocessing  
- **Scaling**: Standardizes input spectral data using `scaler.pkl`.  
- **Dimensionality Reduction**: PCA transformation (`dimension_reduction_pca.pkl`).  
- **Feature Selection**: Removes unnecessary columns and selects important spectral bands.  

---

## 📈 Model & Prediction  
- **ANN Model** (tuned with Keras and TensorFlow).  
- **Random Forest Model** (as an alternative).  
- **Real-time Predictions**: Users can upload CSV files and receive instant results.  
- **Visualization**: Displays spectral reflectance trends, feature correlations, and predictions.  

---

## 📊 AI-Driven Insights  
The model analyzes hyperspectral bands and identifies **patterns in reflectance** to predict vomitoxin levels. The insights help in **agriculture, food safety, and material analysis**.  

---

## 👨‍💻 Author  
Developed by **Shiva Kant Pandey**  

🚀 Ready to revolutionize spectral data analysis? Let's go! 🎯  
