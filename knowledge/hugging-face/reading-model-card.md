# 如何阅读 Hugging Face Model Card

模型页面不只是下载入口。Model Card 应该帮助使用者了解模型的用途、使用方法、评测、限制和许可证。

## 阅读顺序

### 1. 作者与仓库 ID

优先使用模型开发方的官方组织账号，确认仓库 ID 没有拼写混淆。社区量化版和微调版并不等于原始官方模型。

### 2. 任务类型

确认它用于文本生成、Embedding、分类、视觉还是其他任务。任务不匹配时，模型即使很大也无法直接解决问题。

### 3. Base 与 Instruct

- Base 模型主要完成续写，适合继续训练或研究。
- Instruct/Chat 模型经过指令或对话训练，更适合直接问答。

入门对话实验应优先选择 Instruct/Chat 版本。

### 4. 参数与架构

查看参数量、上下文长度、Dense/MoE 类型、支持语言和输入模态。参数量的详细解释见[模型参数量、精度与资源需求](../llm/model-parameters.md)。

### 5. 文件格式与精度

- `safetensors` 常用于 Transformers。
- `GGUF` 常用于 llama.cpp。
- FP16、BF16、INT8、INT4 会影响文件大小、内存和推理表现。

### 6. License

许可证决定是否允许商用、修改和分发。公开下载不等于没有使用限制。

### 7. Gated model

Gated 模型要求登录并接受条款或申请权限。能看到仓库页面不代表可以直接下载权重。

### 8. Limitations and biases

查看模型不适合什么任务、训练数据可能有什么偏差，以及官方建议的安全边界。

### 9. 使用示例与版本

优先采用 Model Card 当前给出的调用方式。生产或可复现实验应通过 `revision` 固定 tag 或完整 commit hash，避免 `main` 更新后行为变化。

## 选择模型的检查清单

- [ ] 任务和语言匹配。
- [ ] 是适合直接使用的 Instruct/Chat 版本。
- [ ] 许可证满足用途。
- [ ] 参数量和精度适合本机硬件。
- [ ] 上下文长度满足输入规模。
- [ ] 阅读过限制和已知风险。
- [ ] 调用代码与当前版本一致。

## 自测

- [ ] 为什么不能只按下载量选择模型？
- [ ] Base 模型为什么不一定适合直接聊天？
- [ ] 公开模型为什么仍然必须查看许可证？
- [ ] `revision` 对可复现实验有什么帮助？

## 官方资料

- [Hugging Face Model Cards](https://huggingface.co/docs/hub/model-cards)
- [下载与固定 revision](https://huggingface.co/docs/huggingface_hub/en/guides/download)

