#!/bin/bash
set -e
echo "###############################################################################"
echo "# installing environment"
echo "###############################################################################"
script_root="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $script_root
. $script_root/.env
pip install ${WOWOOL_TEST_PIP_INSTALL_OPTIONS} -r $script_root/requirements.txt
pip list -v | grep wowool

echo "###############################################################################"
echo "# running tests"
echo "###############################################################################"

python3 $script_root/run_all.py
echo "###############################################################################"
echo "# pip info"
echo "###############################################################################"
pip list -v | grep wowool
