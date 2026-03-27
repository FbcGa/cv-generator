from pathlib import Path

_root = Path(__file__).resolve().parent
_src = _root / "src"

_extra: set[str] = set()
if _src.is_dir():
    for pattern in ("templates/**/*.html", "static/**/*", "data/**/*"):
        for path in _src.glob(pattern):
            if path.is_file():
                _extra.add(str(path.resolve()))

bind = "0.0.0.0:5000"
workers = 1
reload = True
reload_engine = "poll"
reload_extra_files = sorted(_extra)
