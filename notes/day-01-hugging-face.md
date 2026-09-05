# Day 1：从 Hugging Face 开始认识大模型

更新日期：2026-09-05

## 今天的目标

完成本章后，应当能够：

1. 说清 Hugging Face Hub、Transformers、Datasets 和 Spaces 分别是什么。
2. 看懂一个模型页面最重要的信息。
3. 使用 `pipeline` 下载并运行一个小型开源语言模型。
4. 理解 tokenizer、model、推理、权重和缓存的基本关系。
5. 知道哪些内容暂时不需要学习。

本阶段不训练模型。先建立完整的使用体验，再逐渐深入 Transformer 和训练原理。

## 1. Hugging Face 是什么

可以先把 Hugging Face 理解成 AI 领域的 GitHub 加工具箱：

- **Hub**：托管带版本记录的模型、数据集和演示应用。
- **Transformers**：用统一 Python API 加载和运行 Transformer 模型。
- **Datasets**：下载、查看和处理数据集。
- **Tokenizers**：把文本转换为模型能够处理的 token ID。
- **Spaces**：托管 Gradio、Docker 或静态 HTML 构建的 AI 演示应用。
- **huggingface_hub**：通过 Python 或命令行下载、上传和管理 Hub 文件。

Hub 上主要有三种仓库：

- Model：配置、tokenizer、权重、模型说明和评测信息。
- Dataset：训练或评测数据及其说明。
- Space：可以在线运行的 AI 应用。

它们和 GitHub 仓库相似，但对模型权重、大文件、数据集预览和在线推理做了专门支持。

## 2. 如何阅读模型页面

打开一个模型页面时，优先检查以下内容：

1. **作者是否可信**：优先选择模型官方组织的账号。
2. **Model Card**：用途、语言、输入输出、局限和示例。
3. **License**：是否允许商业使用、修改与分发。
4. **Task**：文本生成、Embedding、分类还是其他任务。
5. **参数规模**：如 0.6B、7B、32B。规模越大，通常占用的内存和计算量越高。
6. **模型类型**：Base 模型用于继续训练；Instruct/Chat 模型适合直接对话。
7. **文件格式**：`safetensors` 常用于 Transformers；`GGUF` 常用于 llama.cpp。
8. **Gated model**：有些模型必须登录并接受许可证才能下载。

不要只看下载量或榜单分数。一个模型是否适合，还取决于语言、上下文长度、硬件、许可证和具体任务。

## 3. 第一个实践：运行本地模型

本实验选择 `Qwen/Qwen3-0.6B`：模型较小、支持中文、采用 Apache-2.0 许可证，并且不需要先接受额外的 gated model 协议。小模型适合学习 API，但输出质量不能代表大型模型。

### 3.1 创建环境

在仓库根目录执行：

```bash
cd /Users/laichao/workspace/ai-learning-lab
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install torch transformers accelerate safetensors
```

第一次运行会从 Hugging Face 下载模型并缓存到本机，因此需要联网并占用磁盘空间。后续运行通常直接读取缓存。

### 3.2 运行示例

```bash
python examples/01_hugging_face/quickstart.py
```

第一次运行时间较长是正常现象。程序将：

1. 根据仓库 ID 找到模型。
2. 下载配置、tokenizer 和权重。
3. 将对话套用为模型需要的 chat template。
4. 把文本编码为 token ID。
5. 执行推理，逐 token 生成结果。
6. 将 token ID 解码回文本。

### 3.3 修改并观察

依次修改示例程序中的参数：

- 将问题改成 C++、算法或日常问题。
- 把 `max_new_tokens` 从 `128` 改成 `32`，观察输出是否被截断。
- 分别设置固定随机种子与不同随机种子，观察采样结果。
- 打印 `pipe.tokenizer.tokenize("你好，Hugging Face")`，观察中英文分词结果。
- 打印 `pipe.tokenizer.apply_chat_template(messages, tokenize=False)`，观察聊天消息如何变成模型真正接收的文本。

## 4. 需要理解的关键对象

### Tokenizer

模型不能直接读取字符串。Tokenizer 会把文本切分并映射为整数 ID，也负责把输出 ID 还原成文本。

```text
字符串 → tokens → token IDs → 模型 → output IDs → 字符串
```

