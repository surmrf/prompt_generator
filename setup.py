from setuptools import setup, find_packages

setup(
    name="prompt_generator",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["tiktoken"],
    entry_points={
        "console_scripts": [
            "generate-prompts = prompt_generator.main:main",
        ],
    },
)
