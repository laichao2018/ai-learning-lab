# AI Learning Lab

这是我的大模型与 AI 工程学习仓库，主要记录概念、代码实验、项目实践和评测结果。

## 当前目标

用一周时间完成从传统软件工程到大模型应用开发的入门，最终做出一个能够检索 C++ 代码、调用工具并运行评测的代码库助手。

## 仓库结构

```text
.
├── ROADMAP.md              # 七天学习计划
├── notes/                  # 每日笔记和概念总结
├── examples/               # 独立的小型代码实验
├── projects/
│   └── cpp-assistant/      # 一周实战项目
├── evals/                  # 测试问题、评测脚本和结果
└── resources/              # 学习资料索引
```

## 学习原则

1. 先调用模型，再理解模型内部原理。
2. 先手写最小实现，再引入大型框架。
3. 每个实验都记录输入、输出、耗时和成本。
4. 重要结论必须能够通过测试或资料来源验证。
5. API Key 只放在本地 `.env`，绝不提交到 Git。

## 开始使用

```bash
cp .env.example .env
python3 -m venv .venv
source .venv/bin/activate
```

后续根据具体实验安装依赖。学习进度记录在 [ROADMAP.md](ROADMAP.md)。

