
# Image similarity based E-commerce recommendation engine

![demo](demo.gif)
This is a image similarity based search engine that is intended to ne used as a recommendation system in E-commerce platforms to recommend products similar to the items that the customer has already viewed. The entire has been implemented on the Amazon product images dataset published online by [Amazon-Berkeley](https://amazon-berkeley-objects.s3.amazonaws.com/index.html). A pre-trained [VGG16](https://keras.io/api/applications/vgg/) model available in keras-tensorflow is used as a feature extractor to form feature vector of each image in the database and then for a new image, the corresponding feature vector is compared with every feature vector in the database to find potential matches. Considering the massive size of the dataset, the conventional Nearest Neighbor Search algorithm becomes very slow in real time and therefore, we have used approximate nearest neighbor search algorithm which is conveniently implemented in [Spotify/Annoy](https://github.com/spotify/annoy). The entire image database is hosted in [Microsoft Azure](https://azure.microsoft.com/en-in/) storage service since it cannot be hosted locally in the server owing to its size and the web app makes API calls to this service using the [Azure python API](https://learn.microsoft.com/en-us/azure/developer/python/sdk/azure-sdk-overview) to retrieve the recommended images.

For detailed step by step explanation, check out the ```notebook.ipynb``` file.

The recommendation system has been hosted online as a web application with Streamlit and can be accessed [here](https://rajarshigo-product-image-recommendation-app-app-k1n5ko.streamlitapp.com/). The web application is deployed as docker container with [nginx](https://www.nginx.com/) as reverse proxy.

## Run locally with docker
A docker image of the application is published on docker-hub for convenience and can be used to test the application locally. However, if you want to make additional tweaks to suit your own application then you can follow the instructions in the next section to run locally without docker.
1. Install docker using your distribution's package manager or follow the instructions on the official [website.](https://docs.docker.com/engine/install/)
2. Open a terminal and pull the image from docker-hub using the following command.
   
   ```docker pull rajarshi13g/image-recommendation```
3. Run a container using the pulled image and also bind the port 8080 with the container.
   
   ```docker run -p8080:80 rajarshi13g/image-recommendation```
4. Open a browser window and browse to this address ```localhost:8080```.

## Run locally without docker
1. Clone this repo.
   
   ```git clone https://github.com/RajarshiGO/product_image_recommendation_app```
2. Open a termial and change the working directory to the cloned repository.
   
   ```cd product_image_recommendation_app```
3. Install the dependecies through ```pip```. Make sure to install ```pip``` beforehand.
   
   ```pip install -r requirements.txt```
4. Type the command below to launch the app.
   
   ```streamlit run app.py```
