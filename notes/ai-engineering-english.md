# 支线任务：AI 工程英语

更新日期：2026-09-05

## 目标

这条支线的目标不是应试英语，而是在实际工作中做到：

1. 能阅读 Hugging Face Model Card 和官方文档。
2. 能理解安装日志、异常信息和 GitHub Issue。
3. 能准确描述模型、数据、推理、训练和评测过程。
4. 能用简单英语搜索问题、提交 Issue 或写 README。

每天投入 20～30 分钟，坚持和主线学习内容绑定。

## 每日五步法

### 1. Read：阅读 5～10 分钟

阅读当天正在使用的英文官方文档，只选一小节。第一遍不要逐词翻译，先回答：

- 这段在解决什么问题？
- 输入、操作和输出分别是什么？
- 哪些单词重复出现？

### 2. Collect：收集 5 个词或词组

只记录当天真实遇到的高频表达，不抄大词表。每条记录包含：

```text
term: checkpoint
中文：模型检查点；某个训练或保存阶段的模型状态
原句：Load a model from a checkpoint.
自己的句子：This checkpoint is used for text generation.
易混淆项：checkpoint 不一定等于完整的最终模型产品
```

### 3. Write：写 3 句英文

用当天的词描述自己做过的事情，例如：

```text
I loaded a pretrained model from the Hugging Face Hub.
The tokenizer converted the prompt into token IDs.
The model generated 128 new tokens during inference.
```

先追求准确和清楚，不追求复杂句型。

### 4. Speak：口头复述 2 分钟

不看原文，用英语说明：今天运行了什么、遇到了什么问题、如何解决。不会的词先用简单表达替代。

### 5. Review：间隔复习 5 分钟

复习节奏：当天、次日、第 3 天、第 7 天。看到英文能解释意思，并能自己造句，才算掌握。

## 七天词汇主题

### Day 1：Hugging Face 与模型页面

- `repository`：仓库
- `model card`：模型说明文档
- `dataset`：数据集
- `Space`：托管在 Hugging Face 上的演示应用
- `pretrained model`：预训练模型
- `checkpoint`：模型检查点
- `model weights`：模型权重
- `configuration`：配置
- `license`：许可证
- `gated model`：需要申请或接受条款才能访问的模型
- `download` / `upload`：下载 / 上传
- `revision`：仓库的分支、标签或提交版本
- `cache`：缓存

练习：打开一个 Model Card，用中文回答它的用途、许可证、参数规模、输入输出和限制。

### Day 2：Prompt 与文本生成

- `prompt`：提供给模型的输入指令或上下文
- `system message`：规定模型行为的系统消息
- `instruction`：指令
- `completion`：模型生成的补全文本
- `structured output`：结构化输出
- `sampling`：从概率分布中采样
- `temperature`：控制采样随机性的参数
- `top-p`：核采样阈值
- `maximum output tokens`：最大输出 token 数
- `deterministic`：相同输入下结果可重复或接近固定
- `truncate`：截断
- `streaming`：流式返回输出

练习：用英文写一个要求模型输出 JSON 的简短 Prompt。

### Day 3：Embedding 与 RAG

- `embedding`：将内容表示成向量
- `vector`：向量
- `similarity`：相似度
- `retrieval`：检索
- `retrieve`：检索、取回
- `chunk`：文档切分后的片段
- `index`：索引
- `query`：查询
- `relevance`：相关性
- `ranking` / `reranking`：排序 / 重排序
- `context`：提供给模型的上下文
- `grounded answer`：基于给定资料、有依据的回答

练习：用五句简单英语描述 RAG 的完整流程。

### Day 4：Agent 与工具调用

- `agent`：能够规划并调用工具完成任务的智能体
- `tool call`：工具调用
- `argument` / `parameter`：调用参数
- `schema`：数据结构约束
- `workflow`：工作流
- `state`：执行过程中的状态
- `permission`：权限
- `side effect`：修改外部状态的副作用
- `sandbox`：受限制的执行环境
- `human approval`：人工确认
- `timeout`：超时
- `retry`：重试

练习：用英文说明为什么删除文件的工具调用需要人工确认。

