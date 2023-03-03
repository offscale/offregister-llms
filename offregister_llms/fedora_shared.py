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
    uname_r = c.run("uname -r").stdout

    dnf_depends(
        c,
        "kernel-devel-{uname_r}".format(uname_r=uname_r),
        "kernel-headers-{uname_r}".format(uname_r=uname_r),
    )
    if c.run("rpm --quiet -q epel-release").failed:
        c.sudo(
            "dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm"
        )

    distro = "rhel9"
    arch = " x86_64"
    repo = "https://developer.download.nvidia.com/compute/cuda/repos/{distro}/{arch}/cuda-{distro}.repo".format(
        distro=distro, arch=arch
    )
    c.sudo("dnf config-manager --add-repo {repo}".format(repo=repo))
    c.sudo("dnf clean expire-cache")
    c.sudo("dnf module install nvidia-driver:latest-dkms")
    dnf_depends(c, "python3", "cuda")

    repo_name = "docker-ce"
    repo = "dnf config-manager --add-repo https://download.docker.com/linux/centos/{repo_name}.repo".format(
        repo_name=repo_name
    )
    if not c.run(
        "yum repolist {repo_name} --enabled".format(repo_name=repo_name)
    ).stdout:
        c.sudo("dnf config-manager --add-repo {repo}".format(repo=repo))
    dnf_depends(
        c, "docker-ce", "docker-ce-cli", "containerd.io", "docker-compose-plugin"
    )


__all__ = ["llm_dependencies"]
