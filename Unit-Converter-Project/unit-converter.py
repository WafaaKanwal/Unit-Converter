import streamlit as st  

st.title("🔄 Unit Converter")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Select a category, choose units, enter a value, and press 'Convert'.")

category = st.selectbox("📌 Choose a Category", ["Length", "Weight", "Time"])

unit_options = {
    "Length": {
        "Kilometers": 1.0,
        "Miles": 0.621371,
        "Meters": 1000,
        "Feet": 3280.84,
        "Centimeters": 100000,
        "Inches": 39370.1
    },
    "Weight": {
        "Kilograms": 1.0,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    },
    "Time": {
        "Seconds": 1.0,
        "Minutes": 1 / 60,
        "Hours": 1 / 3600,
        "Days": 1 / 86400
    }
}

from_unit = st.selectbox("Convert From", list(unit_options[category].keys()))
to_unit = st.selectbox("Convert To", list(unit_options[category].keys()))
value = st.text_input("Enter value to convert", "", key="value_input")

def convert_units(value, from_unit, to_unit, category_units):
    try:
        value = float(value)  
        if value == 0:
            return 0  
        base_value = value / category_units[from_unit]  # Convert to base unit
        converted_value = base_value * category_units[to_unit]  # Convert to target unit
        return converted_value
    except ValueError:
        return None  


if st.button("🔄 Convert", key="convert_button"):
    if value.strip():  # Empty input check
        result = convert_units(value, from_unit, to_unit, unit_options[category])
        if result is None:
            st.error("❌ Invalid input! Please enter a numeric value.")
        elif result == 0:
            st.info("ℹ️ 0 remains 0 in all conversions.")
        else:
            st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.warning("⚠️ Please enter a value to convert.")


