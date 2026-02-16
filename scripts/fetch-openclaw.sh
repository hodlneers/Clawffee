#!/usr/bin/env bash
set -euo pipefail

UPSTREAM_URL="https://github.com/openclaw/openclaw.git"
TARGET_DIR="external/openclaw"
OPENCLAW_REF="${OPENCLAW_REF:-main}"

mkdir -p external

if [ ! -d "${TARGET_DIR}/.git" ]; then
  echo "[clawffee] Cloning OpenClaw into ${TARGET_DIR}"
  git clone "${UPSTREAM_URL}" "${TARGET_DIR}"
else
  echo "[clawffee] Updating OpenClaw in ${TARGET_DIR}"
fi

cd "${TARGET_DIR}"

git fetch --tags --prune origin

git checkout "${OPENCLAW_REF}"

if git rev-parse --verify "origin/${OPENCLAW_REF}" >/dev/null 2>&1; then
  git reset --hard "origin/${OPENCLAW_REF}" >/dev/null
fi

echo "[clawffee] OpenClaw checked out at: $(git rev-parse HEAD)"
