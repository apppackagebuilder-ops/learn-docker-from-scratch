docker run -d --name static-demo -p 8083:80 -v ${PWD}/html:/usr/share/nginx/html:ro nginx
Write-Host "Open http://localhost:8083"
Write-Host "Stop with: docker stop static-demo"
Write-Host "Remove with: docker rm static-demo"
