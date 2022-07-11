
export AWS_REGION=us-east-1
export AWS_PROFILE=mfa
export AS_USER=evanc
export EDITOR="code -w"
alias dev='cd ~/dev'
alias cam='cd ~/camel'
alias repo='cd ~/TheHomeRepot'
alias tools='cd ~/TheHomeRepot/lib/python/ActiveStatePlatform/tools'
export THR_ROOT=/Users/evanc/TheHomeRepot

function plat() {
    if [ -n "$1" ]
    then
    case $1 in
        "prod")
        export AS_PLATFORM=$1
        export PS1="[\[\e[36m\]\D{%F-%T}\[\e[m\]-\[\e[31m\][${AS_PLATFORM}]\[\e[m\]\[\e[122m\]-\W\[\e[m\]]$"
        echo "You are now on production."
        ;;
        "staging")
        export AS_PLATFORM=$1
        export PS1="[\[\e[36m\]\D{%F-%T}\[\e[m\]-\[\e[35m\][${AS_PLATFORM}]\[\e[m\]\[\e[122m\]-\W\[\e[m\]]$"
        echo "You are now on staging."
        ;;
        "pr"*)
        export AS_PLATFORM=$1
        export PS1="[\[\e[36m\]\D{%F-%T}\[\e[m\]-\[\e[35m\][${AS_PLATFORM}]\[\e[m\]\[\e[122m\]-\W\[\e[m\]]$"
        echo "You are now on $AS_PLATFORM."
        ;;
        *)
        echo "I cannot set that platform."
        ;;
    esac

    else
        unset AS_PLATFORM
        echo "AS_PLATFORM unset"
        export PS1="[\[\e[36m\]\D{%F-%T}\[\e[m\]-\W\[\e[m\]]$"
    fi
    export EDITOR=nano
}
function PR-DEPLOY() {
       USER=$AS_USER pr-deploy
}

function PR() {
       plat $1;
       echo -e "$AS_USER\n" | python3 ~/TheHomeRepot/lib/python/ActiveStatePlatform/tools/apikey.py new;
}
# -- START ACTIVESTATE INSTALLATION
export PATH="/Users/evanc/.local/ActiveState/StateTool/release/bin:$PATH"
# -- STOP ACTIVESTATE INSTALLATION
# -- START ACTIVESTATE DEFAULT RUNTIME ENVIRONMENT
export PATH="/Users/evanc/Library/Caches/activestate/bin:$PATH"
# -- STOP ACTIVESTATE DEFAULT RUNTIME ENVIRONMENT
