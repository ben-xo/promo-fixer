#!/bin/bash
set -e

SCRIPT_DIR=$( cd "$( dirname "$(readlink "${BASH_SOURCE[0]}")" )" && pwd )

FIRST_INSTALL=""
if [[ ! -d ~/.virtualenvs/promo-fixer ]]; then
  python3 -mvenv ~/.virtualenvs/promo-fixer
  FIRST_INSTALL="yes"
fi

. ~/.virtualenvs/promo-fixer/bin/activate

if [[ ! "$FIRST_INSTALL" == "" ]]; then
  pip3 install -r "${SCRIPT_DIR}"/requirements.txt
fi

python3 "${SCRIPT_DIR}"/promo_fixer.py --dir "$@"

deactivate
