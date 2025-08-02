import streamlit as st
import requests
import json

st.set_page_config(
    page_title="ContractMe",
    page_icon="🤖",
    layout="wide"
)

st.markdown(
        """
        <style>
        .stButton>button {
            background-color: #A9D3FF;
            color: black;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            display: block;
            margin: 0 auto;
        }
        
        .stButton>button:hover {
            background-color: #8BC4FF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def center_text(text, size='h1'):
    """A simple function to center text using markdown."""
    st.markdown(f"<{size} style='text-align: center;color:black'>{text}</{size}>", unsafe_allow_html=True)

def send_fastapi_request(data):
    """Send POST request to FastAPI endpoint"""
    try:
        # Replace with your FastAPI server URL
        fastapi_url = "http://localhost:8000/upload"  # Adjust this URL
        
        response = requests.post(
            fastapi_url,
            json=data,
            headers={"Content-Type": "application/json"}
        )
        
        if response.status_code == 200:
            st.success("Request sent successfully!")
            return response.json()
        else:
            st.error(f"Error: {response.status_code} - {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("Could not connect to FastAPI server. Make sure it's running on http://localhost:8000")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

center_text("ContractMe", size='h1')

# File uploader
uploaded_file = st.file_uploader("Upload your document", type=['pdf', 'docx', 'txt'])

# Centered button using Streamlit
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Process Document", key="process_button"):
        if uploaded_file is not None:
            # Prepare data to send to FastAPI
            file_data = {
                "filename": uploaded_file.name,
                "file_type": uploaded_file.type,
                "file_size": uploaded_file.size,
                "content": uploaded_file.read().decode('utf-8') if uploaded_file.type == 'text/plain' else "Binary file content"
            }
            
            # Send request to FastAPI
            result = send_fastapi_request(file_data)
            
            if result:
                st.json(result)  # Display the response from FastAPI
        else:
            st.warning("Please upload a file first!")

# Display uploaded file info
if uploaded_file is not None:
    st.info(f"Uploaded: {uploaded_file.name} ({uploaded_file.size} bytes)")









