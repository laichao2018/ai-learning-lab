# PyTorch、TensorFlow 与 Transformer 的关系

更新日期：2026-09-05

## 一句话说明

PyTorch 和 TensorFlow 是用于数值计算、自动求导及构建神经网络的深度学习框架；Transformer 是一种神经网络架构；Hugging Face Transformers 是在这些框架之上提供预训练模型实现、加载和训练工具的库。

它们不是同一层的竞争概念。

## 技术栈分层

```text
AI 应用
聊天、RAG、Agent、分类、翻译、代码助手
                         │
预训练模型与工具库
Hugging Face Transformers、KerasHub 等
                         │
模型架构
Transformer、CNN、RNN、Diffusion 等
                         │
深度学习框架
PyTorch、TensorFlow、JAX
                         │
核心机制
Tensor、计算图、自动求导、优化器、分布式计算
                         │
硬件与加速运行时
CPU、CUDA/NVIDIA GPU、Metal/Apple GPU、TPU
```

上层通常调用下层。一个使用 Hugging Face Transformers 加载的语言模型，底层常由 PyTorch 的 Tensor 和算子执行；它采用的网络结构可能是 Transformer；最终运行在 CPU、GPU 或其他加速器上。

## “Transformers”有两种常见含义

### Transformer：模型架构

Transformer 是一种以 Attention 为核心的神经网络架构。它规定了网络由哪些模块组成、数据如何流动，例如：

- Token Embedding
- Positional Information
- Self-Attention
- Feed-Forward Network
- Normalization
- Residual Connection

GPT、BERT、T5、Qwen 等模型都属于 Transformer 家族，但具体结构和训练目标并不完全相同。

### Transformers：Hugging Face 库

大写名称 `Transformers` 通常指 Hugging Face 的 Python 库。它提供：

- 常见模型架构的代码实现。
- 预训练权重和配置的加载接口。
- Tokenizer 与预处理工具。
- 推理、生成、训练和保存能力。
- 与 Hub、Datasets、Accelerate 等组件的集成。

因此：

```text
Transformer architecture ≠ Hugging Face Transformers library
```

前者是模型设计，后者是实现和使用模型的软件库。

## PyTorch 是什么

PyTorch 是一个开源深度学习框架。它的核心能力包括：

- `torch.Tensor`：支持 CPU 和加速器的多维数组。
- `torch.autograd`：自动计算梯度。
- `torch.nn.Module`：组合神经网络层和模型。
- `torch.optim`：根据梯度更新模型参数。
- `Dataset` 和 `DataLoader`：组织和批量读取数据。
- 分布式训练、模型编译和部署相关工具。

PyTorch 的代码通常接近普通 Python 控制流，因此便于调试和研究。Hugging Face 社区中的大量语言模型示例默认使用 PyTorch。

对于 C++ 工程师，可以这样建立直觉：

- Tensor 类似带有 shape、dtype、device 的多维数组对象。
- `nn.Module` 类似可递归组合、自动注册参数的组件基类。
- Autograd 会记录参与计算的操作关系，并自动执行反向传播。
- Optimizer 根据梯度原地更新参数。

## TensorFlow 是什么

TensorFlow 也是开源深度学习框架，同样提供 Tensor、自动求导、模型构建、训练、分布式计算和部署能力。

常见核心概念包括：

- `tf.Tensor`：多维数据。
- `tf.Variable`：训练时可更新的状态或参数。
- `tf.GradientTape`：记录计算并求梯度。
- `tf.Module`：组织变量和计算。
- Keras Layer/Model：更高层的模型构建接口。
- `tf.data`：数据输入流水线。

TensorFlow 2 默认支持 eager execution，也可以将代码编译为计算图执行。它拥有成熟的训练、服务端部署、移动端和浏览器生态。

## Keras 与 TensorFlow 的关系

Keras 是高层深度学习 API，主要抽象 Layer、Model、Loss、Metric、Optimizer 以及 `fit()`、`evaluate()`、`predict()` 等流程。

