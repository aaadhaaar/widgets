import streamlit as st
import yfinance as yf

# Set the page title
st.set_page_config(page_title="Nifty Price Widget", layout="centered")

# Centered title
st.title("📈 Nifty 50 Live Price")

# Fetch Nifty data using yfinance
nifty_symbol = "^NSEI"  # Symbol for Nifty 50 index
nifty_data = yf.Ticker(nifty_symbol)

# Get the latest market price
try:
    nifty_price = nifty_data.history(period="1d")['Close'][-1]
    st.markdown(
        f"""
        <div style="text-align: center; 
                    border: 2px solid #1652f0; 
                    border-radius: 10px; 
                    padding: 20px; 
                    background-color: #f9f9f9;
                    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #1652f0;">₹{nifty_price:,.2f}</h2>
            <p style="font-size: 16px; color: #555;">Current Nifty 50 Price</p>
        </div>
        """,
        unsafe_allow_html=True
    )
except Exception as e:
    st.error("Unable to fetch Nifty 50 data. Please try again later.")