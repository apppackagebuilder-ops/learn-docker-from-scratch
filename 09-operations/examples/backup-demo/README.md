# Backup Demo

## Goal

This example provides simple PowerShell scripts for backing up and restoring a Docker volume.

## Pre-requisites

- Docker Desktop running
- A Docker volume to back up

## Flow

### Step-1: Run the backup script

```powershell
./backup-volume.ps1
```

### Step-2: Verify the backup file was created

Look for:

- `volume-backup.tar`

### Step-3: Run the restore script when needed

```powershell
./restore-volume.ps1
```

## Expected Output

- The backup script should create `volume-backup.tar` in the current folder
- The restore script should unpack the archive into the target volume

## What You Are Learning

- One practical way to back up Docker-managed data
- One practical way to restore Docker-managed data
