# Dorker!
**[Docker](https://docs.docker.com/get-started)** is a platform for developers and sysadmins to build, run, and share applications with containers.

### Installation amd Configuration
Based on the Docker Certified Associate Exam **[study guide](https://docker.cdn.prismic.io/docker/4a619747-6889-48cd-8420-60f24a6a13ac_DCA_study+Guide_v1.3.pdf)**. For more info, check the **[website](https://success.docker.com/certification)**.


#### Dorker editions[#](https://docs.docker.com/get-docker/)
- Community edition 
- Enterprise edition 

#### Docker platforms
Check out the compatibility matrix for **[list](https://success.docker.com/article/compatibility-matrix)**.

  - ##### Considerations for selecting Docker platforms
      - Production or deelopment
      - Type of aapplication
      - Cloud or on premises
      - Scalability requirement
      - Pay as you go fixed pricing
      - Linux or Windows container

#### Sizing Docker
Before you run containerized app with Docker in production, you want to know the size of the hardware that will be required. If you only want to run the Docker Engine, you simply need to make sure you meet the minimum resource requirements of your host OS, in most cases, for development environment. However, to run Docker containers in production, the sizing of the hardware will vary greatly based on the workload (the containers that contains your application and data). 

> **Note:** Universal Control Plane [(UCP)](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/ucp.html) and Docker Trusted Registry [(DTR)](https://docs.mirantis.com/docker-enterprise/v3.0/dockeree-products/dtr.html) have very dfferent sizing guidelines than the Docker Engine.

- ##### UCP Sizing
  - ###### Minimum requirements
    - 8 GB of RAM for manager nodes or nodes running DTR
    - 4 GB of RAM for worker nodes
    - 3 GB of free disk space
  
  - ###### Recommendation for production requirements
    - 16 GB of RAM for manager nodes or nodes running DTR
    - 4 vCPU for manager nodes or nodess running DTR
    - 25-100 GB of free disk space
    
>**Note:** Windows images require much space disk space than Linu images. 

#### What is Docker Enginer?
DE is the heart of Docker, and when you think of Docker, you are actually thinking of Docker Engine. DE is designed as a server based client application, and it is made up of three different things which are:

  - ##### Dockerd or Docker deamon
    - This is installed when DOcker is installed, it is the Docker server itself.
  
  - ##### RESTFUL API
    - This is also installed along with the deamon. It defines the interface used by all other programs to talk to the Docker deamon, and other pieces that made up the Docker ecosystem incudong both tools from Docker, as well as third-party applications.
  
  - ##### Docker client (CLI)
    - This is the Docker commands run by clients to talk to the Docker server, pull down images, build images, and instantiate container. 
    
#### What is Docker namespace?
Namespaces are used by Docker Engine to isolate what is happening in the running conatainers from those containers the operationg system (hostOS) is running on. With namespaces, the kernel resources such as:
  - Process ID
  - User IDs
  - Network storage
  - Inner process communication
all the above can be virtualised and shared between the host OS and the running containers.

   - ##### Types of namespace in use by Docker.
     - Process
     - Mount
     - IPC
     - Network
     - User
namespaces are similar to hypervisor in term of merit.

#### Docker control groups
Used for controlling container resouces, primarily around CPU and memory.
  - ##### Used in Docker to control 
    - CPU limits
    - CPU reservations
    - Memory limits
    - Memory reservations
> ***Note:*** Using cgroup in linux requires strict kernel requirements.