历史上 Keras 经常通过 `tf.keras` 与 TensorFlow 绑定，因此很多旧资料会把 Keras 直接称为 TensorFlow 的高层接口。当前 Keras 3 已是多后端 API，可以运行在 TensorFlow、JAX 或 PyTorch 之上。

因此阅读资料时需要注意版本语境：

- 旧资料中的 Keras 往往特指 `tf.keras`。
- 当前 Keras 3 可以选择 TensorFlow、JAX 或 PyTorch 后端。
- Keras 是高层 API；实际张量计算和设备执行仍由所选后端承担。

## JAX 是什么

JAX 提供类似 NumPy 的数值计算接口，并强调函数变换，例如自动求导、即时编译和向量化。它在研究、大规模训练和 TPU 场景中较常见。

Hugging Face 资料中的 Flax 通常指构建在 JAX 上的神经网络库。看到“PyTorch / TensorFlow / Flax”时，可以理解为同一个模型可能存在多套不同框架的实现或权重。

第一周不需要同时学习 JAX，只需知道它处在与 PyTorch、TensorFlow相近的框架层。

## 所有框架共有的基本概念

### Tensor

Tensor 是带有形状和数据类型的多维数组。例如：

```text
标量：shape = []
向量：shape = [hidden_size]
矩阵：shape = [batch_size, hidden_size]
序列批次：shape = [batch_size, sequence_length, hidden_size]
```

模型的输入、输出、参数和中间结果通常都是 Tensor。

### Shape、dtype 与 device

- `shape`：每个维度的大小。
- `dtype`：FP32、FP16、BF16、INT8 等数据类型。
- `device`：数据位于 CPU、GPU、TPU 还是其他设备。

很多运行错误都来自 shape 不匹配、dtype 不兼容或 Tensor 位于不同 device。

### Layer、Model 与 Parameter

- Layer：执行一类计算的网络组件，例如 Linear、Embedding、Attention。
- Model：由多层组件组合成的完整网络。
- Parameter：通过训练更新的 Tensor，例如权重和偏置。

不是所有 Tensor 都是 Parameter。输入、标签和临时计算结果通常不会作为模型参数保存。

### Forward pass

前向传播把输入依次传过模型各层，得到预测结果和 loss。

```text
input → model → prediction → loss(prediction, target)
```

推理通常只需要前向传播。

### Loss

Loss 是衡量模型预测与目标之间差异的标量。训练的目标通常是让平均 loss 下降。语言模型常见目标是根据前文预测下一个 token。

### Gradient 与 Backward pass

梯度描述 loss 对每个参数变化的敏感程度。反向传播从 loss 出发，利用链式法则计算所有可训练参数的梯度。

框架的自动求导系统让开发者不需要手工推导整个网络的梯度。

### Optimizer

Optimizer 使用梯度更新参数。最简化的形式是：

```text
parameter = parameter - learning_rate × gradient
```

实际常使用 SGD、Adam 或 AdamW 等算法。

### Batch、step 与 epoch

- Sample：一条训练样本。
- Batch：一次并行处理的一组样本。
- Step：通常指处理一个 batch 并更新一次参数。
- Epoch：完整遍历一次训练数据。

### Training 与 evaluation mode

训练模式允许计算梯度并启用某些训练行为；评测或推理模式关闭这些行为。PyTorch 中常见 `model.train()`、`model.eval()` 和 `torch.no_grad()`；它们与“调用训练接口”不是同一个概念。

## 一个训练循环发生了什么

框架不同，核心流程基本一致：

```text
for each batch:
    1. 读取输入和标签
    2. 前向传播得到预测
    3. 计算 loss
    4. 清除旧梯度
    5. 反向传播计算新梯度
    6. Optimizer 更新参数
```

PyTorch 风格示意：

```python
optimizer.zero_grad()
prediction = model(inputs)
loss = loss_fn(prediction, targets)
loss.backward()
optimizer.step()
```

TensorFlow 风格示意：

```python
with tf.GradientTape() as tape:
    prediction = model(inputs)
    loss = loss_fn(targets, prediction)

gradients = tape.gradient(loss, model.trainable_variables)
optimizer.apply_gradients(zip(gradients, model.trainable_variables))
```

