# syntax=docker/dockerfile:1.7
# LeaseLogic Development and Deployment Container
FROM ubuntu:22.04

# Set working directory
WORKDIR /workspace

# Make apt faster and more reliable
ARG DEBIAN_FRONTEND=noninteractive
# - Use Ubuntu mirror redirector for archive (fallback/rotation across mirrors)
# - Keep security on canonical security.ubuntu.com (more reliable)
# - Add retries/timeouts and force IPv4 (often faster/more reliable in CI)
ARG APT_ARCHIVE_MIRROR=mirror://mirrors.ubuntu.com/mirrors.txt
ARG APT_SECURITY_MIRROR=http://security.ubuntu.com/ubuntu/
RUN set -eux; \
    sed -i "s|http://archive.ubuntu.com/ubuntu/|${APT_ARCHIVE_MIRROR}|g" /etc/apt/sources.list; \
    sed -i "s|http://jp.archive.ubuntu.com/ubuntu/|${APT_ARCHIVE_MIRROR}|g" /etc/apt/sources.list || true; \
    sed -i "s|http://ftp.jaist.ac.jp/pub/Linux/ubuntu/|${APT_ARCHIVE_MIRROR}|g" /etc/apt/sources.list || true; \
    sed -i "s|http://security.ubuntu.com/ubuntu/|${APT_SECURITY_MIRROR}|g" /etc/apt/sources.list; \
    printf 'Acquire::Retries "10";\nAcquire::http::Timeout "20";\nAcquire::https::Timeout "20";\nAcquire::ForceIPv4 "true";\nAcquire::Languages "none";\n' > /etc/apt/apt.conf.d/99speed

# Install .NET SDK 8.0
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends wget ca-certificates gnupg lsb-release apt-transport-https; \
    wget -q https://packages.microsoft.com/config/ubuntu/22.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb; \
    dpkg -i packages-microsoft-prod.deb; \
    rm -f packages-microsoft-prod.deb; \
    apt-get update; \
    apt-get install -y --no-install-recommends dotnet-sdk-8.0

# Install essential system packages
# + Japanese fonts & fontconfig for proper PDF/PPTX rendering in headless Chrome
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        curl \
        wget \
        unzip \
        zip \
        git \
        jq \
        procps \
        gnupg \
        lsb-release \
        ca-certificates \
        apt-transport-https \
        sudo \
        emacs \
        libreoffice \
        fontconfig \
        locales \
        fonts-noto-cjk \
        fonts-noto-color-emoji \
        fonts-ipafont-gothic \
        fonts-ipafont-mincho \
        && locale-gen ja_JP.UTF-8 && update-locale LANG=ja_JP.UTF-8 && \
        fc-cache -f -v

# Install Google Chrome
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    bash -lc 'set -eux; wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -; \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends google-chrome-stable'

# Install Node.js 20.x
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    bash -lc 'set -eux; curl -fsSL https://deb.nodesource.com/setup_20.x | bash -; \
    apt-get install -y --no-install-recommends nodejs'

# Global npm packages (installed after Node.js)
RUN --mount=type=cache,target=/root/.npm \
    npm install -g @marp-team/marp-cli @openai/codex

# Install Azure CLI
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    bash -lc 'set -eux; curl -sL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > /etc/apt/trusted.gpg.d/microsoft.gpg; \
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $(lsb_release -cs) main" > /etc/apt/sources.list.d/azure-cli.list; \
    apt-get update; \
    apt-get install -y --no-install-recommends azure-cli'

# Install PowerShell 7
RUN --mount=type=cache,target=/var/lib/apt/lists,sharing=locked \
    --mount=type=cache,target=/var/cache/apt,sharing=locked \
    apt-get update && apt-get install -y --no-install-recommends powershell

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
ENV LANG=ja_JP.UTF-8
ENV LC_ALL=ja_JP.UTF-8

# Default command
CMD ["/bin/bash"]

# Labels
LABEL description="LeaseLogic Development and Deployment Container" \
      version="1.0" \
      tools="dotnet-sdk-8.0,nodejs-20.x,azure-cli,powershell-7,azure-functions-core-tools,bicep"
