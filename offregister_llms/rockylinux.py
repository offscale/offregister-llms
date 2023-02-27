"""
Install LLMs on Rocky Linux
"""

import posixpath

from patchwork.files import exists

from offregister_llms.fedora_shared import llm_dependencies


def install_llm0(c, *args, **kwargs):
    """
    :param c: Connection
    :type c: ```fabric.connection.Connection```
    """
    llm_dependencies(c)
    dnf_depends("git", "curl")
    repo_dir = "/etc/yum.repos.d"
    repo_file = "nvidia-container-toolkit.repo"
    repo_full_filepath = posixpath.join(repo_dir, repo_file)
    if not exists(c, c.sudo, repo_full_filepath):
        filename = "libnvidia-container.repo"
        url = "https://nvidia.github.io/libnvidia-container/centos8/{filename}".format(
            filename=filename
        )
        c.run("curl -s -L {url}".format(url=url))
        c.sudo(
            "mv {filename} {repo_full_filepath}".format(
                filename=filename, repo_full_filepath=repo_full_filepath
            )
        )
    dnf_depends("nvidia-docker2")
    return "Reboot your system if this is your first time running this command"


__all__ = ["install_llm0"]
