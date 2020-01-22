#!/bin/bash

launch_dir=$(pwd)
pjt_root_dir="$(cd "$( dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1  && cd .. && pwd)"

cd $pjt_root_dir

source ./bin/utilities.sh

#==============================================================================
section 'Switch to Project Root [if necessary] and Load Utilities'
#==============================================================================
success 'Bash utilities loaded!'

if [ "$launch_dir" != "$pjt_root_dir" ]; then
  success "Switched to project root for execution"
fi


#==============================================================================
section 'Prompt to Install Dependencies'
#==============================================================================
read -p 'Install PyQT5 System Dependencies? [y/n] ' -n 1 -r

echo && echo

if [[ $REPLY =~ ^[Yy]$ ]]; then
    sudo apt-get install qtcreator pyqt5-dev-tools
    sudo apt-get install python3-pyqt5
    sudo apt-get install qttools5-dev-tools
    sudo apt-get install python3-pyqt5.qtwebkit
else
  success 'Skipping system dependency installations ...'
fi

#==============================================================================
section 'Setup and Activate Python3.7 Virtual Environment'
#==============================================================================
if [[ "$VIRTUAL_ENV" != "" ]]; then
  deactivate >/dev/null 2>&1
  success "Deactivated current virtual environment"
fi

virtualenv -p $(which python3.7) venv  >/dev/null 2>&1
success "Set-up Python 3.7 virtual environment"

source ./venv/bin/activate >/dev/null 2>&1
success "Activated Python 3.7 virtual environment"

pip install -r ./requirements.txt >/dev/null 2>&1
success "Installed ./requirements.txt dependencies"


#==============================================================================
section 'Finishing Up'
#==============================================================================
if [ "$launch_dir" != "$pjt_root_dir" ]; then
  success "Drop you back off in your start directory."
  cd $launch_dir
fi

echo