#!/bin/bash
chmod +x ~/MA/bin/*.py
chmod +x ~/MA/bin/*.sh
trap "chmod -x ~/MA/bin/*" EXIT
