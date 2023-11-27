# Ansible and vCenter

Ansible talks to vCenter through the web API, as opposed to running commands directly on the server.  Therefore, these can be run with just localhost, no inventory needed.


## Gather Facts [All]
This serves as a good "test" for verifying connectivity to vCenter.  It goes out and grabs information about the vCenter server and VMs / hosts.

```ansible-playbook Gather_Facts_All.yaml``` 


## Gather Facts [Specific]
This gets information about a specific VM, template, or host.  Useful for verifying if you're using the right information.

```ansible-playbook Gather_Facts_Specific.yaml``` 

## Deploying a CentOS Template
This deploys a template to an ESXI server.