# Backup Demo

## Purpose

This example provides simple PowerShell scripts for backing up and restoring a Docker volume.

## Backup

```powershell
./backup-volume.ps1
```

## Restore

```powershell
./restore-volume.ps1
```

## Expected Output

The backup script should create a `volume-backup.tar` file in the current folder.

The restore script should unpack that archive back into the target volume.

## What You Are Learning

- One practical way to back up Docker-managed data
- One practical way to restore Docker-managed data
