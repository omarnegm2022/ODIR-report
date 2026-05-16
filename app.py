# =============================================================================
# Telecom Customer Churn Prediction - Streamlit Dashboard
# =============================================================================

import os
import streamlit as st
import pandas as pd
# import numpy as np
import plotly.express as px




# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Telecom Customer Churn Prediction Dashboard",
    page_icon="📊",
    # layout="wide",
)

# =========================================================
# STYLING
# =========================================================
# st.markdown("""
# <style>
# [data-testid="stAppViewContainer"] {
#     background: #262730;
#     color: white;
# }
# .kpi-card {
#     background: #262730;
# }
# .kpi-value {
#     font-weight: bold;
# }
# </style>
# """, unsafe_allow_html=True)

# =========================================================
# HELPERS
# =========================================================
csv_path = "./New_df.csv"

df = pd.read_csv(csv_path,index_col = False)
# =========================================================
# SIDEBAR
# =========================================================
st.sidebar.title("⚙ Single Patient info")
# st.subheader("Single Customer Prediction")
with st.form("predict_form"):
        revenue = st.number_input("Revenue", 0.0, 10000.0, 50.0)
        regularity = st.number_input("Regularity", 0.0, 31.0, 15.0)
        frequency = st.number_input("Frequency", 0.0, 100.0, 10.0)
        data_volume = st.number_input("Data Volume", 0.0, 100000.0, 1000.0)

        submit = st.form_submit_button("Predict")



# =========================================================
# HEADER
# =========================================================
st.title("📈 ODIR Analysis Dashboard")
st.caption("Executive dashboard for Eye disease monitoring")

# =========================================================
# KPI SECTION
# =========================================================
col1, col2, col3, col4 = st.columns(4)
# st.markdown("""
#     <style>
#     /* Target the second column */
#     [data-testid="column"]:nth-child(2) {
#         background-color: white;
#     }
#     </style>
# """, unsafe_allow_html=True)

Total_Records = len(df.index)
Total_Patients = len(set(df['ID']))
col1.metric("Total Patients", f"{Total_Patients:,}")
col2.metric("Normal Rate", f"{df['N'].sum() / Total_Records:,}")
col2.metric("Male Percentage ", f"{len(set(df[df['Patient Sex'] == 'Male']['ID'])) * 100/ Total_Patients:,}")
col2.metric("Female Percentage ", f"{len(set(df[df['Patient Sex'] == 'Female']['ID'])) * 100/ Total_Patients:,}")

# col3.metric("Retention", f"{len(df)-df['churn_prediction'].sum():,}")
# col4.metric("Avg Probability", f"{df['churn_probability'].mean():.2%}")

# =========================================================
# TABS
# =========================================================
tab1, tab2, tab3, tab4 = st.tabs([    "📊 Trends",    "🌍 Geography",    "🔍 Predict",    "📈 Model"])

# =========================================================
# TAB 1 - TRENDS
# =========================================================
with tab1:
    col1, col2, col3 = st.columns(3)

    with col1:
            fig = px.histogram(
            df,
            x="Patient Age",
            nbins=40,
            title="Age Distribution"
        )
            st.plotly_chart(fig, width='stretch')

    with col2:
            fig = px.pie(
            df,
            names="Primary Disease",
            title="Disease by Gender"
        )
            st.plotly_chart(fig, width='stretch')

    with col3:
            fig = px.scatter(
            df,
            x="Patient Age",
            y="Disease Count",
            title="Age vs Disease"
        )
            st.plotly_chart(fig, width='stretch')

# =========================================================
# TAB 2 - GEOGRAPHY (Senegal regions)
# =========================================================
with tab2:
    st.subheader("Churn risk by Senegal region")

      # agg = (
      #       df.groupby("region", as_index=False)
      #         .agg(
      #             customers=("churn_probability", "size"),
      #             avg_churn_prob=("churn_probability", "mean"),
      #             predicted_churn=("churn_prediction", "sum"),
      #         )
      #   )
      #   agg["region_norm"] = agg["region"].astype(str).str.strip().str.upper()

    c1, c2 = st.columns([2, 1])
    with c1:
           fig = px.bar(
                          df,
                          x='Patient Sex',
                          y='Disease Count',
                          color='Primary Disease',
                          facet_col='Age_Group',
                          barmode='group',
                          title='Disease Distribution by Age Group and Gender'
                          )
   
              
           st.plotly_chart(fig, width='stretch')

    with c2:
            fig = px.line( df,
                          x = 'Patient Age', y= 'Primary Disease',
                          title = "Disease trend by age")
            st.plotly_chart(fig, width = 'stretch')


# =========================================================
# TAB 3 - PREDICTION
# =========================================================



# =========================================================
# TAB 4 - MODEL
# =========================================================


st.caption("ODIR Dashboard")
