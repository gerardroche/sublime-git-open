# Copyright (C) 2023 Gerard Roche
#
# This file is part of GitOpen.
#
# GitOpen is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# GitOpen is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GitOpen.  If not, see <https://www.gnu.org/licenses/>.

import os
import subprocess
import sys

import sublime_plugin


class GitOpenCommand(sublime_plugin.WindowCommand):

    def run(self, commit: bool = False, issue: bool = False, remote: str = '', branch: str = '') -> None:
        view = self.window.active_view()
        if not view:
            return

        cwd = _get_cwd(view)
        if not cwd:
            return

        git_open_cmd = _get_git_open_cmd(commit, issue, remote, branch)

        cmd, shell = _get_args(view, git_open_cmd)
        subprocess.Popen(cmd, shell=shell, cwd=cwd)


def _get_git_open_cmd(commit: bool, issue: bool, remote: str, branch: str) -> str:
    cmd = ['git open']

    if remote:
        cmd.append(remote)

    if branch:
        cmd.append(branch)

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
