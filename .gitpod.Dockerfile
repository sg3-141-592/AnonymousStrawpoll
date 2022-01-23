FROM gitpod/workspace-full
# Powershell
#https://github.com/PowerShell/PowerShell/releases/download/v7.2.1/powershell-lts_7.2.1-1.deb_amd64.deb
RUN wget https://github.com/PowerShell/PowerShell/releases/download/v7.2.1/powershell-lts_7.2.1-1.deb_amd64.deb && \
    sudo add-apt-repository universe && \
    sudo dpkg --force-all -i powershell-lts_7.2.1-1.deb_amd64.deb && \
    rm powershell-lts_7.2.1-1.deb_amd64.deb