"""
Core generator — generates Moments copy using AI API.
"""

from .styles import get_style_info, STYLES
from .config import load_config


class MomentsGenerator:
    """Generate WeChat Moments copy with AI."""

    def __init__(self, api_key="", api_base="https://api.deepseek.com",
                 model="deepseek-chat"):
        self.api_key = api_key
        self.api_base = api_base
        self.model = model

    @classmethod
    def from_config(cls):
        config = load_config()
        return cls(
            api_key=config["api_key"],
            api_base=config["api_base"],
            model=config["model"],
        )

    def generate(self, topic, style="casual", count=3,
                 max_length=100, with_tags=True):
        """
        Generate Moments copy.

        Args:
            topic: What you want to post about
            style: Writing style (casual, aesthetic, funny, etc.)
            count: Number of copies to generate
            max_length: Max character length per copy
            with_tags: Whether to include hashtags

        Returns:
            List of dicts: [{"text": "...", "tags": "..."}, ...]
        """
        if not topic.strip():
            raise ValueError("Topic cannot be empty")

        style_info = get_style_info(style)

        tags_instruction = (
            "每句末尾加上 3-5 个相关的话题标签，用空格隔开，标签前加 #"
            if with_tags else "不需要加标签"
        )

        prompt = (
            f"{style_info['prompt']}\n\n"
            f"主题内容：{topic}\n"
            f"风格参考：{'；'.join(style_info['examples'][:2])}\n"
            f"要求：\n"
            f"1. 生成 {count} 条不同的朋友圈文案\n"
            f"2. 每条不超过 {max_length} 个字\n"
            f"3. 语言自然真实，像真人发的\n"
            f"4. {tags_instruction}\n"
            f"5. 不要用「亲爱的」「亲」等营销语气\n"
            f"6. 不要编号\n\n"
            f"每一条单独一行输出，不要多余说明。"
        )

        response = self._call_llm(prompt)
        return self._parse_response(response, with_tags)

    def _call_llm(self, prompt):
        """Call LLM API."""
        if not self.api_key:
            raise ValueError(
                "API key required. Set DEEPSEEK_API_KEY env var or "
                "create ~/.moments-writer.json"
            )

        from openai import OpenAI
        client = OpenAI(api_key=self.api_key, base_url=self.api_base)

        response = client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "你是一个朋友圈文案生成助手。只输出文案，不要多余内容。"},
                {"role": "user", "content": prompt},
            ],
            temperature=0.8,
            max_tokens=1024,
            timeout=30,
        )
        return response.choices[0].message.content

    def _parse_response(self, text, with_tags):
        """Parse LLM response into structured results."""
        results = []
        lines = [line.strip() for line in text.split("\n") if line.strip()]

        for line in lines:
            # Skip markdown formatting, numbers, or separator lines
            if line.startswith("```") or line.startswith("---") or line.startswith("==="):
                continue
            # Remove leading numbers like "1." or "1、"
            clean = line.lstrip("0123456789.、) ）")
            clean = clean.strip()
            if not clean:
                continue

            # Split tags from text
            tags = ""
            if "#" in clean and with_tags:
                # Find where tags start
                tag_start = clean.find("#")
                text_part = clean[:tag_start].strip()
                tag_part = clean[tag_start:].strip()
                if text_part:
                    results.append({"text": text_part, "tags": tag_part})
            else:
                results.append({"text": clean, "tags": ""})

        return results if results else [{"text": text, "tags": ""}]
