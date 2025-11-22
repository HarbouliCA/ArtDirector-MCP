# 🎨 ArtDirector MCP
**The AI-Powered Design Auditor for Data Visualization**

> *"Don't just generate charts. Direct them."*

**ArtDirector** is a Model Context Protocol (MCP) server that acts as a quality assurance layer for AI-generated visualizations. It ensures your charts are **semantic, accessible, and clutter-free**.

---

## 🚀 Features

### 1. 🚦 Semantic Color Enforcement
Ensures your colors match the data's meaning.
*   **Red**: Danger, Loss, Churn, Error, Decrease
*   **Green**: Profit, Growth, Success, Safe, Revenue
*   **Orange**: Warning, Risk, Potential, Pending

### 2. 📏 Layout Intelligence
Prevents design clutter before it happens.
*   **Collision Detection**: Checks if text labels overlap.
*   **Breathing Room**: Enforces minimum padding between elements.

### 3. 👁️ Accessibility (Coming Soon)
*   Contrast ratio checks (WCAG AA).
*   Colorblind-safe palette recommendations.

---

## 📦 Installation

### Prerequisites
*   Python 3.10+
*   `uv` or `pip`

### 1. Clone the Repository
```bash
git clone https://github.com/HarbouliCA/ArtDirector-MCP.git
cd ArtDirector-MCP
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🤖 Configuration for AI Agents

### Option A: Claude Desktop App
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "art-director": {
      "command": "python",
      "args": ["/absolute/path/to/ArtDirector-MCP/server.py"]
    }
  }
}
```

### Option B: VS Code (Cline / Roo Code)
Add this to your MCP settings file:
```json
{
  "mcpServers": {
    "art-director": {
      "command": "python",
      "args": ["/absolute/path/to/ArtDirector-MCP/server.py"]
    }
  }
}
```

### Option C: Google Antigravity / Gem
Add this to your `.gemini/antigravity/mcp_config.json`:
```json
{
  "mcpServers": {
    "art-director": {
      "command": "python",
      "args": ["C:/Users/YOUR_USER/path/to/ArtDirector-MCP/server.py"],
      "enabled": true
    }
  }
}
```

---

## 🛠️ Usage
Once installed, you can ask your AI Agent:

> *"Generate a bar chart for Revenue Growth vs Churn. Then audit it with ArtDirector."*

The AI will:
1.  Generate the chart code.
2.  Send the chart definition to **ArtDirector**.
3.  **ArtDirector** will reply: *"⚠️ Semantic Error: 'Churn' is colored Green. Suggest using Red."*
4.  The AI will fix the code automatically.

---

## 📄 License
MIT License. Built by **Anass Harbouli**.
