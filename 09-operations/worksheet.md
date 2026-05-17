# Worksheet: Operations

## Goal

Use this worksheet to confirm that you can check container health, read logs, protect data, and troubleshoot methodically.

## Before You Start

- Review the operations lesson.
- If possible, run the health-check example and inspect it yourself.

## Flow-1: Health and Logs

1. Why is a running container not always a healthy container?
2. What does a health check do?
3. What command shows container logs?
4. What command can follow new log lines as they appear?

## Flow-2: Resource and Data Safety

1. Why might you set memory or CPU limits?
2. Why is volume backup important?
3. Give one troubleshooting step for a container that exits immediately.

## Flow-3: Hands-On Check

1. Which URL opens the health endpoint in the example?
2. Which command shows low-level health status for the container?
3. What file should the backup flow create?

## Flow-4: Reflection

Why is a checklist better than random guessing when troubleshooting containers?
# Worksheet: Operations

## Part 1: Health and Logs

1. Why is a running container not always healthy?
2. What is a health check used for?
3. Why should apps log to standard output and standard error?

## Part 2: Limits and Data Safety

1. Why can resource limits be important?
2. Why should important Docker volumes be backed up?
3. What is one simple backup idea for a volume?

## Part 3: Troubleshooting

A web app is not reachable in the browser. List 4 things you should check.

A container exits immediately. List 3 possible reasons.

## Part 4: Practice

Run the health-check demo and inspect:

- Logs
- Health status
- Port behavior
