import streamlit as st
import pandas as pd
import numpy as np
import os
import streamlit_authenticator as stauth
import yaml

# Import the YAML file into script:
from yaml.loader import SafeLoader
with open('./credentials.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

# Create the authenticator object:
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

filepath = os.path.abspath("passport_applications.csv")

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

if __name__ == "__main__":
    authenticator.login(key='Login', location='main')
    
    if st.session_state['authentication_status']:
        authenticator.logout('Logout', 'main')
        st.write(f'Welcome *{st.session_state["name"]}*')
        st.write(st.session_state["roles"])

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
        # Initialize roles in session state
        if "roles" not in st.session_state:
            st.session_state["roles"] = [{0: "viewer"}]  # Default role is viewer

        if "editor" in st.session_state["roles"]:
            redact_columns = entities_to_extract
        elif len(st.session_state["roles"]) == 1 and "viewer" in st.session_state["roles"]:
            redact_columns = default_entity_types[2:]
        else:
            # If role is undefined, show an error
            st.error("Invalid role detected. Please check session state.")
            redact_columns = []

        # Redact selected columns in the DataFrame
        redacted_df = df.copy()
        for col in redact_columns:
            if col in redacted_df.columns:
                redacted_df[col] = "-"

        # Display the redacted DataFrame
        st.write(redacted_df)

        csv = convert_df(redacted_df)

        st.download_button(
            "Press to Download",
            csv,
            "redacted_applications.csv",
            "text/csv",
            key='download-csv'
        )
    elif st.session_state['authentication_status'] == False:
        st.error('Username/password is incorrect')
    elif st.session_state['authentication_status'] == None:
        st.warning('Please enter your username and password')