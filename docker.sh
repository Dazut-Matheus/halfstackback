docker stop asa
docker rm asa
sudo docker build -t asa .
sudo docker run -d --net host --name asa asa