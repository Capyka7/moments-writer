"""
Style definitions and templates for moments-writer.
"""

STYLES = {
    "casual": {
        "name": "日常唠嗑",
        "prompt": "写一条日常唠嗑风格的朋友圈，语气轻松随意，像在跟朋友聊天。可以带点生活的小确幸或小吐槽。",
        "examples": [
            "今天吃撑了，嗝～",
            "周末的正确打开方式：睡到自然醒，然后…继续躺着",
        ],
    },
    "aesthetic": {
        "name": "文艺唯美",
        "prompt": "写一条文艺风格的朋友圈，语言优美有意境，适合配风景或氛围感照片。可以用一些修辞和意象。",
        "examples": [
            "落日归山海，山海藏深意。",
            "风很温柔，花很浪漫，你很特别。",
        ],
    },
    "funny": {
        "name": "搞笑沙雕",
        "prompt": "写一条搞笑风格的朋友圈，幽默有趣，能让人看了笑出来。可以用自嘲、夸张、反讽等手法。",
        "examples": [
            "我的体重它做错了什么，你们要这样对它…",
            "钱包：我可能不是人，但你是真的狗。",
        ],
    },
    "inspirational": {
        "name": "励志正能量",
        "prompt": "写一条励志风格的朋友圈，给人正能量和鼓励。积极向上，但不鸡汤。",
        "examples": [
            "每一天都是新的开始，别让昨天的烦恼影响了今天的心情。",
            "你只管努力，剩下的交给时间。",
        ],
    },
    "foodie": {
        "name": "美食探店",
        "prompt": "写一条美食主题的朋友圈，描述食物色香味和用餐体验。让人看了有食欲。",
        "examples": [
            "这家店的蛋糕绝了！入口即化，甜而不腻。",
            "碳水带来的快乐，是任何东西都替代不了的。",
        ],
    },
    "travel": {
        "name": "旅行记录",
        "prompt": "写一条旅行风格的朋友圈，记录旅途中的风景和心情。有画面感，让人向往。",
        "examples": [
            "总要去趟重庆吧，吹吹嘉陵江的晚风。",
            "把烦恼丢进海里，把快乐装进相机。",
        ],
    },
    "emotional": {
        "name": "情感抒发",
        "prompt": "写一条情感风格的朋友圈，表达内心感受。可以关于思念、遗憾、感动、成长。细腻但不矫情。",
        "examples": [
            "有些人，见一面就够怀念一辈子。",
            "原来成长就是把哭声调成静音的过程。",
        ],
    },
    "minimal": {
        "name": "极简冷淡",
        "prompt": "写一条极简风格的朋友圈，字数很少，冷淡有态度。惜字如金，但意味深长。",
        "examples": [
            "今日无事。",
            "听雨。",
        ],
    },
}


def get_style_names():
    """Get list of available style IDs."""
    return list(STYLES.keys())


def get_style_info(style_id):
    """Get style info by ID."""
    return STYLES.get(style_id, STYLES["casual"])
