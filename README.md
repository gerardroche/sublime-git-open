# GitOpen

[`git-open`](https://github.com/paulirish/git-open) integration for Sublime Text.

## Setup

1. Install [`git-open`](https://github.com/paulirish/git-open).
2. Install [GitOpen](https://packagecontrol.io/packages/GitOpen) via Package Control.

## Commands

Command                     | Description
:---------------------------| :----------
**GitOpen**                 | Open the page for this branch on the repo website
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

## NeoVintageous mappings

[NeoVintageous](https://github.com/NeoVintageous/NeoVintageous) is a Vim emulator for Sublime Text.

1. Open the Command Palette: `Command Palette → NeoVintageous: Open neovintageous file`.

2. Add your preferred mappings.

   **Example**

   ```vim
   nnoremap <leader>oo :GitOpen<CR>
   nnoremap <leader>oc :GitOpen commit=true<CR>
   nnoremap <leader>oi :GitOpen issue=true<CR>
   ```

3. To apply the changes, reload the neovintageousrc from the Command Palette: `Command Palette → NeoVintageous: Reload neovintageous file`.

## Changelog

See [CHANGELOG.md](CHANGELOG.md).

## License

Released under the [GPL-3.0-or-later License](LICENSE).
