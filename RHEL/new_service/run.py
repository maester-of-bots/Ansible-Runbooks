import subprocess

# Example usage
playbook = '/mnt/e/Ansible-Runbooks/new_service/new_bot.yaml'

vars = {
    'app_name': 'TGS-RBOT-HotFuzz',
    'destination_folder': '/home/TGSAdmin/apps/reddit/TGS-RBOT-HotFuzz',
    'GH_KEY': ''
}

command = f'wsl ansible-playbook {playbook}'

# Append variables to the command
for key, value in vars.items():
    command += f' -e "{key}={value}"'

print(command)
