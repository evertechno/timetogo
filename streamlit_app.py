import streamlit as st
import time
from datetime import datetime, timedelta

# Timer end time (59 days from now)
end_time = datetime.now() + timedelta(days=59)

# Function to calculate the time remaining
def get_time_remaining():
    current_time = datetime.now()
    remaining_time = end_time - current_time

    days = remaining_time.days
    hours, remainder = divmod(remaining_time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    return days, hours, minutes, seconds

# Streamlit app layout
st.set_page_config(page_title="59-Day Timer", page_icon="⏰", layout="centered")

# CSS for custom styling
st.markdown(
    """
    <style>
    body {
        background-color: #f4f7fc;
        font-family: 'Arial', sans-serif;
    }
    .title {
        color: #2F4F4F;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-top: 50px;
    }
    .timer {
        font-size: 64px;
        font-weight: bold;
        color: #ff6347;
        text-align: center;
        padding: 20px;
        background-color: #fff;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.markdown('<div class="title">59-Day Timer</div>', unsafe_allow_html=True)

# Create a placeholder for the timer
timer_placeholder = st.empty()

# Keep updating the timer
while True:
    days, hours, minutes, seconds = get_time_remaining()

    # Display the time remaining with custom styling
    timer_placeholder.markdown(
        f'<div class="timer">{days} days, {hours:02}:{minutes:02}:{seconds:02}</div>',
        unsafe_allow_html=True
    )

    # Sleep for 1 second to update the timer
    time.sleep(1)

    # You can also add some animation or visual effect here if desired!
