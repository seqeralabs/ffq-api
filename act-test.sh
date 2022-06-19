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
