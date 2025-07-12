#!/bin/bash
set -e

echo "🔧 Installing PaperHunter..."

# 1. Install dependencies
if command -v pip3 >/dev/null 2>&1; then
  echo "📦 Installing dependencies..."
  pip3 install --user -r requirements.txt
else
  echo "❌ pip3 not found. Please install Python 3 and pip first."
  exit 1
fi

# 2. Create ~/.local/bin directory
TARGET="$HOME/.local/bin"
mkdir -p "$TARGET"

# 3. Make main.py executable
chmod +x main.py

# 4. Create symbolic link to ~/.local/bin/paperhunter
ln -sf "$(pwd)/main.py" "$TARGET/paperhunter"

# 5. Detect current shell and modify profile
SHELL_NAME=$(basename "$SHELL")
if [[ "$SHELL_NAME" == "bash" ]]; then
  PROFILE="$HOME/.bashrc"
elif [[ "$SHELL_NAME" == "zsh" ]]; then
  PROFILE="$HOME/.zshrc"
else
  PROFILE="$HOME/.profile"
fi

# 6. Check if PATH is already added, append if not
if ! grep -q 'export PATH="$HOME/.local/bin:$PATH"' "$PROFILE"; then
  echo "📌 Adding ~/.local/bin to PATH in $PROFILE"
  echo '' >> "$PROFILE"
  echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$PROFILE"
else
  echo "✅ PATH already includes ~/.local/bin in $PROFILE"
fi

# 7. Attempt to refresh PATH for current shell
export PATH="$HOME/.local/bin:$PATH"

# 8. Verify installation
if command -v paperhunter >/dev/null 2>&1; then
  echo "✅ Installation complete! You can now run 'paperhunter' command."
  echo "🧪 Try running: paperhunter -con ndss -year 2024 -kw dns"
else
  echo "⚠️ Warning: 'paperhunter' command not found in current shell."
  echo "⚠️ Please restart your terminal, or run: source $PROFILE"
  echo "⚠️ Alternatively, run: exec $SHELL"
fi