### Day 5：评测与可靠性

- `evaluation` / `eval`：评测
- `benchmark`：基准测试
- `test case`：测试用例
- `metric`：指标
- `accuracy`：准确率
- `precision`：查准率
- `recall`：召回率
- `latency`：延迟
- `throughput`：吞吐量
- `hallucination`：模型生成无依据内容的现象
- `regression`：修改后已有能力退化
- `failure mode`：典型失败方式

练习：用英文记录一次模型测试，包括期望结果、实际结果和失败原因。

### Day 6：推理、量化与性能

- `inference`：使用已有模型生成结果
- `training`：通过数据更新模型参数
- `fine-tuning`：在预训练模型上继续训练
- `quantization`：降低数值精度以减少资源占用
- `context window`：单次可处理的上下文范围
- `KV cache`：保存 Attention 中间状态的缓存
- `memory footprint`：内存或显存占用
- `offload`：把部分计算或权重转移到其他设备
- `batch`：批量处理的一组输入
- `token per second`：每秒生成的 token 数
- `time to first token`：首个 token 的等待时间
- `bottleneck`：性能瓶颈

练习：用英文比较本地小模型和云端大模型的速度、成本与质量。

### Day 7：开源协作

- `issue`：问题或需求记录
- `pull request`：代码合并请求
- `reproduce`：复现问题
- `prerequisite`：前置条件
- `dependency`：依赖
- `installation`：安装过程
- `troubleshooting`：故障排查
- `workaround`：临时解决方法
- `breaking change`：不向后兼容的变更
- `deprecated`：已弃用
- `release notes`：版本说明
- `contribution`：贡献

练习：选择一个英文 GitHub Issue，写出问题、复现步骤、实际行为和预期行为。

## Hugging Face 页面常见表达

- `Use this model`：查看如何调用这个模型。
- `Files and versions`：查看仓库文件和历史版本。
- `This model is gated`：需要登录并接受条件或申请访问。
- `Load a pretrained model`：加载已经训练好的模型。
- `Run inference`：执行推理。
- `Fine-tune on a downstream task`：针对下游任务继续训练。
- `Push to Hub`：将模型、数据或应用上传到 Hugging Face Hub。
- `For research purposes only`：只允许研究用途，需仔细核对许可证。
- `Limitations and biases`：模型的限制与潜在偏差。
- `Out-of-distribution`：输入偏离训练数据分布。

## 容易混淆的词

### model、architecture、weights、checkpoint

- `architecture` 是网络结构设计。
- `weights` 是训练得到的参数数值。
- `checkpoint` 是某个保存时刻的权重及相关状态。
- `model` 在不同语境中可能指结构、权重或完整可运行对象。

### parameter 与 argument

- `parameter` 常指函数定义中的参数、配置项，也指模型参数。
- `argument` 常指函数调用时传入的具体值。
- 在一般技术文档中两者有时会被宽松地混用。

### train、fine-tune、infer

- `train from scratch`：从头训练。
- `fine-tune`：在已有模型上继续训练。
- `infer` / `run inference`：不更新权重，只生成结果。

### retrieve、search、fetch、load

- `search`：搜索候选结果。
- `retrieve`：检索并取回相关内容，RAG 中最常见。
- `fetch`：从远端获取资源或数据。
- `load`：把文件或对象载入程序或内存。

## 建议的术语记录模板

每周新建一个文件，例如 `notes/glossary-week-01.md`：

```markdown
# Glossary Week 01

## checkpoint

- 中文：模型检查点
- 来源：Hugging Face Transformers Quickstart
- 原句：
- 我的理解：
- 我的例句：
- 复习日期：Day 1 / Day 2 / Day 4 / Day 7
```

## 每周验收标准

- 能快速识别本周至少 30 个高频术语。
- 能不借助翻译阅读一个简短 Model Card。
- 能用英文写出程序的安装与运行步骤。
- 能用 3～5 句英文准确描述一次实验。
- 能用英文关键词搜索并定位一个技术问题。

衡量进步的标准不是背了多少单词，而是查阅英文资料和定位问题所需的时间是否变短。