不同模型可能使用不同 tokenizer。同一段文字在不同模型上的 token 数可能不同，不能随意混用。

### Model

模型由网络结构和训练得到的权重组成。`from_pretrained()` 通常会读取：

- `config.json`：模型结构配置。
- tokenizer 文件：词表、规则和特殊 token。
- `*.safetensors`：模型权重。
- generation config：默认生成参数。

### Pipeline

`pipeline` 是高层封装，会连接预处理、模型推理和后处理。它适合入门和快速验证。之后为了理解底层，可以再改用 `AutoTokenizer`、`AutoModelForCausalLM` 和 `model.generate()`。

### Chat template

对模型来说，聊天最终仍是一串 token。`role` 和 `content` 会通过模型自带的 chat template 转换成带特殊控制 token 的文本。不同模型格式不同，因此应使用模型自带模板，而不是自行拼接字符串。

### 推理与训练

- **推理**：权重保持不变，根据输入生成输出。本章做的是推理。
- **微调**：在已有权重基础上继续训练，使模型适应特定任务。
- **预训练**：从大量数据训练基础模型，成本远高于个人入门实验。

## 5. Hugging Face 账号和命令行

公开模型通常可以匿名下载。以下场景需要账号和 Access Token：

- 下载 gated 或私有模型。
- 上传模型、数据集或 Space。
- 使用需要身份认证的托管服务。

创建账号后，可以安装并登录 CLI：

```bash
python -m pip install huggingface_hub
hf auth login
```

只给 Token 必要权限。Token 属于敏感凭据，不要写入代码、Markdown、Git 提交或截图。

查看某个仓库将下载哪些文件而不实际下载：

```bash
hf download Qwen/Qwen3-0.6B --include "*.json" --dry-run
```

下载单个文件：

```bash
hf download Qwen/Qwen3-0.6B config.json
```

Hugging Face 默认使用本地缓存。不要直接修改缓存中的文件；如需固定可重复版本，可以在代码中指定 `revision` 为 tag 或完整 commit hash。

## 6. 今天的阅读顺序

控制在 60～90 分钟，不需要一次读完整门课程：

1. [Hugging Face Hub 文档首页](https://huggingface.co/docs/hub/index)：认识 Models、Datasets、Spaces。
2. [LLM Course 第一章](https://huggingface.co/learn/llm-course/chapter1/1)：建立 Transformer 和任务类型的整体认识。
3. [Transformers Quickstart](https://huggingface.co/docs/transformers/quicktour)：重点看 `pipeline`、`AutoTokenizer` 和 `AutoModel`。
4. [Chat templates](https://huggingface.co/docs/transformers/chat_templating)：理解聊天消息如何转成 token 序列。
5. [Hub 下载指南](https://huggingface.co/docs/huggingface_hub/en/guides/download)：理解缓存、revision 和 CLI 下载。
6. [Spaces 概览](https://huggingface.co/docs/hub/main/spaces-overview)：只需知道如何发布在线 Demo，暂时不用实践。

## 7. 今日练习与验收

完成后在本文底部写下自己的答案：

- [ ] Hugging Face Hub 与 GitHub 有什么相同和不同？
- [ ] Model、Dataset、Space 分别解决什么问题？
- [ ] Base 模型和 Instruct 模型有什么区别？
- [ ] Tokenizer 为什么必须和模型匹配？
- [ ] `pipeline` 帮我们封装了哪些步骤？
- [ ] 模型下载到了哪里？第二次运行为什么更快？
- [ ] 运行并修改 `quickstart.py`，保存一次输出。

### 我的记录

```text
完成日期：
运行环境：
模型：Qwen/Qwen3-0.6B
首次加载耗时：
生成耗时：
主要发现：
仍有疑问：
```

## 8. 暂时不要做的事情

- 不要第一天就训练或微调模型。
- 不要下载超过机器承载能力的大模型。
- 不要同时学习多个 Agent/RAG 框架。
- 不要跳过 Model Card 和 License。
- 不要将 Hugging Face Token 或其他 API Key 提交到 Git。

下一步是在不依赖 `pipeline` 的情况下，显式使用 tokenizer 和 model 完成一次生成，并观察输入、输出张量的形状。

