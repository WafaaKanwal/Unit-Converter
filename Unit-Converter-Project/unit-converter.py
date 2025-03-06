import streamlit as st  

st.title("🔄 Unit Converter")
st.markdown("### Convert Length, Weight, and Time Instantly")
st.write("Select a category, choose a unit, enter a value, and press 'Convert'.")

category = st.selectbox("📌 Choose a Category", ["📏 Length", "⚖️ Weight", "⏳ Time"])

unit_options = {
    "📏 Length": {
        "🌍 Kilometers to Miles": ("Miles", 0.621371),
        "🛣️ Miles to Kilometers": ("Kilometers", 1.60934),
    },
    "⚖️ Weight": {
        "🏋️ Kilograms to Pounds": ("Pounds", 2.20462),
        "🥩 Pounds to Kilograms": ("Kilograms", 0.453592),
    },
    "⏳ Time": {
        "⏱️ Seconds to Minutes": ("Minutes", 1 / 60),
        "⌛ Minutes to Seconds": ("Seconds", 60),
        "⏳ Minutes to Hours": ("Hours", 1 / 60),
        "🕰️ Hours to Minutes": ("Minutes", 60),
        "🌞 Hours to Days": ("Days", 1 / 24),
        "🌙 Days to Hours": ("Hours", 24),
    }
}

unit = st.selectbox("🎯 Choose a Unit", list(unit_options[category].keys()))
value = st.text_input("✍️ Enter the value to convert", "", key="value_input")

def convert_units(value, unit_data):
    try:
        value = float(value)  
        return value * unit_data[1], unit_data[0]  
    except ValueError:
        return None, None  

if st.button("🔁 Convert"):
    if value:
        try:
            value_float = float(value)
            if value_float == 0:
                st.info("ℹ️ 0 remains 0 in all conversions.")
            else:
                result, converted_unit = convert_units(value, unit_options[category][unit])
                st.success(f"✅ {value} converted to **{result:.4f} {converted_unit}**")
        except ValueError:
            st.error("❌ Invalid input! Please enter a numeric value.")
    else:
        st.warning("⚠️ Please enter a value to convert.")
