Write-Host "Starting an Nginx container in the background..."
docker run -d -p 8080:80 --name cli-nginx-demo nginx
Write-Host ""
Write-Host "Showing running containers..."
docker ps
Write-Host ""
Write-Host "Showing logs..."
docker logs cli-nginx-demo
Write-Host ""
Write-Host "Inspecting the container..."
docker inspect cli-nginx-demo
Write-Host ""
Write-Host "When you are finished, run:"
Write-Host "docker stop cli-nginx-demo"
Write-Host "docker rm cli-nginx-demo"
