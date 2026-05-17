# Images and Containers Example

## Purpose

This example uses Nginx and a small HTML file to help you see the difference between an image and a running container.

## Run

```powershell
./run-example.ps1
```

## Expected Output

You should see:

- A container named `static-demo` start successfully
- A message telling you to open `http://localhost:8083`
- The static HTML page in your browser

## What You Are Learning

- How one image becomes a running container
- How a bind mount can provide files to the container
- How port mapping exposes the app in a browser
