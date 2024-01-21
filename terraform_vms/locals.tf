locals {
  virtual_machines = {
    "vm1" = { vm_name = "sonar-01", vm_cpu = 2, vm_ram = 4, vm_disk_size = 10, vm_core_fraction = 20 },
    "vm2" = { vm_name = "nexus-01", vm_cpu = 2, vm_ram = 4, vm_disk_size = 10, vm_core_fraction = 20 }
  }

  vm_metadata  = {
    ssh-keys           = "centos:${file("~/.ssh/id_rsa.pub")}"
    serial-port-enable = 1
    ssh-user = "centos"
  }
}

