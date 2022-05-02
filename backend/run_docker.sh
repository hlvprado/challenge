docker build -t helder_backend .
docker run -p 5000:5000 --name helder_backend helder_backend
# docker run -d -p 5000:5000 --name helder_backend helder_backend
