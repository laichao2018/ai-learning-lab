# Day 1：从 Hugging Face 开始认识大模型

更新日期：2026-09-05

## 学习目标

完成本阶段后，应当能够：

1. 说明 Hugging Face Hub、Transformers、Datasets、Tokenizers 和 Spaces 的作用。
2. 阅读 Model Card，判断模型是否适合自己的任务和设备。
3. 解释参数量、权重大小、量化精度和运行内存的区别。
4. 使用 Transformers 在本地运行一个小型开源语言模型。
5. 描述文本经过 tokenizer、模型推理再解码为文本的过程。
6. 解释 PyTorch、TensorFlow、Transformer 与 Hugging Face Transformers 的层级关系。

本阶段不训练模型。先走通模型发现、选择、下载和推理的完整流程。

## 学习顺序

### 0. 建立深度学习技术栈地图

阅读：[PyTorch、TensorFlow 与 Transformer 的关系](../knowledge/foundations/deep-learning-stack.md)

重点回答：

- 深度学习框架与模型架构有什么区别？
- Transformer 与 Hugging Face Transformers 为什么不是同一个东西？
- Tensor、Layer、Parameter、Gradient 和 Optimizer 分别是什么？

### 1. 认识 Hugging Face

阅读：[Hugging Face 生态与核心组件](../knowledge/hugging-face/ecosystem.md)

重点回答：

- Hub 与 GitHub 有什么相同和不同？
- Model、Dataset 和 Space 分别存放什么？
- Transformers 和 huggingface_hub 分别负责什么？

### 2. 学会挑选模型

阅读：[如何阅读 Model Card](../knowledge/hugging-face/reading-model-card.md)

重点回答：

- Base 和 Instruct 模型有什么区别？
- 为什么必须检查许可证和模型限制？
- 参数量是否等于模型质量？

### 3. 理解模型参数量

阅读：[模型参数量、精度与资源需求](../knowledge/llm/model-parameters.md)

重点回答：

- `7B` 中的 `B` 表示什么？
- 7B FP16 权重为什么约为 14 GB？
- 权重文件大小为什么不等于运行内存？
- Dense 和 MoE 模型的参数应该如何比较？

### 4. 理解一次推理

阅读：[Tokenizer、Chat Template 与推理](../knowledge/llm/tokenizer-and-inference.md)

重点回答：

- 模型为什么不能直接处理字符串？
- chat template 的用途是什么？
- 推理、微调和预训练有什么区别？

### 5. 完成第一次本地运行

实践：[使用 Transformers 运行 Qwen3-0.6B](../tutorials/hugging-face/run-first-model.md)

对应代码：[quickstart.py](../examples/01_hugging_face/quickstart.py)

## 官方资料阅读顺序

控制在 60～90 分钟，不要求一次读完全部课程：

1. [Hugging Face Hub 文档首页](https://huggingface.co/docs/hub/index)
2. [LLM Course 第一章](https://huggingface.co/learn/llm-course/chapter1/1)
3. [Transformers Quickstart](https://huggingface.co/docs/transformers/quicktour)
4. [Chat templates](https://huggingface.co/docs/transformers/chat_templating)
5. [Hub 下载指南](https://huggingface.co/docs/huggingface_hub/en/guides/download)

## 当日验收

- [ ] 完成上述五篇知识文档的自测题。
- [ ] 能画出“硬件 → 框架 → 架构 → 工具库 → 应用”的分层关系。
- [ ] 成功运行 `quickstart.py`。
- [ ] 修改问题和至少两个生成参数，比较输出差异。
- [ ] 查看 tokenizer 的分词结果和渲染后的 chat template。
- [ ] 在 `notes/` 中记录运行环境、耗时、发现和疑问。
- [ ] 从今天的资料中选择 5 个英语术语，写入词汇记录。

英语支线：[AI 工程英语学习计划](../notes/ai-engineering-english.md)
