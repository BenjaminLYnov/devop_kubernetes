import os

os.system(" kubectl apply -f Configmap-multikeys.yaml && \
            kubectl apply -f devop303/Deployment-devop303.yml && \
            kubectl apply -f devop303/Service-devop303.yml && \
            kubectl apply -f devop303/Ingress-devop303.yml && \
            kubectl apply -f helloWorld/Deployment-helloWorld.yml && \
            kubectl apply -f helloWorld/Service-helloWorld.yml && \
            kubectl apply -f helloWorld/Ingress-helloWorld.yml && \
            kubectl apply -f redis/Deployment-Redis.yml && \
            kubectl apply -f redis/Service-Redis.yml && \
            kubectl apply -f quota/quota.yaml -n=hello-world && \
            kubectl apply -f quota/quota.yaml -n=devop303 \
        ")
