FROM ubuntu
RUN mkdir /app
WORKDIR /app
RUN apt update && apt install -y nginx python3 python3-pip unzip
ADD ./requirements.txt .
RUN pip3 install -r requirements.txt
RUN mkdir uploads
COPY ./model ./model
ADD ./app.py ./
ADD ./files.pkl ./
ADD ./nearest_neighbor.ann ./
ADD ./script.sh ./
ADD ./nginx.conf /etc/nginx/nginx.conf
RUN chmod a+x script.sh
EXPOSE 80
CMD ["./script.sh"]


