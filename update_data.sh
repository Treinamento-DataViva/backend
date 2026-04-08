#!/bin/bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_DIR="${ROOT_DIR}/.venv"
FALLBACK_VENV_DIR="${ROOT_DIR}/venv"

if [ -d "${VENV_DIR}" ]; then
  source "${VENV_DIR}/bin/activate"
elif [ -d "${FALLBACK_VENV_DIR}" ]; then
  source "${FALLBACK_VENV_DIR}/bin/activate"
else
  python3 -m venv "${VENV_DIR}"
  source "${VENV_DIR}/bin/activate"
fi

pip install -r "${ROOT_DIR}/requirements.txt"

python "${ROOT_DIR}/db/init/scripts/etl.py"
