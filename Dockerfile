# LeaseLogic Development and Deployment Container
FROM mcr.microsoft.com/dotnet/sdk:8.0

# Set working directory
WORKDIR /workspace

# Install essential system packages
RUN apt-get update && \
    apt-get install -y \
        curl \
        wget \
        unzip \
        zip \
        git \
        vim \
        jq \
        procps \
        gnupg \
        lsb-release \
        ca-certificates \
        apt-transport-https \
        sudo \
        && rm -rf /var/lib/apt/lists/*

# Install Node.js 20.x
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash - && \
    apt-get install -y nodejs && \
    rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg && \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/azure-cli.list && \
    apt-get update && \
    apt-get install -y azure-cli && \
    rm -rf /var/lib/apt/lists/*

# Install PowerShell 7
RUN wget -q "https://packages.microsoft.com/config/debian/$(lsb_release -rs)/packages-microsoft-prod.deb" -O packages-microsoft-prod.deb && \
    dpkg -i packages-microsoft-prod.deb && \
    apt-get update && \
    apt-get install -y powershell && \
    rm packages-microsoft-prod.deb && \
    rm -rf /var/lib/apt/lists/*

# Install Azure PowerShell Module
RUN pwsh -Command "Set-PSRepository -Name 'PSGallery' -InstallationPolicy Trusted; Install-Module -Name Az -Scope AllUsers -Force"

# Install Bicep CLI
RUN curl -Lo bicep https://github.com/Azure/bicep/releases/latest/download/bicep-linux-x64 && \
    chmod +x ./bicep && \
    mv ./bicep /usr/local/bin/bicep

# Install Azure Functions Core Tools
RUN npm install -g azure-functions-core-tools@4 --unsafe-perm true
RUN npm install -g azurite

# Install global npm packages for development
RUN npm install -g typescript @anthropic-ai/claude-code
RUN npm install -g @google/gemini-cli

# Set .NET environment variables
ENV DOTNET_ROOT=/usr/share/dotnet
ENV DOTNET_CLI_TELEMETRY_OPTOUT=1
ENV DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
ENV DOTNET_NOLOGO=1
ENV PATH="$PATH:/usr/share/dotnet"

# Set up workspace and permissions (maintaining directory structure)
RUN mkdir -p /workspaces

# Configure bash environment for root user
RUN echo 'export PATH="/usr/share/dotnet:$PATH"' >> ~/.bashrc && \
    echo 'export DOTNET_ROOT="/usr/share/dotnet"' >> ~/.bashrc && \
    echo 'export DOTNET_CLI_TELEMETRY_OPTOUT=1' >> ~/.bashrc && \
    echo 'export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1' >> ~/.bashrc && \
    echo 'export DOTNET_NOLOGO=1' >> ~/.bashrc

# Configure PowerShell profile for root user
RUN mkdir -p /root/.config/powershell && \
    echo '# LeaseLogic PowerShell Profile' > /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo '$env:PATH = "$env:PATH:/usr/share/dotnet:/usr/local/bin:/usr/bin"' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo '$env:DOTNET_ROOT = "/usr/share/dotnet"' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo '$env:DOTNET_CLI_TELEMETRY_OPTOUT = "1"' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo '$env:DOTNET_SKIP_FIRST_TIME_EXPERIENCE = "1"' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo '$env:DOTNET_NOLOGO = "1"' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1 && \
    echo 'Set-PSRepository -Name PSGallery -InstallationPolicy Trusted' >> /root/.config/powershell/Microsoft.PowerShell_profile.ps1

# Environment variables
ENV WORKSPACE=/workspace

# Default command
CMD ["/bin/bash"]

# Labels
LABEL description="LeaseLogic Development and Deployment Container" \
      version="1.0" \
      tools="dotnet-sdk-8.0,nodejs-20.x,azure-cli,powershell-7,azure-functions-core-tools,bicep"