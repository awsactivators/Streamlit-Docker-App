import streamlit as st

st.title("Welcome to ROI Calculator")
st.header("Get your cashflow")
initial = st.number_input("Initial investment in USD")
yr = st.number_input("how many years of investment in years")
growth = st.number_input("Increase in profit p.a. in %")
terminal_value = 0
current_val = initial
for year in range(int(yr)):
   current_val += growth * current_val
   terminal_value = current_val

# perform cashflow projections for the next 5 years
st.write(f'Initial investment of $ {initial} after {yr} years at a profit increase of {growth} per annum is $ {terminal_value}')