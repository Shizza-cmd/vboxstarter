import subprocess
import configparser



config = configparser.ConfigParser()
config.read("config.ini")


vm_name = config["virtual_machine"]["vm_name"]
vboxmanage = config["virtual_machine"]["vboxmanage_path"]


def start_vm(vm_name):
    try:
        subprocess.run([vboxmanage, "startvm", vm_name, "--type", "headless"], check=True)
        print(f"VM '{vm_name}' started successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to start VM '{vm_name}': {e}")

start_vm(vm_name)
