import streamlit as st

st.set_page_config(page_title="Heygen Interactive Agent Test")

st.title("Test Heygen Interactive Agent")
st.write("If the script is working correctly, the Heygen avatar should appear in the bottom left corner.")

iframe_code = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
        }
        #heygen-streaming-embed {
            position: fixed;
            left: 20px;
            bottom: 20px;
            width: 400px;
            height: 400px;
            border-radius: 16px;
            border: 2px solid #fff;
            box-shadow: 0px 8px 24px rgba(0, 0, 0, 0.12);
            transition: all 0.3s ease-in-out;
            overflow: hidden;
        }
        #heygen-streaming-container {
            width: 100%;
            height: 100%;
        }
        #heygen-streaming-container iframe {
            width: 100%;
            height: 100%;
            border: none;
        }
    </style>
</head>
<body>
    <div id="heygen-streaming-embed">
        <div id="heygen-streaming-container">
            <iframe 
                src="https://labs.heygen.com/guest/streaming-embed?share=eyJxdWFsaXR5IjoiaGlnaCIsImF2YXRhck5hbWUiOiJCcnlhbl9GaXRuZXNzQ29hY2hfcHVibGlj%0D%0AIiwicHJldmlld0ltZyI6Imh0dHBzOi8vZmlsZXMyLmhleWdlbi5haS9hdmF0YXIvdjMvN2ZiZWY0%0D%0AZGQxZDY2NDFiYzg3NzdiMjZhNmFhYWM4NWVfNDU1ODAvcHJldmlld190YWxrXzEud2VicCIsIm5l%0D%0AZWRSZW1vdmVCYWNrZ3JvdW5kIjpmYWxzZSwia25vd2xlZGdlQmFzZUlkIjoiNzBhYmFhMjA3NjA4%0D%0ANGFhNzk1ZDhmYzE4YWZmZWI4ZTciLCJ1c2VybmFtZSI6IjIyMjJiMWY3Y2Y0MjQ0NDA4ZDg1ZDdk%0D%0AZGRkMzdiOTEyIn0%3D&inIFrame=1" 
                allow="microphone" 
                allowfullscreen>
            </iframe>
        </div>
    </div>
</body>
</html>
"""

st.components.v1.html(iframe_code, height=450, scrolling=False)
