import streamlit as st

# Set page configuration
st.set_page_config(page_title="Unit Converter", page_icon="🔢", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border-radius: 5px;
            padding: 10px 24px;
        }
        .stButton > button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🌍 Unit Converter")
st.markdown("Convert units across different categories effortlessly.")

# Sidebar for category selection
st.sidebar.header("Select Conversion Category")
conversions = {
    "Length": {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084, "Yards": 1.09361, "Miles": 0.000621371, "Nautical Miles": 0.000539957},
    "Area": {"Square Meters": 1, "Square Kilometers": 0.000001, "Square Centimeters": 10000, "Square Millimeters": 1000000, "Square Inches": 1550.0031, "Square Feet": 10.7639, "Square Yards": 1.19599, "Acres": 0.000247105, "Hectares": 0.0001},
    "Data Transfer Rate": {"Bits per second": 1, "Kilobits per second": 0.001, "Megabits per second": 0.000001, "Gigabits per second": 0.000000001},
    "Digital Storage": {"Bytes": 1, "Kilobytes": 0.001, "Megabytes": 0.000001, "Gigabytes": 0.000000001, "Terabytes": 0.000000000001},
    "Energy": {"Joules": 1, "Kilojoules": 0.001, "Calories": 0.239006, "Kilocalories": 0.000239006, "Watt-hours": 0.000277778},
    "Frequency": {"Hertz": 1, "Kilohertz": 0.001, "Megahertz": 0.000001, "Gigahertz": 0.000000001},
    "Fuel Economy": {"Kilometers per liter": 1, "Miles per gallon": 2.35215},
    "Mass": {"Kilograms": 1, "Grams": 1000, "Milligrams": 1_000_000, "Pounds": 2.20462, "Ounces": 35.274, "Tonnes": 0.001},
    "Plane Angle": {"Degrees": 1, "Radians": 0.0174533},
    "Pressure": {"Pascals": 1, "Kilopascals": 0.001, "Bars": 0.00001, "Atmospheres": 0.0000098692},
    "Speed": {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084, "Knots": 1.94384},
    "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"},
    "Time": {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400},
    "Volume": {"Liters": 1, "Milliliters": 1000, "Cubic meters": 0.001, "Cubic centimeters": 1000, "Cubic inches": 61.0237, "Cubic feet": 0.0353147, "Gallons": 0.264172}
}

type_selection = st.sidebar.selectbox("Select Category", list(conversions.keys()))

# Layout for unit selection and conversion
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", list(conversions[type_selection].keys()))
with col2:
    to_unit = st.selectbox("To", list(conversions[type_selection].keys()))

# Input field for value
value = st.number_input("Enter Value", min_value=0.0, format="%.2f")

# Convert button
if st.button("Convert"):
    if type_selection == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            result = (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            result = (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            result = value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            result = value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            result = (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            result = (value - 273.15) * 9/5 + 32
        else:
            result = value
    else:
        result = value * (conversions[type_selection][to_unit] / conversions[type_selection][from_unit])
    
    st.success(f"Converted Value: {result:.2f} {to_unit}")
