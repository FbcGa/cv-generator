from __future__ import annotations

import json
from pathlib import Path
from flask import Flask, Response, render_template
from weasyprint import HTML

root_folder = Path(__file__).resolve().parent
data_path = root_folder / "data" / "cv_data.json"
templates_folder = root_folder / "templates"
static_folder = root_folder / "static"

def load_cv() -> dict:
    with data_path.open(encoding="utf-8") as f:
        return json.load(f)


def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=templates_folder,
        static_folder=static_folder,
        static_url_path="/static",
    )

    @app.route("/")
    def index():
        return render_template("cv.html", cv=load_cv())

    @app.route("/cv.pdf")
    def cv_pdf():
        cv = load_cv()
        html = render_template("cv.html", cv=cv)
        base_url = static_folder.resolve().as_uri() + "/"
        pdf_bytes = HTML(string=html, base_url=base_url).write_pdf()
        return Response(
            pdf_bytes,
            mimetype="application/pdf",
            headers={
                "Content-Disposition": 'inline; filename="fabricio_alipazaga.pdf"',
            },
        )

    @app.route("/health")
    def health():
        return {"status": "ok"}

    return app


app = create_app()

if __name__ == "__main__":
    app.config["DEBUG"] = True
