from pathlib import Path


if __name__ == '__main__':
    _header = '## Hi there 👋'
    repo_dir = Path(__file__).resolve().parent.parent
    base_dir = repo_dir / '_pages' / 'includes'
    _intro = (base_dir / 'intro.md').read_text().strip()
    _news = (base_dir / 'news.md').read_text().strip()
    _pub = (base_dir / 'pub.md').read_text().strip()
    _honers = (base_dir / 'honers.md').read_text().strip()
    _others = (base_dir / 'others.md').read_text().strip()
    with (repo_dir / 'README.md').open('w') as f:
        f.write(_header)
        f.write('\n\n')
        f.write(_intro)
        f.write('\n\n##')
        f.write(_others)
        f.write('\n\n##')
        f.write(_news)
        f.write('\n\n##')
        f.write(_pub)
