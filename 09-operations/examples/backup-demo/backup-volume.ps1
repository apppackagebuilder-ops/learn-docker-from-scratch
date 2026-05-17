param(
    [string]$VolumeName = 'course_pgdata',
    [string]$ArchiveName = 'volume-backup.tar'
)

docker run --rm -v ${VolumeName}:/source -v ${PWD}:/backup alpine sh -c "tar cf /backup/${ArchiveName} -C /source ."
Write-Host "Backup written to ${PWD}\${ArchiveName}"
