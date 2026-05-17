Write-Host "Checking Docker version..."
docker version
Write-Host ""
Write-Host "Checking Docker engine details..."
docker info
Write-Host ""
Write-Host "Running hello-world to verify containers work..."
docker run hello-world
Write-Host ""
Write-Host "Listing images..."
docker images
Write-Host ""
Write-Host "Listing all containers..."
docker ps -a
