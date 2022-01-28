FROM gitpod/workspace-full

# Install Ansible
RUN sudo apt update
RUN sudo apt install software-properties-common
RUN sudo add-apt-repository --yes --update ppa:ansible/ansible
RUN sudo apt install ansible

# Powershell
RUN wget https://github.com/PowerShell/PowerShell/releases/download/v7.2.1/powershell-lts_7.2.1-1.deb_amd64.deb && \
    sudo add-apt-repository universe && \
    sudo dpkg --force-all -i powershell-lts_7.2.1-1.deb_amd64.deb && \
    rm powershell-lts_7.2.1-1.deb_amd64.deb