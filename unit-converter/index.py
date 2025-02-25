import streamlit as st

# Title
st.title("Unit Converter")

# Conversion Dictionary
conversions = {
    "kg to lbs": 2.20462,
    "lbs to kg": 1 / 2.20462,
    "m to km": 0.001,
    "km to m": 1000,
    "cm to m": 0.01,
    "m to cm": 100,
    "inch to cm": 2.54,
    "cm to inch": 1 / 2.54,
    "c to f": lambda c: (c * 9/5) + 32,
    "f to c": lambda f: (f - 32) * 5/9
}

# Dropdown for unit selection
conversion_type = st.selectbox("Select Conversion Type", list(conversions.keys()))

# Input field for value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    conversion = conversions[conversion_type]
    result = conversion(value) if callable(conversion) else value * conversion
    st.success(f"Converted Value: {result:.2f}")
