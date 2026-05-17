# Security, Multi-Stage Builds, and Image Optimization

## Goal of This Lesson

This lesson teaches a very important production mindset:

> A working image is not automatically a good image.

An image can work and still be:

- Too large
- Less secure than necessary
- Harder to maintain

So this lesson focuses on building images that are safer, smaller, and cleaner.

## Security Best Practices

Security can feel intimidating, so let us keep it practical.

You do not need to become a security expert on day one.
You only need to build good habits.

### 1. Use trusted base images

Start from images you trust.

That often means:

- Official images
- Well-reviewed internal base images
- Images with a clear maintenance story

Why?

Because your image inherits from its base.

### 2. Keep images updated

Old images can contain known vulnerabilities.

If you never rebuild or update, you may keep shipping outdated packages.

### 3. Do not bake secrets into images

Avoid storing secrets in:

- Dockerfiles
- Source code
- Image layers

Why is this dangerous?

Because images get shared, pushed, cached, and stored.
If a secret is baked into an image, it can spread farther than you expect.

### 4. Run as a non-root user

Many images default to root unless you change that.

Running as a non-root user reduces risk.
If an attacker breaks into the app, they should not automatically get full root power inside the container.

### 5. Install only what you need

Every extra package adds weight and possible attack surface.

Smaller images often mean:

- Fewer packages
- Fewer surprises
- Faster pulls
- Less to patch later

## What Is a Multi-Stage Build?

A multi-stage build uses more than one `FROM` line in the same Dockerfile.

That sounds strange at first, but the idea is simple.

Sometimes you need a big environment to build the app, but only a small environment to run it.

So you split those jobs into stages.

## Why Multi-Stage Builds Help

Imagine baking a cake.
You need mixing bowls, measuring cups, and tools while baking.
But you do not serve the cake with all those tools attached to it.

Multi-stage builds follow the same idea.

- Build stage: includes tools needed to assemble the app
- Runtime stage: includes only what is needed to run the app

## Example Idea

1. Build the app in a larger image
2. Produce the final app output
3. Copy only the necessary output into a smaller runtime image

This keeps the final image cleaner.

## Why This Is Better

Benefits include:

- Smaller final image
- Fewer tools in production
- Better security
- Faster deployment and download times

## Image Optimization Tips

Here are habits that usually improve image quality.

### Start from a smaller base image when appropriate

Smaller is not always better in every case, but it often helps.

### Use `.dockerignore`

Do not send unnecessary files into the build context.

### Copy dependency files before application code

This helps Docker reuse cached dependency layers when only app code changes.

### Keep layers purposeful

Do not add steps you do not really need.

### Avoid carrying build tools into production if they are no longer needed

This is exactly what multi-stage builds help solve.

## Example in This Lesson

This lesson includes a small Node.js app with a multi-stage Dockerfile.

Read it slowly and notice:

- Which stage installs dependencies
- Which stage becomes the final runtime image
- How the non-root user is created

## Common Beginner Mistakes

### Mistake 1: Using `latest` for everything without thinking

Version tags should be chosen intentionally.

### Mistake 2: Running as root by default forever

That is common, but not a great habit for production-minded images.

### Mistake 3: Putting build tools into the final runtime image

If the app does not need the build tools at runtime, leave them behind.

### Mistake 4: Copying the whole repository when only a few files are needed

That makes images and contexts larger than necessary.

## Mini Summary

Remember these principles:

1. Use trusted and maintained base images.
2. Keep images updated.
3. Do not store secrets in images.
4. Prefer non-root runtime users when practical.
5. Use multi-stage builds to keep final images smaller and cleaner.

## Quick Quiz

1. Why should you avoid putting secrets in images?
2. What is the main purpose of a multi-stage build?
3. Why is a smaller image often better?
4. Why run as a non-root user?
5. What is one caching benefit of copying dependency files before source code?

## Exercise

1. Read the example Dockerfile stage by stage.
2. Identify which stage builds the app.
3. Identify which stage runs the app.
4. Explain why the final image is smaller than a single-stage version.
5. Point out one security improvement used in the example.

## What Comes Next

Continue to [Docker Hub and Private Registries](../11-registries-and-sharing/registries-and-sharing.md).
