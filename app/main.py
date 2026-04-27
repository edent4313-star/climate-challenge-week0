import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Climate Dashboard", layout="wide")

st.title("🌍 Climate Dashboard")

countries = ["Ethiopia", "Kenya", "Nigeria", "Egypt"]
years = list(range(2000, 2024))

rows = []
for country in countries:
    for year in years:
        rows.append({
            "Country": country,
            "Year": year,
            "T2M": np.random.uniform(20, 35),
            "PRECTOTCORR": np.random.uniform(10, 250),
            "RH2M": np.random.uniform(30, 90)
        })

df = pd.DataFrame(rows)

# Sidebar filters
st.sidebar.header("Filters")

selected_country = st.sidebar.multiselect(
    "Select Country",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Year Range",
    min_value=int(df["Year"].min()),
    max_value=int(df["Year"].max()),
    value=(2005, 2020)
)

variable = st.sidebar.selectbox(
    "Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)

filtered = df[
    (df["Country"].isin(selected_country)) &
    (df["Year"] >= year_range[0]) &
    (df["Year"] <= year_range[1])
]

st.subheader("Temperature Trend")
fig1 = px.line(filtered, x="Year", y="T2M", color="Country", markers=True)
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Precipitation Distribution")
fig2 = px.box(filtered, x="Country", y="PRECTOTCORR", color="Country")
st.plotly_chart(fig2, use_container_width=True)

st.subheader(f"{variable} by Year")
fig3 = px.bar(filtered, x="Year", y=variable, color="Country", barmode="group")
st.plotly_chart(fig3, use_container_width=True)
