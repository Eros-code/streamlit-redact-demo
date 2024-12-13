import streamlit as st
import pandas as pd
import numpy as np

if __name__ == "__main__":
    st.write("""
             # Streamlit redact dummy passport application data
             *This page demonstrates how data can be redacted in streamlit*""")

    
    ## add things to the sidebar

    # # Add a selectbox to the sidebar:

    default_entity_types = [
    "application_id",
    "application_reference",
    "forename", 
    "surname",
    "passport_number",
    "email_address", 
    "age"
    ]

    entities_to_extract = st.sidebar.multiselect(
        "Select PII types to redact", default_entity_types
    )