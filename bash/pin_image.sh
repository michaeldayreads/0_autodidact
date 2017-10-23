set -ex

CI_ORCHESTRATION=marathon
CI_PROJECT=bigip-ctlr
CI_BRANCH=docker-latest

DOCKER_IMG="michaeldayreads/$CI_ORCHESTRATION-$CI_PROJECT:devel-$CI_BRANCH"
docker pull $DOCKER_IMG

# method to find docker id, not using
#
# DOCKER_ID=(`docker images | grep "michaeldayreads/$CI_ORCHESTRATION-$CI_PROJECT" | \
#    grep " devel-$CI_BRANCH " | awk 'NR==1{print $3}'`)
# echo "Docker id: $DOCKER_ID"

DOCKER_TAG=(`docker inspect $DOCKER_IMG | grep BUILD_STAMP= | \
    cut -d "=" -f 2 | cut -d '"' -f 1`)

# this tag would be exported
echo "Docker tag: $DOCKER_TAG"

# simulate the use downstream of the tag being used to pull this precise image
docker rmi -f $DOCKER_IMG
docker pull michaeldayreads/$CI_ORCHESTRATION-$CI_PROJECT:$DOCKER_TAG

