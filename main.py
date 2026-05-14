import streamlit as st
from streamlit_webrtc import webrtc_streamer
import av
from pyzbar.pyzbar import decode

st.title("Quick Python Barcode Scanner")


def video_frame_callback(frame):
    img = frame.to_ndarray(format="bgr24")

    # Scan the frame for barcodes
    barcodes = decode(img)
    for barcode in barcodes:
        data = barcode.data.decode("utf-8")
        # Display the result on the terminal/log
        print(f"Scanned: {data}")
        # Note: To show data back on the UI in real-time
        # requires a bit more state handling.

    return av.VideoFrame.from_ndarray(img, format="bgr24")


webrtc_streamer(key="scanner", video_frame_callback=video_frame_callback)
