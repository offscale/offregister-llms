"""
Shared routines for installing on Fedora based distributions including: RHEL; CentOS; RockyLinux
"""

from offregister_fab_utils.dnf import dnf_depends


def llm_dependencies(c):
    """
    Install LLM dependencies

    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    repo = "https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo"
    if not c.run("yum repolist cuda-rhel8-x86_64 --enabled", hide=True).stdout:
        c.sudo("dnf config-manager --add-repo {repo}".format(repo=repo))
        c.sudo("dnf clean all")
    if (
        c.run(
            "dnf module list --quiet --enabled nvidia-driver", hide=True, warn=True
        ).exited
        != 0
    ):
        c.sudo("dnf -y module install --skip-broken nvidia-driver:latest-dkms")
    dnf_depends(c, "python3", "cuda")  # c.sudo('dnf -y install cuda')


__all__ = ["llm_dependencies"]
