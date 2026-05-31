"""
Configuration management for moments-writer.
"""

import json
import os
from pathlib import Path

CONFIG_FILE = Path.home() / ".moments-writer.json"

DEFAULT_CONFIG = {
    "api_key": "",
    "api_base": "https://api.deepseek.com",
    "model": "deepseek-chat",
    "default_style": "casual",
    "default_count": 3,
    "with_tags": True,
}


def load_config():
    """Load config from file, env vars override file."""
    config = dict(DEFAULT_CONFIG)

    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                file_config = json.load(f)
                config.update(file_config)
        except (json.JSONDecodeError, IOError):
            pass

    # Env override
    env_key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if env_key:
        config["api_key"] = env_key

    env_base = os.environ.get("DEEPSEEK_API_BASE") or os.environ.get("OPENAI_API_BASE")
    if env_base:
        config["api_base"] = env_base

    return config


def save_config(config):
    """Save config to file."""
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)


def get_api_key(config=None):
    """Get API key from anywhere possible."""
    if config and config.get("api_key"):
        return config["api_key"]
    key = os.environ.get("DEEPSEEK_API_KEY") or os.environ.get("OPENAI_API_KEY")
    if key:
        return key
    return ""
