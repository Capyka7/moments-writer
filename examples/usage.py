"""
Usage examples for moments-writer.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from moments_writer import MomentsGenerator
from moments_writer.styles import STYLES, get_style_names


def example_list_styles():
    """List all available styles."""
    print("🎨 可用风格:")
    for sid, info in STYLES.items():
        print(f"  {sid:<14} {info['name']}")
        print(f"  {'':14} 示例: {info['examples'][0]}")
        print()


def example_generate():
    """Generate some copy."""
    gen = MomentsGenerator.from_config()

    if not gen.api_key:
        print("⚠️  请先设置 DEEPSEEK_API_KEY 环境变量")
        return

    print("=" * 40)
    print("📝 生成示例: 今天去了海边")
    print("=" * 40)

    results = gen.generate("今天去了海边，吹海风", style="aesthetic", count=2)

    for i, r in enumerate(results, 1):
        print(f"\n  ✏️  第{i}条:")
        print(f"     {r['text']}")
        if r['tags']:
            print(f"     {r['tags']}")

    print("\n" + "=" * 40)
    print("😄 生成示例: 发工资了")
    print("=" * 40)

    results = gen.generate("发工资了，开心", style="funny", count=2)

    for i, r in enumerate(results, 1):
        print(f"\n  ✏️  第{i}条:")
        print(f"     {r['text']}")
        if r['tags']:
            print(f"     {r['tags']}")


if __name__ == "__main__":
    example_list_styles()
    example_generate()
