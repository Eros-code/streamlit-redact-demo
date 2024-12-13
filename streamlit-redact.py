import streamlit as st
import pandas as pd
import numpy as np
import os

filepath = os.path.abspath("passport_applications.csv")

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

if __name__ == "__main__":
    st.write("""
             # Streamlit redact dummy passport application data
             *This page demonstrates how data can be redacted in streamlit*""")
    
    df = pd.read_csv(filepath)
    df = df.astype({'application_reference': 'str', 'passport_number': 'str'})

    
    ## add things to the sidebar

    # Add a selectbox to the sidebar:

    # the list of column names to add to the multi-selctor
    default_entity_types = list(df.columns)

    entities_to_extract = st.sidebar.multiselect(
        "Select PII types to redact", default_entity_types, key="redact_multiselect"
    )

    redact_columns = st.session_state.redact_multiselect
    for i in redact_columns:
        df[i] = '-'
    df

    csv = convert_df(df)

    st.download_button(
        "Press to Download",
        csv,
        "redacted_applications.csv",
        "text/csv",
        key='download-csv'
    )