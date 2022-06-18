#
# Test GitHub Action locally
# https://github.com/nektos/act
#
act \
 --container-architecture linux/amd64 \
 -e act.json \
 -s AWS_ACCESS_KEY_ID \
 -s AWS_SECRET_ACCESS_KEY \
 -s GITHUB_TOKEN
