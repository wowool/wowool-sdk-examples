#!/bin/bash
script_root="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $script_root

python${1} -m venv env${1}
source env${1}/bin/activate
export WOWOOL_TEST_PIP_INSTALL_OPTIONS="--no-binary=wowool-sdk-cpp"
$script_root/scripts/install-and-test.sh
if [ $? -ne 0 ]; then
  echo "❌ Tests failed for Python ${1}"
  deactivate
  rm -rf env${1}
  exit 1
fi
echo "✅ Done Testing Python ${1}"

deactivate
rm -rf env${1}
