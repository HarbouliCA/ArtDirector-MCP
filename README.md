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

## 🛠️ Usage: The Consultant Workflow

**ArtDirector acts as an advisor, not a blocker.**

1.  **Generate**: The AI generates the visualization code first.
2.  **Consult**: The AI sends the design to ArtDirector.
3.  **Report**: ArtDirector returns a list of **Suggestions** (e.g., *"Consider changing 'Churn' to Red"*).
4.  **Decide**: The User (You) decides whether to apply the changes.
5.  **Verify**: If changes are made, ArtDirector re-checks the final output to ensure accuracy.

> *"Generate the chart, then ask ArtDirector for a design review."*

---

## 📄 License
MIT License. Built by **Anass Harbouli**.
