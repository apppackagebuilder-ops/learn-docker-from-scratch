# Static HTML Content

## Goal

This folder contains the web page served by the Nginx container in the images-and-containers example.

## How It Is Used

The parent example mounts this folder into the Nginx container.

That means:

- Nginx provides the web server
- This folder provides the page content

## Flow

### Step-1: Start the parent example container

Run the parent example from the folder above this one.

### Step-2: Open the browser URL from the parent example

The mounted HTML files in this folder should be served by Nginx.

## Expected Output

When the example container is running, the browser should show:

- A heading that says `Hello from a Docker example`
- A paragraph explaining that port mapping works

## What You Are Learning

- Containers can serve files from mounted content
- The web server and the page content can come from different places
