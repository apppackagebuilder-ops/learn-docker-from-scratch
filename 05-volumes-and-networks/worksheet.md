# Worksheet: Volumes and Networks

## Part 1: Storage

1. Why can data disappear when a container is removed?
2. What is a named volume?
3. What is a bind mount?
4. When would you prefer a bind mount over a named volume?

## Part 2: Networking

1. Why do containers need networks?
2. Why is `localhost` often wrong when one container tries to reach another?
3. What is the benefit of a custom Docker network?

## Part 3: Practice

1. Create a volume named `practice-data`.
2. Write a file into it using one container.
3. Read the file from a second container.
4. Create a network named `practice-net`.
5. Start two containers on it.
6. Use one container to reach the other by name.

## Part 4: Reflection

Explain in your own words why a volume helps with databases and why a shared network helps with multi-container apps.
