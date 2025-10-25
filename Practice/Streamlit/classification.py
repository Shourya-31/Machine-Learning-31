import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# ✅ use st.cache_data decorator for data loading
@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

# ✅ Train the RandomForest model
model = RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

# ✅ Corrected: there is no st.slider.title()
st.sidebar.title("Input Features")

# ✅ fixed typo: "Speal" → "Sepal"
sepal_length = st.sidebar.slider(
    "Sepal length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)
sepal_width = st.sidebar.slider(
    "Sepal width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)
petal_length = st.sidebar.slider(
    "Petal length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)
petal_width = st.sidebar.slider(
    "Petal width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

# ✅ Prepare input data
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
    columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

prediction = model.predict(input_data)


# ✅ Make prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

# ✅ Display result
st.subheader("Prediction")
st.write(f"The predicted species is: **{predicted_species}**")
