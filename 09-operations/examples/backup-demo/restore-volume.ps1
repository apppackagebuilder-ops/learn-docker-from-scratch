param(
    [string]$VolumeName = 'course_pgdata',
    [string]$ArchiveName = 'volume-backup.tar'
)

docker run --rm -v ${VolumeName}:/target -v ${PWD}:/backup alpine sh -c "tar xf /backup/${ArchiveName} -C /target"
Write-Host "Restore completed for volume ${VolumeName}"
