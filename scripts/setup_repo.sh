#!/usr/bin/env bash
set -euo pipefail

REPO_URL="git@github.com:mahtin/rachellevy.org.uk.git"

# Initial git setup
git init
git remote add origin "$REPO_URL"

# Create basic structure
mkdir -p content/pages themes scripts .github/workflows

# Add Smashing Magazine theme as a submodule
if [ ! -d "themes/smashing-magazine" ]; then
  git submodule add https://github.com/getpelican/pelican-themes.git themes/pelican-themes
  # Symlink or copy the smashing-magazine theme
  ln -s pelican-themes/smashing-magazine themes/smashing-magazine
fi

echo "Repository initialized. Now run: git add . && git commit -m 'Initial commit'"

