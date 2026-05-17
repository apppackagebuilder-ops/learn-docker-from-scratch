# Tagging Demo

## Purpose

This example gives you a tiny image so you can practice build, tag, and push commands.

## Build

```powershell
docker build -t registry-demo .
```

## Tag

```powershell
docker tag registry-demo your-dockerhub-name/registry-demo:1.0.0
```

## Push

```powershell
docker push your-dockerhub-name/registry-demo:1.0.0
```

## Expected Output

After the build, `docker images` should show `registry-demo`.

After tagging, `docker images` should also show the fully tagged image name.

If you are logged in and push successfully, the image should appear in your registry account.
