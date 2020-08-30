#For this demo ssh into c1-node1
ssh aen@c1-node1

#Disable swap, swapoff then edit your fstab removing any entry for swap partitions
#You can recover the space with fdisk. You may want to reboot to ensure your config is ok. 
swapoff -a
vi /etc/fstab

#Add the Google's apt repository gpg key
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -

#Add the kuberentes apt repository
sudo bash -c 'cat <<EOF >/etc/apt/sources.list.d/kubernetes.list
deb https://apt.kubernetes.io/ kubernetes-xenial main
EOF'

#Update the package list 
sudo apt-get update
apt-cache policy kubelet | head -n 20 

#Install the required packages, if needed we can request a specific version
sudo apt-get install -y docker.io kubelet kubeadm kubectl
sudo apt-mark hold docker.io kubelet kubeadm kubectl

#Check the status of our kubelet and our container runtime, docker.
#The kubelet will enter a crashloop until it's joined
sudo systemctl status kubelet.service 
sudo systemctl status docker.service 

#Ensure both are set to start when the system starts up.
sudo systemctl enable kubelet.service
sudo systemctl enable docker.service

#Setup Docker daemon. This is a change that has been added since the recording of the course.
sudo bash -c 'cat > /etc/docker/daemon.json <<EOF
{
  "exec-opts": ["native.cgroupdriver=systemd"],
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "100m"
  },
  "storage-driver": "overlay2"
}
EOF'

sudo systemctl daemon-reload
sudo systemctl restart docker

#If you didn't keep the output, on the master, you can get the token.
kubeadm token list

#If you need to generate a new token, perhaps the old one timed out/expired.
kubeadm token create

#On the master, you can find the ca cert hash.
openssl x509 -pubkey -in /etc/kubernetes/pki/ca.crt | openssl rsa -pubin -outform der 2>/dev/null | openssl dgst -sha256 -hex | sed 's/^.* //'

#Using the master (API Server) IP address or name, the token and the cert has, let's join this Node to our cluster.
sudo kubeadm join 172.16.94.10:6443 \
    --token 9woi9e.gmuuxnbzd8anltdg \
    --discovery-token-ca-cert-hash sha256:f9cb1e56fecaf9989b5e882f54bb4a27d56e1e92ef9d56ef19a6634b507d76a9

#Back on master, this will say NotReady until the networking pod is created on the new node. Has to schedule the pod, then pull the container.
kubectl get nodes 

#On the master, watch for the calico pod and the kube-proxy to change to Running on the newly added nodes.
kubectl get pods --all-namespaces --watch

#Still on the master, look for this added node's status as ready.
kubectl get nodes

#GO BACK TO THE TOP AND DO THE SAME FOR c1-node2.
#Just SSH into c1-node2 and run the commands again.
ssh aen@c1-node2
#You can skip the token re-creation if you have one that's still valid.