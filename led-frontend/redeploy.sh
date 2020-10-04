sudo docker build -t lsac-frontend .
sudo docker run -d --restart always -p 80:80 lsac-frontend
