registry ?= public.ecr.aws/seqera-labs
tag ?= $(shell cat VERSION)
platform ?= linux/amd64

build:
	docker buildx build \
		--platform ${platform} \
		-o type=docker \
		--tag ${registry}/ffq:${tag} \
		.

push:
	docker buildx build \
		--platform ${platform} \
		--push \
		--tag ${registry}/ffq:${tag} \
		.
