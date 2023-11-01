import streamlit as st
from pytube import YouTube

st.set_page_config(
    page_title="Youtube Downloader",
    page_icon="white"
)

st.markdown(
    """
    <style>
        body{
            background-color:#FF0000;
            }
        .stTextInput{
        background-color:#d9d9d9;
        font-size:20px;
        }
    </style>
    """,
    unsafe_allow_html=True
)
st.title("MY Youtube Video Downloader")
url=st.chat_input("Enter the url of video",key="url")
auto_resolution=st.checkbox("Automation select Resolution")
resolution_option=["144p","240p","360","480p","720p","1080p"]
resolution_audio=["128k","48k","256k",]
resolution_a=st.selectbox("Select Audio Section",resolution_audio)
if not auto_resolution:
    resolution=st.selectbox("slecet video resolution",resolution_option)
if st.button("Download"):
    if url:
        try:
            yt=YouTube(url)
            if auto_resolution:
                stream=yt.streams.get_highest_resolution()
            else:
                if resolution_a=="144p":
                    stream=yt.streams.filter(res="144p",file_extension="mp3").first()
                elif resolution_a=="240p":
                    stream=yt.streams.filter(res="240p",file_extension="mp3").first()
                elif resolution_a=="360p":
                    stream=yt.streams.filter(res="360p",file_extension="mp3").first()
                if resolution_a=="144p":
                    stream=yt.streams.filter(res="144p",file_extension="mp3").first()


                elif resolution=="240p":
                    stream=yt.streams.filter(res="240p",file_extension="mp4").first()
                elif resolution=="360p":
                    stream=yt.streams.filter(res="360p",file_extension="mp4").first()
                elif resolution=="480p":
                    stream=yt.streams.filter(res="480p",file_extension="mp4").first()
                elif resolution=="720p":
                    stream=yt.streams.filter(res="720p",file_extension="mp4").first()
                elif resolution=="1080p":
                    stream=yt.streams.filter(res="1080p",file_extension="mp4").first()
            stream.download()
            st.success("Download SuccessFull")
        except Exception as e:
            st.error(f"Ann errot Accor:{e}")
       # else:
        #    st.warning("Please Enter a valid youtube url:")
