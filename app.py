import streamlit as st


def convert_temp(from_unit, to_unit, value):
    """
    Converts temperature between Celsius and Fahrenheit.

    Args:
        from_unit: The unit the temperature is currently in ("celsius" or "fahrenheit").
        to_unit: The unit to convert the temperature to ("celsius" or "fahrenheit").
        value: The temperature value to convert.

    Returns:
        The converted temperature value.
    """
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9 / 5) + 32
        else:
            return value  # Already in celsius
    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5 / 9
        else:
            return value  # Already in fahrenheit
    else:
        return "Invalid unit. Please use 'celsius' or 'fahrenheit'."


st.title("Temperature Converter")

# Unit selection dropdowns
from_unit = st.selectbox("From Unit", ("celsius", "fahrenheit"))
to_unit = st.selectbox("To Unit", ("celsius", "fahrenheit"))

# Input field for temperature value
temp_value = st.number_input(
    "Enter temperature value:",
    min_value=-100,
    max_value=100)

# Convert button
if st.button("Convert"):
    converted_value = convert_temp(from_unit, to_unit, temp_value)
    st.write(
        f"{temp_value} {from_unit} is equal to {converted_value:.2f} {to_unit}")
