# omarchy-themes

My custom [Omarchy](https://omarchy.org/) themes.

| Theme | Mode | Notes |
|-------|------|-------|
| [coach-prawny](coach-prawny/) | light | Palette from coachprawny.com: paper, ink, prawn orange, board green. COACH PRAWNY screensaver |
| [dvlprlife](dvlprlife/) | dark | From the dvlprlife avatar and dvlprlife.com: banner charcoal, site navy and teal. Avatar and pixel-shades wallpapers, dvlprlife screensaver |

## Use

Each folder is one theme. Link it into Omarchy's themes directory and apply it:

```bash
ln -s ~/Work/omarchy-themes/coach-prawny ~/.config/omarchy/themes/coach-prawny
omarchy theme set "Coach Prawny"
```

Only `colors.toml` is required. Omarchy generates the terminal, Neovim, VS Code
and Hyprland configs from it when the theme is applied.

## Screensaver

Omarchy's screensaver shows one global file, `~/.config/omarchy/branding/screensaver.txt`.
A theme here can ship its own `screensaver.txt`, and the hook in
`hooks/theme-set.d/` copies it into place whenever that theme is set. Themes
without one get the stock Omarchy logo back. Link the hook once:

```bash
ln -s ~/Work/omarchy-themes/hooks/theme-set.d/theme-screensaver.hook \
  ~/.config/omarchy/hooks/theme-set.d/theme-screensaver.hook
```

Keep the art about 84 columns wide or less so it fits the screensaver terminal.
To make new art, render a high-contrast SVG with
`omarchy transcode ascii <file.svg> screensaver.txt --width 84 --mode block`.
