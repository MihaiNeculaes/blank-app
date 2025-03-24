import streamlit as st

def calculate_spice(hdl, triglycerides, bmi):
    numerator = 600 * (hdl ** 0.185)
    denominator = (triglycerides ** 0.2) * (bmi ** 1.338)
    return numerator / denominator

st.title("SPICE Index Calculator")

st.markdown("""
This calculator estimates the **SPICE index (Single Point Insulin Sensitivity Estimator)** based on:

- HDL cholesterol (mg/dL)
- Triglycerides (mg/dL)
- BMI (kg/m²)

---
### 🧮 Formula:
All units must be in **mg/dL** for lipids and **kg/m²** for BMI.
""")

st.latex(r"""
\text{SPICE} = \frac{600 \times (\text{HDL})^{0.185}}{(\text{Triglycerides})^{0.2} \times (\text{BMI})^{1.338}}
""")

hdl = st.number_input("Enter HDL cholesterol (mg/dL)", min_value=0.0, step=0.00001, format="%.5f")
triglycerides = st.number_input("Enter Triglycerides (mg/dL)", min_value=0.0, step=0.00001, format="%.5f")
bmi = st.number_input("Enter BMI (kg/m²)", min_value=0.0, step=0.00001, format="%.5f")

if st.button("Calculate SPICE Index"):
    if hdl > 0 and triglycerides > 0 and bmi > 0:
        spice = calculate_spice(hdl, triglycerides, bmi)
        st.success(f"SPICE Index: {spice:.5f}")
    else:
        st.warning("Please enter all values greater than 0.")
