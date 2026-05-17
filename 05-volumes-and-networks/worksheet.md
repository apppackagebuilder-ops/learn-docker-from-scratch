# Worksheet: Volumes and Networks

## Goal

Use this worksheet to confirm that you understand where container data lives and how containers talk to each other.

## Before You Start

- Review both flows in the lesson.
- If possible, run the volume demo and the network demo.

## Flow-1: Storage Check

1. Why are volumes useful?
2. What is the difference between a bind mount and a named volume?
3. What command creates a named volume?

## Flow-2: Networking Check

1. Why is `localhost` often wrong when one container needs to reach another?
2. What command creates a Docker network?
3. Why are service or container names useful on a shared network?

## Flow-3: Write the Commands

1. Write the command to create a volume called `app-data`.
2. Write the command to create a network called `app-net`.
3. Write the command that reads a file back from the `app-data` volume.

## Flow-4: Reflection

Write one short explanation of why important data should not live only inside a disposable container.
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
