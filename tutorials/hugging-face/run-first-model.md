# 使用 Transformers 运行第一个本地模型

## 目标

运行 `Qwen/Qwen3-0.6B`，观察 tokenizer、chat template 和模型生成结果。该模型体积较小、支持中文并采用 Apache-2.0 许可证，适合走通入门流程。

## 创建环境

```bash
cd /Users/laichao/workspace/ai-learning-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch transformers accelerate safetensors
```

## 运行

```bash
python examples/01_hugging_face/quickstart.py
```

第一次运行会下载模型并写入 Hugging Face 本地缓存，需要联网、等待下载并预留磁盘空间。后续运行通常会复用缓存。

程序会依次完成：

1. 根据仓库 ID 定位模型。
2. 下载配置、tokenizer 和权重。
3. 应用模型的 chat template。
4. 把文本编码为 token ID。
5. 执行推理并生成新 token。
6. 把 token ID 解码为文本。

## 观察与修改

- 修改问题，测试 C++、算法和日常内容。
- 将 `max_new_tokens` 从 `128` 改成 `32`，观察截断。
- 修改 `temperature` 和 `top_p`，观察随机性。
- 查看 `tokenizer.tokenize()` 的中英文分词结果。
- 查看 `apply_chat_template(..., tokenize=False)` 渲染的真实输入。

## Hugging Face CLI

登录：

```bash
python -m pip install huggingface_hub
hf auth login
```

公开模型通常不需要登录。Gated、私有资源或上传操作需要 Access Token。不要把 Token 写入代码或提交到 Git。

在不下载权重的情况下查看部分待下载文件：

```bash
hf download Qwen/Qwen3-0.6B --include "*.json" --dry-run
```

下载单个配置文件：

```bash
hf download Qwen/Qwen3-0.6B config.json
```

默认下载结果进入 Hugging Face 缓存。不要直接修改缓存文件；需要固定版本时，应指定 tag 或完整 commit hash 作为 `revision`。

## 实验记录

在 `notes/` 下创建当天记录：

```text
完成日期：
运行环境：
模型：Qwen/Qwen3-0.6B
首次加载耗时：
生成耗时：
修改过的参数：
主要发现：
仍有疑问：
```

## 常见问题

### 第一次运行很慢

通常是在下载模型。确认网络和剩余磁盘空间，避免反复删除缓存。

### 内存不足

先关闭其他高内存程序；仍然不足时选择更小或量化后的模型。参数量与内存关系见[模型参数量、精度与资源需求](../../knowledge/llm/model-parameters.md)。

### 输出质量不理想

0.6B 是用于入门的小模型。先确认使用了正确的 Instruct/Chat 格式，再尝试更清晰的指令或更大模型。

## 官方资料

- [Qwen3-0.6B Model Card](https://huggingface.co/Qwen/Qwen3-0.6B)
- [Transformers Quickstart](https://huggingface.co/docs/transformers/quicktour)
- [Hugging Face 下载指南](https://huggingface.co/docs/huggingface_hub/en/guides/download)

