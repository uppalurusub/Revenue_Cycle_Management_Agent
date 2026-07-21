import streamlit as st

from api.revenue_cycle_api import process_claim
from components.request_form import render_request_form
from components.response_view import render_response
from components.sidebar import render_sidebar


st.set_page_config(
    page_title="Revenue Cycle Management",
    page_icon="🏥",
    layout="wide",
)

render_sidebar()

st.title("🏥 Revenue Cycle Management")
submitted, payload = render_request_form()

if submitted:
    with st.spinner("Processing Claim..."):
        response = process_claim(payload)

    if "error" in response:
        st.error(response["error"])
        if response.get("status_code"):
            st.caption(f"HTTP Status: {response['status_code']}")
    else:
        render_response(response)
