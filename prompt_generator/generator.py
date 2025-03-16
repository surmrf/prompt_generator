import random
from prompt_generator.utils import count_tokens


def generate_semantic_prompt(target_tokens: int, topic: str = "人工智能") -> str:
    """基于主题生成符合 token 长度的 prompt"""
    prompt_templates = [
        f"请详细介绍{topic}的发展历史及其对社会的影响。",
        f"在{topic}领域，有哪些关键技术？请详细说明。",
        f"未来十年，{topic}可能会有哪些突破？请预测并分析。",
        f"请结合实际案例，解释{topic}是如何应用在各行各业的。",
        f"在{topic}的研究中，存在哪些主要挑战？如何解决？",
    ]

    text = random.choice(prompt_templates)

    # 通过扩展或截断调整 token 数
    while count_tokens(text) < target_tokens:
        text += " 请详细说明。"  # 逐步扩展
    while count_tokens(text) > target_tokens:
        text = text[:-1]  # 逐步减少字符

    return text


def generate_dataset(
    size=100, token_range=(50, 500), topic="人工智能", output_file="data/prompts.json"
):
    """批量生成 Prompt 数据集"""
    dataset = []

    for _ in range(size):
        target_token_count = random.randint(*token_range)
        prompt = generate_semantic_prompt(target_token_count, topic)
        dataset.append({"prompt": prompt, "token_count": count_tokens(prompt)})

    # 保存为 JSON
    with open(output_file, "w", encoding="utf-8") as f:
        import json

        json.dump(dataset, f, ensure_ascii=False, indent=4)

    return dataset
