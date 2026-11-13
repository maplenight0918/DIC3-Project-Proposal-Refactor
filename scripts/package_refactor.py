"""Package explicit project sources and deliverables; never include private/local data."""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'deliverables/refactor/submission.zip'
MANIFEST = ROOT / 'docs/refactor/submission-manifest.json'
ROOT_FILES = ['README.md', 'DESIGN.md', '.gitignore', '.openspec-version', 'requirements-docs.txt']
DIRS = ['assets', 'deliverables', 'docs', 'research', 'scripts', 'openspec', '.agents/skills']

def selected():
    files = [ROOT / name for name in ROOT_FILES]
    for directory in DIRS:
        files.extend(p for p in (ROOT / directory).rglob('*') if p.is_file()
                     and not p.is_symlink()
                     and '__pycache__' not in p.parts
                     and p.suffix not in ('.pyc', '.zip')
                     and p.name != 'review.png'
                     and p != MANIFEST)
    return sorted(set(files))

def main():
    files = selected()
    manifest = {'scope': 'Project sources, preserved original deliverables and DIC3 refactor; excludes .git, environments, raw data, class attachments and third-party full texts.',
                'files': {str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    MANIFEST.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n')
    with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as archive:
        for p in files + [MANIFEST]:
            archive.write(p, str(p.relative_to(ROOT)))
    with zipfile.ZipFile(OUTPUT) as archive:
        assert archive.testzip() is None
        for name, digest in manifest['files'].items():
            assert hashlib.sha256(archive.read(name)).hexdigest() == digest, name
    print(f'PASS: {len(files)+1} files packaged and hashes verified; {OUTPUT.stat().st_size:,} bytes; {OUTPUT}')

if __name__ == '__main__':
    main()
