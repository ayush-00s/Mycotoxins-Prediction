import streamlit as st
import pandas as pd
import numpy as np
import pickle
import tensorflow as tf
from tensorflow.keras.models import load_model

# Load the scaler, PCA, and trained ANN model
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('scaler_y.pkl', 'rb') as file:
    scaler_y = pickle.load(file)

with open('dimension_reduction_pca.pkl', 'rb') as file:
    pca = pickle.load(file)

# Load ANN Model properly
# Properly load ANN model with custom loss function
model = load_model('tuned_ann_model.h5', custom_objects={"mse": tf.keras.losses.MeanSquaredError()})


# Streamlit App
def main():
    st.title("Spectral Data Prediction App")
    st.write("Upload your spectral data (CSV file) to get predictions.")

    # File Uploader
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded file
        data = pd.read_csv(uploaded_file)
        st.write("Uploaded Data Preview:")
        st.write(data.head())

        # Keep only numeric columns
        numeric_data = data.select_dtypes(include=[np.number])
        non_numeric_columns = data.columns.difference(numeric_data.columns)

        if len(non_numeric_columns) > 0:
            st.warning(f"Dropped non-numeric columns: {list(non_numeric_columns)}")

        # Check if there are any numeric columns left
        if numeric_data.empty:
            st.error("No numeric columns found. Please upload a valid dataset.")
            return

        # Scale the input data
        scaled_data = scaler.transform(numeric_data)

        # Apply PCA dynamically
        if scaled_data.shape[1] != pca.n_features_in_:
            st.warning(
                f"Feature count mismatch! Adjusting using PCA. Expected: {pca.n_features_in_}, Found: {scaled_data.shape[1]}"
            )

        pca_data = pca.transform(scaled_data)

        # Make predictions using the ANN model
        predictions_scaled = model.predict(pca_data)
        predictions = scaler_y.inverse_transform(predictions_scaled).flatten()

        # Display predictions
        st.write("Predicted Target Values:")
        st.write(predictions)

        # Download button for predictions
        predictions_df = pd.DataFrame(predictions, columns=["Predictions"])
        st.download_button(
            label="Download Predictions as CSV",
            data=predictions_df.to_csv(index=False),
            file_name="predictions.csv",
            mime="text/csv"
        )

# Run the Streamlit App
if __name__ == "__main__":
    main()
