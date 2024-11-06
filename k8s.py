from kubernetes import client, config

# Load the kubeconfig file
config.load_kube_config()

# Create an instance of the AppsV1Api
apps_v1 = client.AppsV1Api()

# Define the namespace and deployment name
namespace = 'default'
deployment_name = 'myapp-deployment'

# Get the current deployment
deployment = apps_v1.read_namespaced_deployment(name=deployment_name, namespace=namespace)

# Update the number of replicas
deployment.spec.replicas = 5

# Apply the update
apps_v1.patch_namespaced_deployment(name=deployment_name, namespace=namespace, body=deployment)

print(f"Scaled deployment {deployment_name} to 5 replicas")