from pathlib import Path


def build_clinic_demo(dist: Path, origin: str) -> None:
    source = Path(__file__).parent / 'clinic-prospects' / 'ravi-dental-care'
    target = dist / 'demos' / 'ravi-dental-care'
    target.mkdir(parents=True, exist_ok=True)
    html = (source / 'index.html').read_text()
    html = html.replace('{{CANONICAL}}', f'{origin}/demos/ravi-dental-care/')
    (target / 'index.html').write_text(html)
    (target / 'style.css').write_bytes((source / 'style.css').read_bytes())
