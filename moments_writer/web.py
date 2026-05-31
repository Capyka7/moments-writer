"""
Web interface for moments-writer (Flask).
"""

import sys
import os
from pathlib import Path

from flask import Flask, render_template, request, jsonify

from .generator import MomentsGenerator
from .styles import STYLES
from .storage import save_favorite, get_favorites, delete_favorite, search_favorites
from .config import load_config

# Add templates path
templates_dir = Path(__file__).parent.parent / "templates"
app = Flask(__name__, template_folder=str(templates_dir))
app.config["JSON_AS_ASCII"] = False


@app.route("/")
def index():
    styles = {sid: info["name"] for sid, info in STYLES.items()}
    return render_template("index.html", styles=styles)


@app.route("/api/generate", methods=["POST"])
def api_generate():
    data = request.get_json()
    topic = data.get("topic", "").strip()
    if not topic:
        return jsonify({"error": "请输入主题"}), 400

    style = data.get("style", "casual")
    count = int(data.get("count", 3))
    max_length = int(data.get("max_length", 100))
    with_tags = data.get("with_tags", True)
    api_key = data.get("api_key", "")
    api_base = data.get("api_base", "")
    model = data.get("model", "")

    config = load_config()
    generator = MomentsGenerator(
        api_key=api_key or config["api_key"],
        api_base=api_base or config["api_base"],
        model=model or config["model"],
    )

    if not generator.api_key:
        return jsonify({"error": "未设置 API Key"}), 400

    try:
        results = generator.generate(topic, style, count, max_length, with_tags)
        return jsonify({"results": results})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/save", methods=["POST"])
def api_save():
    data = request.get_json()
    save_favorite(
        text=data.get("text", ""),
        tags=data.get("tags", ""),
        style=data.get("style", "casual"),
        topic=data.get("topic", ""),
    )
    return jsonify({"status": "ok"})


@app.route("/api/favorites", methods=["GET"])
def api_favorites():
    keyword = request.args.get("q", "")
    if keyword:
        favs = search_favorites(keyword)
    else:
        favs = get_favorites()
    return jsonify({"favorites": favs})


@app.route("/api/favorites/<int:fav_id>", methods=["DELETE"])
def api_delete_favorite(fav_id):
    delete_favorite(fav_id)
    return jsonify({"status": "ok"})


def main():
    port = int(os.environ.get("PORT", 5566))
    print(f"\n  🌐 朋友圈文案生成器")
    print(f"  {'=' * 30}")
    print(f"  打开浏览器访问:")
    print(f"  http://localhost:{port}")
    print(f"\n  按 Ctrl+C 停止\n")
    app.run(host="0.0.0.0", port=port, debug=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
