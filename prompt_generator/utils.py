# import tiktoken

# # 选择 OpenAI GPT-4 / GPT-3.5 的 tokenizer
# encoding = tiktoken.get_encoding("cl100k_base")


# def count_tokens(text: str) -> int:
#     """计算文本的 token 数"""
#     return len(encoding.encode(text))

import transformers

chat_tokenizer_dir = "./"

tokenizer = transformers.AutoTokenizer.from_pretrained(
    chat_tokenizer_dir, trust_remote_code=True
)


def count_tokens(text: str) -> int:
    """使用 DeepSeek R1 官方 tokenizer 计算 token 数"""

    return len(tokenizer.encode(text))
