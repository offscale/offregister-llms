"""
Shared routines for installing on Fedora based distributions including: RHEL; CentOS; RockyLinux
"""


def llm_dependencies(c):
    """
    Install LLM dependencies

    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    repo = "https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo"
    c.sudo("dnf config-manager --add-repo {repo}".format(repo=repo))
    c.sudo("dnf clean all")
    c.sudo("dnf -y module install nvidia-driver:latest-dkms")
    dnf_depends("cuda")  # c.sudo('dnf -y install cuda')


__all__ = ["llm_dependencies"]
