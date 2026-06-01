#!/usr/bin/env bash
set -euo pipefail

# Build site
./scripts/build.sh

# Deploy via Wrangler (production env)
wrangler deploy --env production

