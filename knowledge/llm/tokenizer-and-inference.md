# Tokenizer、Chat Template 与推理

## 从文本到模型输出

语言模型不直接读取字符串。一次最基本的生成过程是：

```text
字符串 → tokens → token IDs → 模型 → output IDs → 字符串
```

## Tokenizer

Tokenizer 负责：

- 将文本分解为 token。
- 把 token 映射为整数 ID。
- 添加模型所需的特殊 token。
- 将模型输出 ID 解码回文本。

不同模型可能使用不同词表和切分规则，同一段文字的 token 数可能不同。Tokenizer 必须与模型匹配，不能随意混用。

## Model

一个可加载的模型通常包含：

- `config.json`：网络结构配置。
- tokenizer 文件：词表、切分规则和特殊 token。
- `*.safetensors`：模型权重。
- generation config：默认生成参数。

`from_pretrained()` 会根据仓库 ID 或本地目录加载这些内容。

## Pipeline

Transformers 的 `pipeline` 将预处理、模型推理和后处理连接起来，适合快速验证。理解整体流程后，应进一步练习 `AutoTokenizer`、`AutoModelForCausalLM` 和 `model.generate()`。

## Chat Template

对话中的 `role` 和 `content` 最终仍要转换为 token。Chat template 会把多轮消息渲染为模型训练时使用的特殊格式。

不同模型的控制 token 可能不同。错误的格式会明显降低回答质量，因此应使用模型自带的 `apply_chat_template()`，而不是随意拼接字符串。

## 推理、微调与预训练

- 推理：保持权重不变，根据输入生成输出。
- 微调：在已有权重上继续训练，使模型适应任务或风格。
- 预训练：从大量数据训练基础模型，成本远高于个人入门实验。

## 自测

- [ ] 为什么模型不能直接处理字符串？
- [ ] Token 和单词是否总是一一对应？
- [ ] Chat template 为什么会影响输出质量？
- [ ] Pipeline 替我们封装了哪些步骤？
- [ ] 推理时是否会修改模型权重？

## 官方资料

- [Transformers Quickstart](https://huggingface.co/docs/transformers/quicktour)
- [Hugging Face Chat Templates](https://huggingface.co/docs/transformers/chat_templating)

