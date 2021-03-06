#!/bin/bash
#
#  Copyright (c) 2022, Seqera Labs.
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
#  This Source Code Form is "Incompatible With Secondary Licenses", as
#  defined by the Mozilla Public License, v. 2.0.
#
#

# Tag and and push the the GitHub repo and Docker images
#
# - The tag is taken from the `VERSION` file in the project root
# - The tagging is enabled using putting the string `[release]` in the
#   commit comment
# - Use the string `[force release]` to override existing tag/images
#
set -e
set -x
SED=sed
[[ $(uname) == Darwin ]] && SED=gsed
# check for [release] [force] and [enterprise] string in the commit comment
FORCE=${FORCE:-$(git show -s --format='%s' | $SED -rn 's/.*\[(force)\].*/\1/p')}
RELEASE=${RELEASE:-$(git show -s --format='%s' | $SED -rn 's/.*\[(release)\].*/\1/p')}
REMOTE=https://oauth:$GITHUB_TOKEN@github.com/${GITHUB_REPOSITORY}.git
ENTERPRISE=${ENTERPRISE:-$(git show -s --format='%s' | $SED -rn 's/.*\[(enterprise)\].*/\1/p')}
MARKETPLACE=${MARKETPLACE:-$(git show -s --format='%s' | $SED -rn 's/.*\[(marketplace)\].*/\1/p')}

if [[ $RELEASE ]]; then
  # take the version from the `VERSION` file
  TAG=v$(cat VERSION)
  [[ $FORCE == 'force' ]] && FORCE='-f'
  # tag repo
  git tag $TAG $FORCE
  git push $REMOTE $TAG $FORCE
  # push it
  make push
fi
