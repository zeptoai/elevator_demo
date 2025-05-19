import streamlit as st
from PIL import Image, ImageDraw

st.title("エレベーター配置 提案デモアプリ")

uploaded_file = st.file_uploader("図面をアップロード", type=["png", "jpg", "jpeg"])

if uploaded_file:
    image = Image.open(uploaded_file)
    draw = ImageDraw.Draw(image)
    w, h = image.size
    draw.ellipse((w//2-10, h//2-10, w//2+10, h//2+10), fill='red')
    st.image(image, caption="提案位置（赤丸）")
    st.info("提案理由：中央に近く搬入動線が良好なため")
else:
    st.warning("図面ファイル（PNG/JPG）をアップロードしてください。")
