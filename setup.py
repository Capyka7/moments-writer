from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="moments-writer",
    version="0.1.0",
    description="AI-powered WeChat Moments copy generator / 朋友圈文案生成器",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="moments-writer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "openai>=1.0",
        "flask>=3.0",
        "requests>=2.31",
    ],
    entry_points={
        "console_scripts": [
            "moments=moments_writer.cli:main",
            "moments-web=moments_writer.web:main",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing :: Linguistic",
    ],
)
