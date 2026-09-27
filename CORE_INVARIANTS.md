# Core Invariants & Axiomatic Foundation (CORE_INVARIANTS.md)

## 1. Skill Execution Purity & Anti-Hallucination

`skill-taxonomy-arbiter` 是 AI 智能体的专属认知 SOP 流程，必须严格遵守以下刚性法则：
1. **禁止概率式黑盒猜测**：智能体在为用户进行架构形态裁决时，必须将特征解构后传递给底层 `tool-taxonomy-arbiter` 执行物理判定，严禁依赖单次模型概率推断。
2. **零温度漂移保障**：无论何种大语言模型在执行该 Skill，对于相同的需求，必须输出完全一致的法定前缀与形态分类。
3. **结构化交付契约**：必须包含决策置信度、七维空间投影坐标与形式化数学推导逻辑链。

---

## 2. 7-Dimensional Orthogonal Feature Space

本 Skill 指导 Agent 提取并验证以下七维客观指标：
- D1: Lifecycle (瞬时 CLI 0.0 vs 常驻后台 1.0)
- D2: Protocol (管道 Stdio 0.0 vs MCP 0.5 vs 网络套接字 1.0)
- D3: Execution (纯文本/提示词 0.0 vs 编译机器代码 1.0)
- D4: Agenticity (确定性机械算法 0.0 vs LLM 提示词流程 1.0)
- D5: Boundary (功能实现 0.0 vs 规范Spec/红线Rule 1.0)
- D6: Swarm (单节点 0.0 vs 多智能体集群网格 1.0)
- D7: Interface (无界面/API 0.0 vs GUI/移动App 1.0)

---

## 3. Provenance & Grounding

本组件严格符合 IEEE/ACM 学术溯源规范，内联全球对标技术源流，并通过 `tool-citation-optima audit` 达到 Fixed-Point S级标准。