两段代码表达的是同一套数学过程，只是 API 和执行机制不同。

## Hugging Face Transformers 如何连接这些框架

如果直接手写 Transformer，需要自行实现 Attention、层归一化、前馈网络、权重加载和生成逻辑。Transformers 库把这些常见实现封装起来。

例如：

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(MODEL_ID)
```

在 PyTorch 环境中，`model` 通常最终是一个 `torch.nn.Module`，模型参数是 PyTorch Tensor，前向计算交给 PyTorch 和底层硬件运行时完成。

可以把职责拆成：

- Hub：模型文件存在哪里。
- Transformers：如何识别、加载和使用模型。
- Transformer：模型内部采用什么架构。
- PyTorch/TensorFlow/JAX：如何执行 Tensor 运算、求梯度和更新参数。
- CUDA/Metal/TPU runtime：计算最终在哪种硬件上运行。

## 模型、代码与权重不是同一个东西

一个可运行模型通常至少需要：

- 架构实现：定义有哪些层以及如何计算。
- 配置：层数、隐藏维度、Attention heads 等。
- 权重：训练得到的参数值。
- Tokenizer：文本和 token ID 之间的转换规则。
- Chat template：对话消息的编码格式。

PyTorch 或 TensorFlow 提供计算能力，但不会自动提供某个训练好的模型知识；Transformer 架构描述网络结构，但不等于已经训练好的权重；Hugging Face Hub 则把这些资源组织和发布出来。

## 应该先学 PyTorch 还是 TensorFlow

针对当前“大模型应用 + Hugging Face + C++ 推理”的目标，建议：

1. 先学 PyTorch 基础：Tensor、shape、device、`nn.Module`、autograd。
2. 使用 Hugging Face Transformers 完成推理。
3. 再学习一个最小训练循环，理解参数如何被更新。
4. TensorFlow 先掌握概念对应关系，需要参与相关项目时再深入。
5. 后续结合 C++ 背景学习 libtorch、自定义算子、llama.cpp 或推理优化。

不建议第一周同时深入 PyTorch、TensorFlow 和 JAX。它们解决的问题高度重叠，同时学习容易把 API 差异误当成原理差异。

## 常见误区

- “Transformer 是 PyTorch 的一个功能”：错误。Transformer 是架构，可以用多种框架实现。
- “安装 Transformers 就不需要 PyTorch”：不准确。模型计算仍需要受支持的后端或推理运行时。
- “TensorFlow 只能使用计算图”：过时。TensorFlow 2 默认支持 eager execution。
- “Keras 只能运行在 TensorFlow 上”：对当前 Keras 3 不成立。
- “会调用 `pipeline` 就等于理解训练”：错误。`pipeline` 主要简化推理流程。
- “权重文件就是模型的全部”：不完整。还需要架构、配置、tokenizer 等信息。

## 自测

- [ ] PyTorch/TensorFlow 与 Transformer 为什么不是同一层概念？
- [ ] Transformer 和 Hugging Face Transformers 有什么区别？
- [ ] Tensor、Parameter、Layer、Model 分别是什么？
- [ ] Forward、Loss、Backward、Optimizer 的顺序是什么？
- [ ] 推理为什么通常不需要自动求导？
- [ ] Keras 3 与 TensorFlow 的关系是什么？
- [ ] Hugging Face Hub、Transformers、PyTorch 各负责哪一部分？

## 官方资料

- [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html)
- [PyTorch Tensors](https://docs.pytorch.org/tutorials/beginner/basics/tensorqs_tutorial.html)
- [PyTorch Autograd](https://docs.pytorch.org/tutorials/beginner/basics/autogradqs_tutorial.html)
- [PyTorch nn.Module](https://docs.pytorch.org/docs/stable/generated/torch.nn.Module.html)
- [TensorFlow Basics](https://www.tensorflow.org/guide/basics)
- [TensorFlow Automatic Differentiation](https://www.tensorflow.org/guide/autodiff)
- [TensorFlow Modules, Layers and Models](https://www.tensorflow.org/guide/intro_to_modules)
- [Keras 3 Overview](https://keras.io/about/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)

