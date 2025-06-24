import streamlit as st
import glob
import json
import os
from pathlib import Path
from copy import deepcopy

st.set_page_config(
    page_title="工具设置",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Define the mcp-config directory
MCP_CONFIG_DIR = "mcp-config"
# Create directory if it doesn't exist
os.makedirs(MCP_CONFIG_DIR, exist_ok=True)

# 侧边栏顶部添加作者信息（放置在其他侧边栏元素之前）
st.sidebar.markdown("### ✍️ Made by [TeddyNote](https://youtube.com/c/teddynote) 🚀")
st.sidebar.markdown(
    "### 💻 [Project Page](https://github.com/teddynote-lab/langgraph-dynamic-mcp-agents)"
)

# --- Sidebar for File Selection & Save ---
with st.sidebar:
    st.header("📂 配置文件选择 & 保存")
    # JSON文件列表
    json_paths = glob.glob(f"{MCP_CONFIG_DIR}/*.json")
    # If no JSON files found, add a default mcp_config.json option
    if not json_paths and not os.path.exists(f"{MCP_CONFIG_DIR}/mcp_config.json"):
        default_config = {"mcpServers": {}}
        with open(f"{MCP_CONFIG_DIR}/mcp_config.json", "w", encoding="utf-8") as f:
            json.dump(default_config, f, indent=2, ensure_ascii=False)
        json_paths = [f"{MCP_CONFIG_DIR}/mcp_config.json"]

    tools_list = [{"name": Path(p).stem, "path": p} for p in json_paths]
    selected_name = st.selectbox("配置文件选择", [t["name"] for t in tools_list])

    # 加载配置
    if st.button("📥 加载选中文件", key="load", use_container_width=True):
        selected = next(t for t in tools_list if t["name"] == selected_name)
        with open(selected["path"], encoding="utf-8") as f:
            st.session_state.tool_config = json.load(f)
        st.session_state.file_path = selected["path"]
        st.session_state.loaded = True
        st.success(f"已加载: {selected_name}.json")

    # 保存更改
    if st.session_state.get("loaded", False):
        if st.button("💾 保存", key="save", use_container_width=True):
            with open(st.session_state.file_path, "w", encoding="utf-8") as f:
                json.dump(st.session_state.tool_config, f, indent=2, ensure_ascii=False)
            st.session_state.saved_msg = (
                f"保存完成: {Path(st.session_state.file_path).name}"
            )
            st.rerun()

# --- Main Area ---
st.title("🔧 MCP Agents 工具设置")

if not st.session_state.get("loaded", False):
    st.info("请在侧边栏加载JSON文件。")
else:
    # 标签页配置：列表、添加、JSON预览、Cursor AI、Claude Desktop
    tab1, tab2, tab3, tab4, tab5 = st.tabs(
        [
            "📝 工具列表",
            "➕ 添加工具",
            "🔍 JSON预览",
            "💻 Cursor AI",
            "🤖 Claude Desktop",
        ]
    )

    # Tab1: Tool List
    with tab1:
        mcp = st.session_state.tool_config.get("mcpServers", {})
        if not mcp:
            st.warning("没有已注册的工具。")
        else:
            for name in list(mcp.keys()):
                col1, col2 = st.columns([9, 1])
                with col1:
                    st.write(f"• **{name}**")
                with col2:
                    if st.button("删除", key=f"del_{name}"):
                        del st.session_state.tool_config["mcpServers"][name]
                        st.success(f"工具 '{name}' 已删除")
                        st.rerun()

    # Tab2: Add Tool
    with tab2:
        st.markdown("🔍 [Smithery 直达链接](https://smithery.ai/)")
        hint = """{
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
      ]
    }
  }
}
"""
        new_tool_text = st.text_area("工具JSON输入", hint, height=260)
        if st.button("添加", key="add_tool"):
            text = new_tool_text.strip()
            try:
                new_tool = json.loads(text)
            except json.JSONDecodeError:
                try:
                    new_tool = json.loads(f"{{{text}}}")
                except json.JSONDecodeError as e:
                    st.error(f"JSON解析错误: {e}")
                    new_tool = None
            if new_tool is not None:
                if "mcpServers" in new_tool and isinstance(
                    new_tool["mcpServers"], dict
                ):
                    tools_data = new_tool["mcpServers"]
                else:
                    tools_data = new_tool
                for name, cfg in tools_data.items():
                    if "transport" not in cfg:
                        cfg["transport"] = "sse" if "url" in cfg else "stdio"
                    st.session_state.tool_config.setdefault("mcpServers", {})[
                        name
                    ] = cfg
                added = ", ".join(tools_data.keys())
                st.success(f"工具 '{added}' 已添加")
                st.rerun()

    # Tab3: JSON Preview
    with tab3:
        st.code(
            json.dumps(st.session_state.tool_config, indent=2, ensure_ascii=False),
            language="json",
        )

    # Tab4: Cursor AI JSON Preview without transport
    with tab4:
        preview = deepcopy(st.session_state.tool_config)
        servers = preview.get("mcpServers", {})
        for cfg in servers.values():
            if isinstance(cfg, dict) and "transport" in cfg:
                del cfg["transport"]
        st.code(json.dumps(preview, indent=2, ensure_ascii=False), language="json")

    # Tab5: Claude Desktop JSON Preview without transport and URL
    with tab5:
        preview_cd = deepcopy(st.session_state.tool_config)
        servers_cd = preview_cd.get("mcpServers", {})
        # 检查并移除包含URL参数的条目
        invalid = [
            name
            for name, cfg in servers_cd.items()
            if isinstance(cfg, dict) and "url" in cfg
        ]
        if invalid:
            st.error(
                f"Claude Desktop不支持包含'url'参数的工具，已排除以下工具: {', '.join(invalid)}"
            )
            for name in invalid:
                del servers_cd[name]
        # 移除transport
        for cfg in servers_cd.values():
            if isinstance(cfg, dict) and "transport" in cfg:
                del cfg["transport"]
        st.code(json.dumps(preview_cd, indent=2, ensure_ascii=False), language="json")

# 底部保存消息输出
with st.sidebar:
    if st.session_state.get("saved_msg"):
        st.success(st.session_state.pop("saved_msg"))
