# Ansible Setup
Makes the most sense to run from a Linux server, or with WSL.  It's basically broken in some degree on Windows, even though there's a Python library that can isntall on Windows.

## WSL Setup

1. Enable WSL feature:
   - Open the Windows Start menu and search for "Turn Windows features on or off."
   - Click on the search result that says "Turn Windows features on or off."
   - In the Windows Features dialog box, scroll down and locate "Windows Subsystem for Linux."
   - Check the box next to it and click "OK."
   - Restart your computer when prompted.

2. Install a Linux distribution:
   - Open the Microsoft Store from the Start menu.
   - Search for the Linux distribution you want to install (e.g., Ubuntu, Debian, or OpenSUSE).
   - Select the distribution you prefer and click "Install" or "Get."
   - Wait for the installation to complete.

3. Set up your Linux distribution:
   - Launch your installed Linux distribution from the Start menu or any other location.
   - The first time you run it, it will take some time to initialize. It will ask you to create a new username and password for your Linux environment.
   - Follow the prompts to set up your Linux environment.

## Installing Ansible

Once your WSL environment is set up, follow these steps to install Ansible:

1. Open a terminal in your WSL distribution.

2. Run the following commands to update and upgrade your system packages:

```bash
sudo apt update
sudo apt upgrade
```
3. Install Ansible using the package manager:

```bash
sudo apt install ansible
```


## Adding an SSH Key

To allow Ansible to use SSH for remote connections, you need to add your SSH key. 
1. Open a terminal in your WSL distribution.
2. Copy your SSH key into .ssh
3. Set correct permissions 
```shell
   chmod 600 /home/TGSAdmin/.ssh/TGSAdmin
   chown $(whoami) /home/TGSAdmin/.ssh/TGSAdmin
```

4. Run the following command to start the SSH agent:
```bash
eval "$(ssh-agent -s)"
```
5. Add your SSH key to the SSH agent:
```bash
 ssh-add /home/TGSAdmin/.ssh/TGSAdmin
 ```

## Example Inventory file
```
steve_servers:
  hosts:
    10.0.2.129:
    10.0.2.131:
  vars:
    ansible_user: TGSAdmin
    ansible_ssh_common_args: '-o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i /home/TGSAdmin/.ssh/TGSAdmin'
```

## Adding Arguments
```bash
ansible-playbook new_bot.yaml -e "ExecStart=" -e "WorkingDirectory=" -e "Service_Description=" -e "app_name=" -e "destination_folder=" -e "GH_KEY="

ansible-playbook Deploy_CentOS_Template.yaml -e "vcenter_username=" -e "vm_name=" -e "template_name=" -e "datastore_name=" -e "esxi_host="

```

