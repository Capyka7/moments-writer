"""
Command-line interface for moments-writer.
"""

import argparse
import sys
from .generator import MomentsGenerator
from .styles import STYLES, get_style_names
from .storage import save_favorite, get_favorites
from .config import load_config


def main():
    parser = argparse.ArgumentParser(
        description="moments-writer — AI 朋友圈文案生成器",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("topic", nargs="?", help="今天想发什么？")
    parser.add_argument("--style", "-s", default="", choices=get_style_names() + [""],
                        help="文案风格")
    parser.add_argument("--count", "-c", type=int, default=0, help="生成条数")
    parser.add_argument("--max-length", "-m", type=int, default=0, help="最大字数")
    parser.add_argument("--no-tags", action="store_true", help="不加标签")
    parser.add_argument("--save", action="store_true", help="保存到收藏")
    parser.add_argument("--list", action="store_true", help="查看收藏列表")
    parser.add_argument("--styles", action="store_true", help="查看所有风格")
    parser.add_argument("--web", action="store_true", help="启动 Web 界面")

    args = parser.parse_args()

    config = load_config()

    # List styles
    if args.styles:
        print(f"\n{'风格ID':<16} 名称")
        print("-" * 30)
        for sid, info in STYLES.items():
            print(f"{sid:<16} {info['name']}")
        print()
        return 0

    # List favorites
    if args.list:
        favs = get_favorites()
        if not favs:
            print("暂无收藏")
            return 0
        print(f"\n📖 收藏列表 ({len(favs)} 条):\n")
        for f in favs:
            print(f"  [{f['id']}] {f['text']}")
            if f["tags"]:
                print(f"       {f['tags']}")
            print(f"       [{f['style']}] {f['created_at']}")
            print()
        return 0

    # Launch web
    if args.web:
        from .web import main as web_main
        return web_main()

    # Generate
    if not args.topic:
        parser.print_help()
        print("\n示例:")
        print("  moments '今天去海边了'")
        print("  moments '发工资了' --style funny")
        print("  moments '周末爬山' --count 3")
        print("  moments '深夜emo' --style emotional")
        print("  moments --styles")
        print("  moments --list")
        print("  moments --web")
        return 1

    generator = MomentsGenerator(
        api_key=config["api_key"],
        api_base=config["api_base"],
        model=config["model"],
    )

    if not generator.api_key:
        print("❌ 未设置 API Key")
        print("   请设置 DEEPSEEK_API_KEY 环境变量")
        print("   或创建 ~/.moments-writer.json 配置文件")
        return 1

    style = args.style or config.get("default_style", "casual")
    count = args.count or config.get("default_count", 3)
    max_length = args.max_length or 100
    with_tags = not args.no_tags

    # Show config in user config
    if "with_tags" in config:
        with_tags = config["with_tags"]

    print(f"\n🎨 风格: {STYLES.get(style, {}).get('name', style)}")
    print(f"📝 主题: {args.topic}")
    print(f"⏳ 正在生成...\n")

    try:
        results = generator.generate(
            topic=args.topic,
            style=style,
            count=count,
            max_length=max_length,
            with_tags=with_tags,
        )
    except Exception as e:
        print(f"❌ 生成失败: {e}")
        return 1

    for i, r in enumerate(results, 1):
        print(f"  {i}. {r['text']}")
        if r['tags']:
            print(f"     {r['tags']}")
        print()

    # Save all
    if args.save:
        for r in results:
            save_favorite(r["text"], r["tags"], style, args.topic)
        print(f"💾 已保存 {len(results)} 条到收藏")

    return 0


if __name__ == "__main__":
    sys.exit(main())
