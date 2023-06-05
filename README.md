# GitOpen

[`git-open`](https://github.com/paulirish/git-open) integration for Sublime Text.

## Setup

1. Install [`git-open`](https://github.com/paulirish/git-open).
2. Install [GitOpen](https://packagecontrol.io/packages/GitOpen) via Package Control.

## Commands

Command                     | Description
:---------------------------| :----------
**GitOpen&nbsp;**           | Open the page for this branch on the repo website
**GitOpen:&nbsp;Commit**    | Open the current commit in the repo website
**GitOpen:&nbsp;Issue**     | If this branch is named like issue/\#123, this will open the corresponding issue in the repo website

The `git_open` command accepts the following arguments:

Argument | Type
:--------|:-----
`commit` | `bool`
`issue` | `bool`
`remote` | `str`
`branch` | `str`

Example:

```js
{
    "caption": "GitOpen: Upstream",
    "command": "git_open",
    "args": {
        "remote": "upstream",
        "branch": "master"
    }
},
```

## License

Released under the [GPL-3.0-or-later License](LICENSE).
