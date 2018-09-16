#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m'

# install miniconda3
echo -e "${GREEN}Check miniconda version... ${NC}"

if hash -- "conda" 2> /dev/null; then
    echo -e "${GREEN}=> Miniconda has been installed! ${NC}"
    conda_version=$(conda --version | awk '{print $2}')
    echo "miniconda version: $conda_version"
else
    echo -e "${GREEN}=> Miniconda not be installed, Install miniconda3... ${NC}"
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -O $HOME/install_miniconda.sh
    bash $HOME/install_miniconda.sh -b -p $HOME/miniconda
    rm $HOME/install_miniconda.sh
    export PATH=$PATH:$HOME/miniconda/bin
    conda --version
fi
echo -e "${GREEN}=> Install python dependancy... ${NC}"
conda env create -f mac_env.yml

# install adb tools
echo -e "${GREEN}Install adb tools package... ${NC}"
unzip ./adb_exe/adb.zip -d ./adb_exe/

echo -e "${GREEN}Install Complete!"