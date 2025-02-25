import streamlit as st

# Title
st.title("Unit Converter")

# Conversion Dictionary
conversions = {
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Inches": 39.3701,
        "Feet": 3.28084,
        "Yards": 1.09361,
        "Miles": 0.000621371,
    },
    "Weight": {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F"
    }
}

# Category selection
type_selection = st.selectbox("Select Category", list(conversions.keys()))

# Dropdowns for unit selection
from_unit = st.selectbox("From", list(conversions[type_selection].keys()))
to_unit = st.selectbox("To", list(conversions[type_selection].keys()))

# Input field for value
value = st.number_input("Enter Value", format="%.2f")

# Convert button
if st.button("Convert"):
    if type_selection == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        else:
            result = value
    else:
        result = value * (conversions[type_selection][to_unit] / conversions[type_selection][from_unit])
    
    st.success(f"Converted Value: {result:.2f} {to_unit}")
