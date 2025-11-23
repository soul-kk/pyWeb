# 基于 Fzd6 基因突变小鼠肠菌群数据的分析系统

## 项目简介
这是一个使用 Python (Streamlit) 开发的实验模拟系统，用于展示基因突变型与野生型小鼠在脂多糖处理后肠道菌群的变化分析。

## 核心功能
- **实验设置模拟**：模拟选择突变型和野生型小鼠的过程。
- **数据分析展示**：点击“处理完成”后，自动展示 Alpha 多样性、Beta 多样性、菌科变化及相关性分析结果。

## 快速开始

### 1. 本地运行

确保你已经安装了 Python (建议 3.8+)。

1. **安装依赖**
   ```bash
   pip install -r requirements.txt
   ```

2. **启动应用**
   ```bash
   streamlit run app.py
   ```

3. **访问**
   浏览器会自动打开 `http://localhost:8501`。

---

## 部署指南 (公网访问)

最简单、免费且长期有效的部署方式是使用 **Streamlit Community Cloud**。

### 方法一：Streamlit Community Cloud (推荐)

1. **上传代码到 GitHub**
   - 将本项目代码 (`app.py`, `requirements.txt`) 上传到你的 GitHub 仓库。

2. **登录 Streamlit Cloud**
   - 访问 [share.streamlit.io](https://share.streamlit.io/)。
   - 使用 GitHub 账号登录。

3. **部署应用**
   - 点击 "New app"。
   - 选择刚才创建的 GitHub 仓库、分支 (main) 和主文件 (`app.py`)。
   - 点击 "Deploy"。

4. **完成**
   - 等待几分钟，部署完成后你会获得一个专属的公网 URL (例如: `https://fzd6-analysis.streamlit.app`)，可以直接分享给他人访问。

### 方法二：使用 Ngrok (临时测试)

如果你不想上传 GitHub，可以使用 ngrok 将本地端口暴露到公网（仅用于临时演示）。

1. 下载并安装 [ngrok](https://ngrok.com/)。
2. 在终端运行 Streamlit 应用: `streamlit run app.py`。
3. 新开一个终端窗口，运行:
   ```bash
   ngrok http 8501
   ```
4. 复制生成的 Forwarding URL (例如 `https://xxxx.ngrok-free.app`) 即可访问。

