Helm — configuration tool used for  workload and application configuration management
Used as a package manager automates the process of installing, configuring, upgrading, and removing defined workload for k8s. Two key basic resources of k8s are part of default Helm Chart — Deployment & Services.
Used to automate the installation, configuration and upgrade and removing of Applications. The App and its Configuration are package in a so-called Chart.
Helm run as a CLI client for k8s and Chart is the application package. Chart maintain version as separate release and used for run-time change of application.

Benefits of Helm
o Deploy all the resources with a single command, specially used for k8s.
o Use variables to deploy same App with new parameters for different purpose.
o To upgrade to a new version of your chart with simple update to file.
o To automate software installation & upgrade. Ex — Database software, Apache web server, and integration software packed under IBM Cloud Pak.
o Used for dependency management in single place within Chart.


designating a target, which may be a host or group of hosts.
Designed to install and manage software on existing servers.
Able to declare the precise configuration results and then produce
Benefits of Ansible
o operation to run asynchronously such that the status may be checked. This can prevent interruption from SSH timeouts for long running operations.
o Used as Enterprise framework for various configuration management topics. Below picture depict various use cases for Ansible and has over 450+ ready-made module contributed by Red Hat. With Ansible, following can be automated:
![image](https://user-images.githubusercontent.com/6136987/150148608-a0343383-a751-4d13-856c-bc59c68557fc.png)


Terraform — Provisioning tool and run as Infrastructure as Code (IaC) software. 
define infrastructure components which can create an execution plan to build the infrastructure in a service provider such as AWS

Some of the Specific are:
Provides Terraform templates to provision various infrastructures.
Use to provide script to automate cloud instance creation and configuration.
generates an execution plan describing what it will do to reach the desired state, and then executes it to build the described infrastructure.
The infrastructure Terraform can manage includes low-level components such as compute instances, storage, and networking, as well as high-level components such as DNS entries, SaaS features, etc.

Benefits
o Handle the Server Orchestration, not merely configuration.
o Build Immutable infrastructure to avoid affecting existing instance of server.
o Using Declarative tool (template) with simple base code to meet desired state of various clouds.
o Follow Client-only architecture by using Cloud provider’s API for provisioning the infrastructure, which removes the need for additional security checks, running a separate configuration management server and multiple software agents.
Terraform in Cloud Platform — {IBM Cloud : an Example Use case}
o Provision the infrastructure on IBM Cloud — compute, storage, network, load balancers & IAM resources on IBM Cloud Infrastructure.
o Deploy OpenShift Container Platform on IBM Cloud.
o Setup users and authentication roles for OpenShift cluster.
