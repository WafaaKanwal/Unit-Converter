import streamlit as st


# Custom CSS 
st.markdown("""
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 24px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stMarkdown h3 {
        color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and description
st.title("📏 Unit Converter")
st.markdown("Convert **length**, **weight**, and **time** with ease.")

# Unit conversion options
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

# Category selection
category = st.selectbox(
    "📌 **Choose a Category**",
    options=list(unit_options.keys()),
    index=0
)

# Unit selection in columns
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox(
        "**Convert From**",
        options=list(unit_options[category].keys()),
        index=0
    )
with col2:
    to_unit = st.selectbox(
        "**Convert To**",
        options=list(unit_options[category].keys()),
        index=1
    )

# Value input
value = st.text_input(
    "**Enter Value**",
    value="",
    placeholder="e.g., 100",
    help="Enter the numeric value you want to convert."
)

# Conversion function
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

# Convert button
if st.button("🔄 **Convert**", use_container_width=True):
    if value.strip():  # Check if input is not empty
        result = convert_units(value, from_unit, to_unit, unit_options[category])
        if result is None:
            st.error("❌ **Invalid input!** Please enter a numeric value.")
        elif result == 0:
            st.info("ℹ️ **0 remains 0 in all conversions.**")
        else:
            st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")
    else:
        st.warning("⚠️ **Please enter a value to convert.**")

# Footer
st.markdown("---")
st.caption("📏 Made with Streamlit | Designed by [Wafa](https://www.linkedin.com/in/wafa-kanwal-467376279/)")