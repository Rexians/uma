SYSTEM_SPEC=(uname -a)

if [ $1 = "deploy" ]
then
        echo "Updating System..."
        sudo apt update -y && sudo apt upgrade -y
        echo "Installing required packages..."
        sudo apt install curl git wget nano -y
        echo "Installing Python & PIP..."
        sudo apt install python pip -y
        echo "Getting System Information..."
        echo "Found! $SYSTEM_SPEC"
        echo "Git Cloning the REPO"
        git clone https://github.com/Rexians/uma.git
        echo "Enabling Node"
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash
        echo "Reloading Bash ..."
        source .bashrc
        export NVM_DIR="$HOME/.nvm"
        [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
        [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
        echo "Installing Nodejs & NPM"
        nvm install node 
        nvm install --lts
        sudo apt install npm
        echo "Installing PM2"
        sudo npm i -g pm2
        echo "Changing Directory..."
        cd uma/uma
        export PATH="$PATH:/home/default/.local/bin"
        echo "Installing Stuff"
        pip install -r requirements.txt
        echo "Everything finished!"
        echo "Starting App!"
        pm2 start "uvicorn api:app --host 0.0.0.0 --port 8080" --name uma
        echo "Poggers done!"
fi
