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
      - Cloudd or on premises
      - Scalability requirement
      - Pay as you go fixed pricing
      - Linux or Windows container

#### Sizing Docker
Before you run containerized app with Docker in production, you want to know the size of the hardware that will be required. If you only want to run the Docker Engine(development environment), you simply need to make sure you meet the minimum resource requirements of your host OS, in most cases. However, to run Docker containers in production, the sizing of the hardware will vary greatly based on the workload (the containers that contains your application and data). 

> Note: Universal Control Plane (UCP) and Docker Trusted Registry (DTR) have very dfferent sizing guidelines than the Docker Engine.

- ##### UCP Sizing
  - ###### Minimum requirements
    - 8 GB of RAM for manager nodes or nodes running DTR
    - 4 GB of RAM for worker nodes
    - 3 GB of free disk space
  
  - ###### Recommendation for production requirements
    - 16 GB of RAM for manager nodes or nodes running DTR
    - 4 vCPU for manager nodes or nodess running DTR
    - 25-100 GB of free disk space
  > Windows images require much space disk space than Linu images. 
