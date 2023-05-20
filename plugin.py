import os
import subprocess
import sys

import sublime_plugin


class GitOpenCommand(sublime_plugin.WindowCommand):

    def run(self, commit: bool = False, issue: bool = False) -> None:
        view = self.window.active_view()
        if not view:
            return

        cwd = _get_cwd(view)
        if not cwd:
            return

        cmd, shell = _get_args(view, _get_git_open_cmd(commit, issue))
        subprocess.Popen(cmd, shell=shell, cwd=cwd)


def _get_git_open_cmd(commit: bool, issue: bool) -> str:
    cmd = ['git-open']
    if commit:
        cmd.append('--commit')
    elif issue:
        cmd.append('--issue')

    return ' '.join(cmd)


def _get_args(view, shell_cmd: str) -> tuple:
    if sys.platform == "win32":
        shell = True
        cmd = shell_cmd
    elif sys.platform == "darwin":
        cmd = ["/usr/bin/env", "bash", "-l", "-c", shell_cmd]
        shell = False
    elif sys.platform == "linux":
        cmd = ["/usr/bin/env", "bash", "-c", shell_cmd]
        shell = False

    return (cmd, shell)


def _get_cwd(view):
    file_name = view.file_name()
    if not file_name:
        return

    cwd = os.path.dirname(view.file_name())
    if not os.path.isdir(cwd):
        return

    return cwd
