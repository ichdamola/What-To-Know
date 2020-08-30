#Instructions from this URL: https://cloud.google.com/sdk/docs/quickstart-debian-ubuntu
# Create environment variable for correct distribution
CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"

# Add the Cloud SDK distribution URI as a package source
echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list

# Import the Google Cloud Platform public key
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

# Update the package list and install the Cloud SDK
sudo apt-get update 
sudo apt-get install google-cloud-sdk

#Authenticate our console session with gcloud
gcloud init --console-only

#Create a named gcloud project
gcloud projects create psdemogke --name="Kubernetes-Cloud"

#Set our current project context
gcloud config set project psdemogke

#Enable GKE services in our current project
gcloud services enable container.googleapis.com

#You may have to adjust your resource limits and enabled billing here based on your subscription here.
#Go to https://console.cloud.google.com
#From the Navigation menu on the top left, browse to Compute->Kubernetes Engine.
#Click enable billing. Click Set Account.

#Tell GKE to create a single zone, three node cluster for us. 3 is the default size.
#https://cloud.google.com/compute/quotas#checking_your_quota
gcloud container clusters create cscluster --region us-central1-a

#Get our credentials for kubectl
gcloud container clusters get-credentials cscluster --zone us-central1-a --project psdemogke

#Check out out lists of kubectl contexts
kubectl config get-contexts

#set our current context to the GKE context
kubectl config use-context gke_psdemogke_us-central1-a_cscluster

#run a command to communicate with our cluster.
kubectl get nodes

#Delete our GKE cluster
#gcloud container clusters delete cscluster --zone=us-central1-a 

#Delete our project.
#gcloud projects delete psdemogke


#Get a list of all contexts on this system.
kubectl config get-contexts

#Let's set to the kubectl context back to our local custer
kubectl config use-context kubernetes-admin@kubernetes

#use kubectl get nodes
kubectl get nodes
