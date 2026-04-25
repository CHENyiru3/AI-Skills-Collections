# Skill Seekers 参考

本参考基于上游项目 `yusufkaraaslan/Skill_Seekers`，并整理成适合本仓库技能使用的简体中文说明。

## 它能做什么

Skill Seekers 可以把各种资料源转换成结构化的 AI 知识资产，再打包给不同平台使用。最常见的流程是：

```bash
pip install skill-seekers
skill-seekers create <source>
skill-seekers package output/<name> --target <platform>
```

## 常见输入

- 文档网站
- GitHub 仓库，例如 `facebook/react`
- 本地项目目录，例如 `./my-project`
- PDF、DOCX、EPUB、PPTX、HTML、OpenAPI 文件
- Jupyter Notebook
- RSS 或 Atom 订阅
- 视频
- Confluence、Notion、Slack、Discord 导出内容

## 常见输出

- `--target claude`：面向 Claude 的技能包
- `--target gemini`：面向 Gemini 的技能包
- `--target openai`：面向 OpenAI 或 Custom GPT 的打包结果
- `--target langchain`：LangChain 文档
- `--target llama-index`：LlamaIndex 节点
- `--target haystack`：Haystack 文档
- 适合向量数据库继续处理的 Markdown 或结构化内容

## 最小示例

### 文档网站

```bash
skill-seekers create https://docs.react.dev/
skill-seekers package output/react --target claude
```

### GitHub 仓库

```bash
skill-seekers create facebook/react
skill-seekers package output/react --target openai
```

### 本地项目

```bash
skill-seekers create ./my-project
skill-seekers package output/my-project --target langchain
```

### PDF

```bash
skill-seekers create manual.pdf
skill-seekers package output/manual --target claude
```

## 建议回答方式

给用户建议时：

- 如果资料源不明确，先问清楚 source。
- 如果目标平台未确定，先确认 target。
- 优先给出两到三条可以直接运行的命令。
- 只有在基础流程明确后，再补充增强 preset、可复用 config、多源整合等内容。

## 推荐定位

可以把 Skill Seekers 说明为 AI 系统的数据准备层：

- 一次采集
- 一次生成结构化输出目录
- 同一份输出可以继续打包到多个 AI 平台

## 后续扩展点

在快速路径跑通后，可以继续建议：

- 从同一份输出打包到多个目标平台
- 制作可重复使用的配置文件
- 合并多种来源生成一个知识资产
- 增加 enhancement 步骤，让 `SKILL.md` 更完整

## 上游链接

- 仓库：`https://github.com/yusufkaraaslan/Skill_Seekers`
- 网站与文档：`https://skillseekersweb.com/`
