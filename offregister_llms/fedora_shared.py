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
    repo_name = "docker-ce"
    repo = "dnf config-manager --add-repo https://download.docker.com/linux/centos/{repo_name}.repo".format(
        repo_name=repo_name
    )
    cleaned = False

    for repo, repo_name in (
        (repo, repo_name),
        (
            "https://developer.download.nvidia.com/compute/cuda/repos/rhel8/x86_64/cuda-rhel8.repo",
            "cuda-rhel8-x86_64",
        ),
    ):
        if not c.run(
            "yum repolist {repo_name} --enabled".format(repo_name=repo_name), hide=True
        ).stdout:
            c.sudo("dnf config-manager --add-repo {repo}".format(repo=repo))
            if cleaned is False:
                c.sudo("dnf clean all")
                cleaned = True
    dnf_depends(
        c, "docker-ce", "docker-ce-cli", "containerd.io", "docker-compose-plugin"
    )

    if (
        c.run(
            "dnf module list --quiet --enabled nvidia-driver", hide=True, warn=True
        ).exited
        != 0
    ):
        c.sudo("dnf -y module install --skip-broken nvidia-driver:latest-dkms")
    dnf_depends(c, "python3", "cuda")  # c.sudo('dnf -y install cuda')


__all__ = ["llm_dependencies"]
