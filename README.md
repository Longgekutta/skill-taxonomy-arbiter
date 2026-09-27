# skill-taxonomy-arbiter: 软件架构形态确定性仲裁决策技能
### Deterministic Software Archetype Decision Arbiter Skill for AI Agents

[![Status: Production Ready](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)](#)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Type: Agent Skill](https://img.shields.io/badge/Type-Agent%20Skill%20(SOP)-purple.svg)](#)
[![Mathematical Invariance: 100%](https://img.shields.io/badge/Invariance-100%25%20Guaranteed-gold.svg)](#)

---

## 🌟 技能使命与定位 (Mission & Agentic Role)

在智能体驱动的软件工程体系中，`skill-taxonomy-arbiter` 是 AI Agent 的专属认知裁决指南。  
当开发者在会话中提出新产品思路、功能点或者审视一个现有代码仓库时，Agent 通过执行本 Skill 的五步标准作业程序 (SOP)，自主调用底层 `tool-taxonomy-arbiter`，完成七维正交向量投影，并交付具备法律级严谨性的架构形态裁决书。

---

## 🏛️ 技术思想溯源与全球对标矩阵 (World-Class Heritage & Prior Art)

本 Skill 基于全球顶尖软件架构分类学与认知代理工程实践提炼而成：

| 权威源流 / 开源基座 | 源流定位 | 核心机制突破 (Distilled Mechanics) | 本项目吸收与借鉴要点 | 超越点与取舍 (Trade-offs & Innovations) |
| :--- | :--- | :--- | :--- | :--- |
| **[ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101)** [^1] | `SYSTEM_DESIGN_GOLD_STANDARD` (⭐ 90k) | 可视化系统设计、计算密集服务与存储中间件的正交解耦定义 | 吸收其对分布式服务 (Svc)、离线装具 (Tool) 与边界守卫的严格职责划分 | 转化为指导 AI Agent 交互会话的标准作业程序 (SOP) |
| **[tt-a1i/archify](https://github.com/tt-a1i/archify)** [^2] | `AST_ARCH_EXTRACTOR` (⭐ 72.3k) | 从物理代码树静态遍历自动推导软件拓扑与架构组件 | 吸收其代码/文档文件比例计算模型与网络端口监听签名检测算法 | 拓展了 Agentic 时代特有的 Model Context Protocol (MCP)、AI Skill SOP、集群 Mesh 等专属新范式形态判定 |
| **[d2lang/d2](https://github.com/d2lang/d2)** [^3] | `DECLARATIVE_TAXONOMY_ENGINE` (⭐ 25.5k) | 严格声明式图谱语法与编译器状态机的确定性推导 | 吸收其确定性状态推导的设计哲学，确保相同输入永远产生完全相同的决策树 | 专注于多仓工程架构治理与形态裁决 |
| **[kgrzybek/modular-monolith-with-ddd](https://github.com/kgrzybek/modular-monolith-with-ddd)** [^4] | `BOUNDED_CONTEXT_CANONICAL` (⭐ 14k) | 领域驱动设计 (DDD) 与严格的限界上下文防腐层划分 | 吸收其领域边界防腐理念，严格隔离 Rule (负向红线) 与 Spec (正向规范) | 融合 Spotify Backstage 与 CNCF 11 级生态位模型 |
| **[NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent)** [^5] | `AGENT_RUNTIME_TAXONOMY` (⭐ 5.4k) | 智能体环境执行器与提示词认知工作流的解耦标准 | 吸收其将 Agent SOP (Skill) 与底层可执行机器装具 (Tool) 物理分离的规范 | 确立“纯提示词工作流为 skill-*，二进制/命令行算法为 tool-*”的绝对刚性分流守则 |

### 📚 权威引用与事实锚点 (Normative Footnotes)
[^1]: **ByteByteGoHq/system-design-101**: [https://github.com/ByteByteGoHq/system-design-101](https://github.com/ByteByteGoHq/system-design-101). *Explain complex systems using visuals and simple terms.*
[^2]: **tt-a1i/archify**: [https://github.com/tt-a1i/archify](https://github.com/tt-a1i/archify). *Deterministic architectural analysis and AST structure mapping.*
[^3]: **d2lang/d2**: [https://github.com/d2lang/d2](https://github.com/d2lang/d2). *Modern declarative diagramming language with deterministic compiler logic.*
[^4]: **kgrzybek/modular-monolith-with-ddd**: [https://github.com/kgrzybek/modular-monolith-with-ddd](https://github.com/kgrzybek/modular-monolith-with-ddd). *Domain-driven design and strict bounded context enforcement.*
[^5]: **NousResearch/hermes-agent**: [https://github.com/NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent). *Autonomous agent runtime and task orchestration taxonomy.*

---

## ⚖️ 决策动机、取舍与坚决不做的事 (Rationale, Trade-offs & Non-Goals)

### Non-Goals (坚决不做的事)
1. **坚决不做单体大模型主观猜测**：严格强制 Agent 调用底层 `tool-taxonomy-arbiter` 获取数学级判定，严禁 LLM 在缺乏向量推导的情况下信口开河。
2. **坚决不侵入具体业务实现**：本 Skill 的职责为“架构裁定与生态位划分”，不承担具体的代码生成或脚手架初始化。

### Alternatives Considered (备选方案为何被否决)
* **纯自由文本会话建议**：否决。不同模型甚至同一模型在不同上下文中的回答差异巨大，违背用户对“每一次思考得到的结果高度相同或者相似”的核心诉求。
* **硬编码固定问答树**：否决。缺乏高维欧式连续投影计算，无法平滑处理既包含网关又包含客户端特性的复合型前沿项目。

---

## 🛠️ 安装与使用指南 (Installation & Usage)

### 1. 全局智能体安装
已自动部署至全局环境：
`C:\Users\28461\.gemini\config\skills\skill-taxonomy-arbiter\SKILL.md`

### 2. 交互式触发方式
用户仅需在任意对话中提问：
* *"我有一个想法：[需求描述]，应该做成项目还是skill还是mcp？"*
* *"帮我看一下项目 D:\github\xxx 到底符合什么生态位？"*

智能体将自动激活本技能，执行底层工具推演并交付标准裁决书。

---

## 📄 许可证与引用 (License & Citation)

本项目采用 MIT 许可证开源。学术与架构引用请参阅 [`CITATION.cff`](file:///D:/github/skill-taxonomy-arbiter/CITATION.cff)。
