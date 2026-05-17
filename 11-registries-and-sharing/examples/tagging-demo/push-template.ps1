param(
    [string]$DockerHubUser = "your-dockerhub-name",
    [string]$Version = "1.0.0"
)

Write-Host "Building the local image..."
docker build -t registry-demo .

Write-Host "Tagging the image for Docker Hub..."
docker tag registry-demo ${DockerHubUser}/registry-demo:${Version}

Write-Host "The next command would push the image after you log in:"
Write-Host "docker push ${DockerHubUser}/registry-demo:${Version}"
