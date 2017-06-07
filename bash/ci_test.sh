#TRAVIS_REPO_SLUG="michaeldayreads/k8s-bigip-ctlr"
#DOCKER_U="foo"
#DOCKER_P="baz"

if ["$TRAVIS_REPO_SLUG" == "F5Networks/k8s-bigip-ctlr"]; then
    echo "docker login"
else
    echo "[INFO]: Not an 'F5Networks' commit, docker optional."
    if [ "$DOCKER_P" == "" -o "$DOCKER_U" == "" ]; then
        echo "[INFO]: DOCKER_U and/or DOCKER_P environment var absent. Add to travis to push to docker."
    else
        echo "[INFO]: Images will be pushed to https://hub.docker.com/u/$DOCKER_U/"
    fi
fi

if [ "$DOCKER_P" != "" -a "$DOCKER_U" != "" ]; then
    echo "we should be able to push to docker..."
else
    echo "d'oh! logic busted!"
fi
