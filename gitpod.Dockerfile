FROM gitpod/workspace-full

# Installez les dépendances spécifiques
RUN sudo apt-get update && sudo apt-get install -y \
    python3-pip \
    python3-venv

# Installez les extensions VS Code
RUN code --install-extension ms-python.python
