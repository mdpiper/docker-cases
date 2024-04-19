# multiplatform

An example of a multiplatform Docker build.

Build `arm64` and `amd64` images under a single tag,
then push them to Docker Hub, with:
```dockerfile
docker buildx build --platform linux/amd64,linux/arm64 -t mdpiper/multiplatform:latest --push .
```
