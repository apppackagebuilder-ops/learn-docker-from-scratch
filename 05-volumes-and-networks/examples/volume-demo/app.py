from pathlib import Path

storage_dir = Path('/data')
storage_dir.mkdir(parents=True, exist_ok=True)
file_path = storage_dir / 'message.txt'

existing = file_path.read_text().strip() if file_path.exists() else ''
new_message = 'Docker volumes keep this file even if the container is removed.\n'
file_path.write_text(existing + new_message)

print(file_path.read_text())
