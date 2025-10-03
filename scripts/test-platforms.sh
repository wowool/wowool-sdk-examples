#!/bin/bash
set -e
echo "###############################################################################"
echo "# installing environment"
echo "###############################################################################"
script_root="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $script_root

echo "- py3.12-----------------------------------------------------------------------"
$script_root/scripts/test-platform.sh 3.12
$script_root/scripts/test-platform_no_binary.sh 3.12
echo "- py3.13-----------------------------------------------------------------------"
$script_root/scripts/test-platform.sh 3.13
$script_root/scripts/test-platform_no_binary.sh 3.13
echo "- aarch64 py3.13 -----------------------------------------------------------------------"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/aarch64 -it python:3.13 bash -c "/wowool-sdk-examples/scripts/install-and-test.sh"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/aarch64 -it python:3.13 bash -c "/wowool-sdk-examples/scripts/test-platform_no_binary.sh"
echo "- x86_64 py3.13 -----------------------------------------------------------------------"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/x86_64 -it python:3.13 bash -c "/wowool-sdk-examples/scripts/install-and-test.sh"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/x86_64 -it python:3.13 bash -c "/wowool-sdk-examples/scripts/test-platform_no_binary.sh"

echo "- aarch64 py3.12 -----------------------------------------------------------------------"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/aarch64 -it python:3.12 bash -c "/wowool-sdk-examples/scripts/install-and-test.sh"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/aarch64 -it python:3.12 bash -c "/wowool-sdk-examples/scripts/test-platform_no_binary.sh"
echo "- x86_64 py3.12 -----------------------------------------------------------------------"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/x86_64 -it python:3.12 bash -c "/wowool-sdk-examples/scripts/install-and-test.sh"
docker run -v /Users/phforest/dev/wowool/tir:/tir  -v /Users/phforest/dev/wowool-sdk-examples:/wowool-sdk-examples  --rm --platform=linux/x86_64 -it python:3.12 bash -c "/wowool-sdk-examples/scripts/test-platform_no_binary.sh"