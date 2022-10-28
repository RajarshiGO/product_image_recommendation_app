import numpy as np
import streamlit as st
import os
from PIL import Image
import requests
from annoy import AnnoyIndex
from tensorflow import keras
import pickle as pkl
import albumentations as albu
from azure.storage.blob import BlobServiceClient
from azure.storage.blob import StorageStreamDownloader
import io
blob_service = BlobServiceClient(account_name="apprecommendation", account_url = "https://apprecommendation.blob.core.windows.net", credential = "?sv=2021-06-08&ss=b&srt=sco&sp=rltf&se=2023-04-12T18:55:28Z&st=2022-10-15T11:02:28Z&spr=https&sig=LokyJVDsh6y5ka79oPh25Q0geOaD6GDjk0JDiY4qzSE%3D")
source_container_client = blob_service.get_container_client("images")
t = AnnoyIndex(128, 'euclidean')
t.load("nearest_neighbor.ann")
model = model = keras.models.load_model('model')
file_list = open("files.pkl", "rb")
files = pkl.load(file_list)
preprocess = albu.Compose([
    albu.CLAHE(p=1),
    albu.ToGray(p=1),
])
def get_recommendations(image):
    im = Image.open(image)
    im = im.convert('RGB')
    im = im.resize((256, 256))
    im = np.array(im)
    im = preprocess(image = im)
    im = np.expand_dims(im['image']/255, axis=0)
    out_vec = np.squeeze(model(im))
    out_vec = out_vec/np.linalg.norm(out_vec)
    indexes = t.get_nns_by_vector(out_vec, 5)
    return indexes


st.title("Product Recommendation System")
UPLOAD_FOLDER = "uploads"
file = st.file_uploader(
    "Please provide an image of the product to generate recommendations", type=["png", "jpg", "jpeg"])
if file is not None:
    display_image = Image.open(file)
    st.image(display_image)
    indexes = get_recommendations(file)
    st.write("Here are our top 5 recommendations.")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        with io.BytesIO() as image:
            source_container_client.download_blob(files[indexes[0]].lstrip("./")).download_to_stream(image)
            st.image(image)
    with col2:
        with io.BytesIO() as image:
            source_container_client.download_blob(files[indexes[1]].lstrip("./")).download_to_stream(image)
            st.image(image)
    with col3:
        with io.BytesIO() as image:
            source_container_client.download_blob(files[indexes[2]].lstrip("./")).download_to_stream(image)
            st.image(image)
    with col4:
        with io.BytesIO() as image:
            source_container_client.download_blob(files[indexes[3]].lstrip("./")).download_to_stream(image)
            st.image(image)
    with col5:
        with io.BytesIO() as image:
            source_container_client.download_blob(files[indexes[4]].lstrip("./")).download_to_stream(image)
            st.image(image)
    # directory_list = os.listdir(UPLOAD_FOLDER)
    # if(len(directory_list)!=0):
    #     for name in directory_list:
    #         os.remove(os.path.join(UPLOAD_FOLDER, name))
    # with open(os.path.join(UPLOAD_FOLDER, file.name), 'wb') as f:
    #         f.write(file.getbuffer())

st.markdown("<h5 style='text-align: center; color: white;'>OR</h5>",
            unsafe_allow_html=True)
url = st.text_input('Provide an URL of a product image', placeholder='https:// PNG, JPG')
if (url != ""):
    
    try:
        download = requests.get(url, allow_redirects=True)
        directory_list = os.listdir(UPLOAD_FOLDER)
        if(len(directory_list) !=0):
            for name in directory_list:
                os.remove(os.path.join(UPLOAD_FOLDER, name))
        open(f'{UPLOAD_FOLDER}/image.jpg', 'wb').write(download.content)
        st.image(f'{UPLOAD_FOLDER}/image.jpg')
        indexes = get_recommendations(f'{UPLOAD_FOLDER}/image.jpg')
        st.write("Here are our top 5 recommendations.")
        col1, col2, col3, col4, col5 = st.columns(5)
    
        with col1:
            with io.BytesIO() as image:
                source_container_client.download_blob(files[indexes[0]].lstrip("./")).download_to_stream(image)
                st.image(image)
        with col2:
            with io.BytesIO() as image:
                source_container_client.download_blob(files[indexes[1]].lstrip("./")).download_to_stream(image)
                st.image(image)
        with col3:
            with io.BytesIO() as image:
                source_container_client.download_blob(files[indexes[2]].lstrip("./")).download_to_stream(image)
                st.image(image)
        with col4:
            with io.BytesIO() as image:
                source_container_client.download_blob(files[indexes[3]].lstrip("./")).download_to_stream(image)
                st.image(image)
        with col5:
            with io.BytesIO() as image:
                source_container_client.download_blob(files[indexes[4]].lstrip("./")).download_to_stream(image)
                st.image(image)
    except:
        st.write("ERROR 404: File not found. Please try again or provide another URL")
