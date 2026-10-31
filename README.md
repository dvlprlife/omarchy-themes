# omarchy-themes

My custom [Omarchy](https://omarchy.org/) themes.

| Theme | Mode | Notes |
|-------|------|-------|
| [coach-prawny](coach-prawny/) | light | Palette from coachprawny.com: paper, ink, prawn orange, board green |

## Use

Each folder is one theme. Link it into Omarchy's themes directory and apply it:

```bash
ln -s ~/Work/omarchy-themes/coach-prawny ~/.config/omarchy/themes/coach-prawny
omarchy theme set "Coach Prawny"
```

Only `colors.toml` is required. Omarchy generates the terminal, Neovim, VS Code
and Hyprland configs from it when the theme is applied.
