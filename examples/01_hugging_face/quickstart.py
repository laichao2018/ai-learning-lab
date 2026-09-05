"""Day 1: run a small language model from Hugging Face locally."""

import random

import torch
from transformers import pipeline


MODEL_ID = "Qwen/Qwen3-0.6B"


def main() -> None:
    seed = 42
    random.seed(seed)
    torch.manual_seed(seed)

    pipe = pipeline(
        task="text-generation",
        model=MODEL_ID,
        dtype="auto",
        device_map="auto",
    )

    messages = [
        {
            "role": "user",
            "content": "请用三点解释：大语言模型的推理和训练有什么区别？",
        }
    ]

    print("Tokens:")
    print(pipe.tokenizer.tokenize("你好，Hugging Face"))

    print("\nRendered chat template:")
    print(pipe.tokenizer.apply_chat_template(messages, tokenize=False))

    result = pipe(
        messages,
        max_new_tokens=128,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )

    print("\nModel output:")
    print(result[0]["generated_text"][-1]["content"])


if __name__ == "__main__":
    main()

