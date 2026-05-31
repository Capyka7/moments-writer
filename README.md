# moments-writer

> AI-powered WeChat Moments (朋友圈) copy generator — 用 AI 生成朋友圈文案，支持多种风格和场景。

[![Python](https://img.shields.io/badge/python-3.8+-blue.svg)]()
[![License](https://img.shields.io/badge/license-MIT-green.svg)]()
[![DeepSeek](https://img.shields.io/badge/powered%20by-DeepSeek-orange.svg)]()

## ✨ 功能

- 🎨 **多种风格**：文艺、搞笑、励志、日常、美食、旅行、情感、沙雕
- 📝 **一键生成**：输入主题或心情，自动生成朋友圈文案
- 🏷️ **智能标签**：自动添加热门话题标签
- 💾 **收藏管理**：保存喜欢的文案，随时查看
- 🌐 **Web 界面**：浏览器打开即用，清爽美观
- 🖥️ **命令行**：不想开浏览器？终端也能用
- 🔌 **API 接入**：支持 DeepSeek、OpenAI 等兼容接口

## 🚀 快速开始

```bash
# 1. 安装
pip install moments-writer

# 2. 设置 API Key
export DEEPSEEK_API_KEY="sk-your-key-here"

# 3. 生成一条朋友圈
moments "今天去海边了，天气很好"

# 4. 启动 Web 界面
moments-web
```

## 📦 安装

```bash
# 从源码安装
git clone https://github.com/yourname/moments-writer.git
cd moments-writer
pip install -e .

# 或直接运行
python moments_writer/cli.py "今天心情不错"
```

## 💻 命令行用法

```bash
# 指定风格
moments "发工资了" --style funny

# 指定数量
moments "周末爬山" --count 3

# 指定长度
moments "深夜emo" --style emotional --max-length 80

# 带标签
moments "新买了个相机" --with-tags
```

## 🌐 Web 界面

```bash
moments-web
# 浏览器打开 http://localhost:5566
```

界面截图：

```
┌─────────────────────────────────────┐
│  📝 朋友圈文案生成器                 │
│                                     │
│  今天想发什么？                      │
│  ┌─────────────────────────────┐   │
│  │ 今天去海边了，天气很好      │   │
│  └─────────────────────────────┘   │
│                                     │
│  风格：[文艺] 字数：[短] 标签：[✓] │
│                                     │
│  [ 🚀 生成文案 ]                    │
│                                     │
│  ┌─ 结果 ────────────────────────┐ │
│  │                               │ │
│  │  海风是咸的，落日是圆的。     │ │
│  │  今天把心事都交给海浪了🌊    │ │
│  │                               │ │
│  │  #海边日记 #治愈系 #周末      │ │
│  │                               │ │
│  │  [📋 复制] [💾 收藏]          │ │
│  └───────────────────────────────┘ │
└─────────────────────────────────────┘
```

## 📝 支持的风格

| 风格 | 说明 | 示例 |
|------|------|------|
| `casual` | 日常唠嗑 | 今天吃撑了，嗝～ |
| `aesthetic` | 文艺唯美 | 落日归山海，山海藏深意 |
| `funny` | 搞笑沙雕 | 我的体重它做错了什么… |
| `inspirational` | 励志正能量 | 每一天都是新的开始 ✨ |
| `foodie` | 美食探店 | 这家店的蛋糕绝了！ |
| `travel` | 旅行记录 | 总要去趟XX吧，吹吹… |
| `emotional` | 情感抒发 | 有些人，见一面就够… |
| `minimal` | 极简冷淡 | 今日无事。 |

## 🔧 配置

创建 `~/.moments-writer.json`：

```json
{
  "api_key": "sk-xxx",
  "api_base": "https://api.deepseek.com",
  "model": "deepseek-chat",
  "default_style": "casual",
  "default_count": 3,
  "with_tags": true
}
```

## 🏗️ 项目结构

```
moments-writer/
├── moments_writer/
│   ├── __init__.py        # 包入口
│   ├── cli.py             # 命令行工具
│   ├── web.py             # Web 界面 (Flask)
│   ├── generator.py       # 文案生成核心
│   ├── styles.py          # 风格管理和模板
│   ├── storage.py         # 收藏管理 (SQLite)
│   └── config.py          # 配置管理
├── templates/
│   └── index.html         # Web 页面
├── tests/
│   └── test_generator.py
├── examples/
│   └── usage.py
├── setup.py
├── requirements.txt
├── LICENSE
└── README.md
```

## 🤝 贡献

欢迎提 Issue 和 PR！一起让这个工具更好用。

## 📄 许可证

MIT License

---

<p align="center">Made with ❤️ 朋友圈文案自由 ✨</p>
