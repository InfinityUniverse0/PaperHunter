#!/bin/bash

set -e

echo "🔧 Installing PaperHunter..."

# 1. 安装依赖
if command -v pip3 >/dev/null 2>&1; then
  echo "📦 Installing dependencies..."
  pip3 install --user -r requirements.txt
else
  echo "❌ pip3 not found. Please install Python 3 and pip first."
  exit 1
fi

# 2. 创建 ~/.local/bin
TARGET="$HOME/.local/bin"
mkdir -p "$TARGET"

# 3. 添加执行权限
chmod +x main.py

# 4. 建立软链接
ln -sf "$(pwd)/main.py" "$TARGET/paperhunter"

# 5. 检查 PATH
if [[ ":$PATH:" != *":$TARGET:"* ]]; then
  echo "📌 Please add the following line to your shell config (~/.bashrc or ~/.zshrc):"
  echo 'export PATH="$HOME/.local/bin:$PATH"'
  echo "Then run: source ~/.bashrc or source ~/.zshrc"
else
  echo "✅ $TARGET is already in your PATH"
fi

# 6. 完成提示
echo "✅ Installation complete!"
echo "🧪 Try running: paperhunter -con ndss -year 2024 -kw \"dns\""
