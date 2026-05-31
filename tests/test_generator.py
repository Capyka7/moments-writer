"""
Tests for moments-writer generator.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from moments_writer.generator import MomentsGenerator
from moments_writer.styles import STYLES, get_style_names


def test_parse_response_with_tags():
    gen = MomentsGenerator(api_key="test")
    text = "今天天气真好！#阳光 #好心情 #周末"
    results = gen._parse_response(text, with_tags=True)
    assert len(results) > 0
    assert "今天天气真好" in results[0]["text"]
    assert "好心情" in results[0]["tags"]


def test_parse_response_without_tags():
    gen = MomentsGenerator(api_key="test")
    text = "今天天气真好！"
    results = gen._parse_response(text, with_tags=False)
    assert len(results) > 0
    assert results[0]["tags"] == ""


def test_parse_multiline():
    gen = MomentsGenerator(api_key="test")
    text = "第一条文案\n第二条文案\n第三条文案"
    results = gen._parse_response(text, with_tags=False)
    assert len(results) >= 3


def test_styles_complete():
    assert len(STYLES) == 8
    names = get_style_names()
    assert "casual" in names
    assert "aesthetic" in names
    assert "funny" in names


def test_parse_removes_numbers():
    gen = MomentsGenerator(api_key="test")
    text = "1. 第一条文案\n2. 第二条文案"
    results = gen._parse_response(text, with_tags=False)
    for r in results:
        assert not r["text"].startswith("1")
        assert not r["text"].startswith("2")


if __name__ == "__main__":
    test_parse_response_with_tags()
    test_parse_response_without_tags()
    test_parse_multiline()
    test_styles_complete()
    test_parse_removes_numbers()
    print("✅ All tests passed!")
