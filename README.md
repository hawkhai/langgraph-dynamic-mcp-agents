# LangGraph Dynamic MCP Agents

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3.23+-green.svg)
![LangGraph](https://img.shields.io/badge/LangGraph-0.3.25+-orange.svg)
[![Open in - LangGraph Studio](https://img.shields.io/badge/Open_in-LangGraph_Studio-00324d.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI4NS4zMzMiIGhlaWdodD0iODUuMzMzIiB2ZXJzaW9uPSIxLjAiIHZpZXdCb3g9IjAgMCA2NCA2NCI+PHBhdGggZD0iTTEzIDcuOGMtNi4zIDMuMS03LjEgNi4zLTYuOCAyNS43LjQgMjQuNi4zIDI0LjUgMjUuOSAyNC41QzU3LjUgNTggNTggNTcuNSA1OCAzMi4zIDU4IDcuMyA1Ni43IDYgMzIgNmMtMTIuOCAwLTE2LjEuMy0xOSAxLjhtMzcuNiAxNi42YzIuOCAyLjggMy40IDQuMiAzLjQgNy42cy0uNiA0LjgtMy40IDcuNkw0Ny4yIDQzSDE2LjhsLTMuNC0zLjRjLTQuOC00LjgtNC44LTEwLjQgMC0xNS4ybDMuNC0zLjRoMzAuNHoiLz48cGF0aCBkPSJNMTguOSAyNS42Yy0xLjEgMS4zLTEgMS43LjQgMi41LjkuNiAxLjcgMS44IDEuNyAyLjcgMCAxIC43IDIuOCAxLjYgNC4xIDEuNCAxLjkgMS40IDIuNS4zIDMuMi0xIC42LS42LjkgMS40LjkgMS41IDAgMi43LS41IDIuNy0xIDAtLjYgMS4xLS44IDIuNi0uNGwyLjYuNy0xLjgtMi45Yy01LjktOS4zLTkuNC0xMi4zLTExLjUtOS44TTM5IDI2YzAgMS4xLS45IDIuNS0yIDMuMi0yLjQgMS41LTIuNiAzLjQtLjUgNC4yLjguMyAyIDEuNyAyLjUgMy4xLjYgMS41IDEuNCAyLjMgMiAyIDEuNS0uOSAxLjItMy41LS40LTMuNS0yLjEgMC0yLjgtMi44LS44LTMuMyAxLjYtLjQgMS42LS41IDAtLjYtMS4xLS4xLTEuNS0uNi0xLjItMS42LjctMS43IDMuMy0yLjEgMy41LS41LjEuNS4yIDEuNi4zIDIuMiAwIC43LjkgMS40IDEuOSAxLjYgMi4xLjQgMi4zLTIuMy4yLTMuMi0uOC0uMy0yLTEuNy0yLjUtMy4xLTEuMS0zLTMtMy4zLTMtLjUiLz48L3N2Zz4=)](https://langgraph-studio.vercel.app/templates/open?githubUrl=https://github.com/langchain-ai/react-agent)

## 项目概述

> 聊天界面

![Project Overview](./assets/Project-Overview.png)

`LangGraph Dynamic MCP Agents` 是一个通过模型上下文协议(MCP)实现可访问各种外部工具和数据源的ReAct代理项目。该项目基于LangGraph的ReAct代理，提供了一个可以轻松添加和配置MCP工具的界面。

![Project Demo](./assets/MCP-Agents-TeddyFlow.png)

### 主要功能
 
**动态工具设置仪表板**

访问`http://localhost:2025`可以查看工具设置仪表板。

![Tool Settings](./assets/Tools-Settings.png)

在**添加工具**标签页中，您可以复制粘贴来自[Smithery](https://smithery.io)的MCP工具JSON配置来添加工具。

![Tool Settings](./assets/Add-Tools.png)

----

**实时反映**

在工具设置仪表板中添加或修改工具时，会实时反映。

![List Tools](./assets/List-Tools.png)

**系统提示设置**

通过修改`prompts/system_prompt.yaml`文件可以设置系统提示。

这也是动态实时反映的形式。

![System Prompt](./assets/System-Prompt.png)

如果想修改代理的系统提示设置，可以修改`prompts/system_prompt.yaml`文件的内容。

----

### 主要特性

* **LangGraph ReAct代理**: 基于LangGraph的ReAct代理
* **实时动态工具管理**: 可以轻松添加、删除、配置MCP工具（支持Smithery JSON格式）
* **实时动态系统提示设置**: 可以轻松修改系统提示（动态反映）
* **对话记录**: 跟踪和管理与代理的对话内容
* **TeddyFlow集成**: 聊天界面集成
* **Docker镜像构建**: 支持Docker镜像构建
* **本地主机支持**: 可以在localhost运行（支持聊天界面集成）

## 安装方法

1. 克隆仓库

```bash
git clone https://github.com/teddynote-lab/langgraph-dynamic-mcp-agents
cd langgraph-dynamic-mcp-agents
```

2. 设置`.env`文件

以`.env.example`文件为模板，复制并重命名为`.env`文件。

```bash
cp .env.example .env
```

在`.env`文件中设置`LLM_PROVIDER`。

可选择（选择一个）: `ANTHROPIC`, `OPENAI`, `AZURE_OPENAI`

```
LLM_PROVIDER=AZURE_OPENAI
```

以下是必需的API密钥列表。（根据选择的`LLM_PROVIDER`进行设置）

`Anthropic`, `OpenAI`, `Azure OpenAI`设置要使用的API密钥。（必须至少设置一个模型。）

- `ANTHROPIC_API_KEY`: Anthropic API密钥
- `OPENAI_API_KEY`: OpenAI API密钥
- `AZURE_OPENAI_API_KEY`: Azure OpenAI API密钥
- `AZURE_OPENAI_ENDPOINT`: Azure OpenAI端点

3. MCP工具设置

以`mcp-config`文件夹中的`mcp_config.json`文件为基准设置模型使用的MCP工具。

因此，可以预先以JSON格式设置要使用的MCP工具。
这个过程也可以在工具设置仪表板中进行设置。

以下是作为示例编写的例子。

```json
{
  "mcpServers": {
    "perplexity-search": {
      "command": "npx",
      "args": [
        "-y",
        "@smithery/cli@latest",
        "run",
        "@arjunkmrm/perplexity-search",
        "--key",
        "SMITHERY_API_KEY"
      ],
      "transport": "stdio"
    },
    "get_current_time": {
      "command": "python",
      "args": [
        "/app/resources/mcp_server_time.py"
      ],
      "transport": "stdio"
    }
  }
}
```

4. 将.py文件添加为MCP `stdio`服务器

- （参考）请参考`resources`文件夹中的`mcp_server_time.py`文件。

1. 将要使用的自定义编写的.py文件添加到`resources`文件夹中。并编写代码使其能够作为`stdio`服务器运行。

2. 添加到`mcp-config/mcp_config.json`时修改文件路径。

    **规则**

    `./resources/文件名.py` > `/app/resources/文件名.py`

    例如，如果要添加`./resources/mcp_server_time.py`文件，则设置为`/app/resources/mcp_server_time.py`。

```json
"get_current_time": {
    "command": "python",
    "args": [
    "/app/resources/mcp_server_time.py"
    ],
    "transport": "stdio"
}
```

6. 添加在Smithery注册的工具

可以从[Smithery](https://smithery.ai/)获取要使用的MCP工具JSON配置，并在工具仪表板中轻松添加。

1. 访问[Smithery](https://smithery.io)网站，选择要使用的工具。
2. 在工具页面点击右侧的'COPY'按钮复制JSON配置。

![Smithery Copy JSON](./assets/smithery-copy-json.png)

3. 打开`mcp_config.json`文件，添加复制的JSON。

> 粘贴复制的内容。

![Add Smithery Tool](./assets/Add-Smithery-Tool.png)

## 应用程序运行

所有设置完成后，可以使用以下命令运行。

> Windows(PowerShell)

```bash
docker compose build --no-cache; docker-compose up -d
```

> Mac / Linux

```bash
docker compose build --no-cache && docker-compose up -d
```

**访问地址**

- TeddyFlow集成: https://teddyflow.com/
- 聊天界面: `http://localhost:2024`
- 工具设置仪表板: `http://localhost:2025`

## teddyflow.com 连接方法

1. 在teddyflow.com注册会员。

注册时在"测试密钥"中输入`teddynote-youtube`可以无需审批直接注册。

![teddyflow-code](./assets/teddyflow-code.png)

2. 登录后点击"连接新应用"按钮。

![teddyflow-guide-01](./assets/teddyflow-guide-01.png)

3. 输入应用名称并点击"连接"按钮。
4. 在标签页中选择"LangGraph"，然后输入以下信息：
- Endpoint: `http://localhost:2024`
- Graph: `agent`

![teddyflow-guide-02](./assets/teddyflow-guide-02.png)

5. 连接设置完成后点击"保存"按钮。

6. 点击"连接应用"按钮进行保存。

## 公司名称/社区徽标和品牌应用

我们推出了面向公司名称/社区的自定义功能。

![teddyflow-company](./assets/teddyflow-custom-logo.png)

如果您希望引入，请联系service@brain-crew.com，我们将为您提供帮助。

## 许可证

Apache License 2.0 ([LICENSE](LICENSE))