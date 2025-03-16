import argparse
from prompt_generator.generator import generate_dataset


def main():
    parser = argparse.ArgumentParser(description="生成指定 token 长度的 Prompt 数据集")
    parser.add_argument("--size", type=int, default=100, help="生成的 Prompt 数量")
    parser.add_argument("--min_tokens", type=int, default=50, help="最小 Token 数")
    parser.add_argument("--max_tokens", type=int, default=500, help="最大 Token 数")
    parser.add_argument("--topic", type=str, default="人工智能", help="Prompt 主题")
    parser.add_argument(
        "--output", type=str, default="data/prompts.json", help="输出文件"
    )

    args = parser.parse_args()

    generate_dataset(
        size=args.size,
        token_range=(args.min_tokens, args.max_tokens),
        topic=args.topic,
        output_file=args.output,
    )

    print(f"数据集已生成：{args.output}")


if __name__ == "__main__":
    main()
