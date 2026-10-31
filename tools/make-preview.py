#!/usr/bin/env python3
"""Render <theme>/preview.png: the first wallpaper with a mock terminal in the theme's colors.

Usage: tools/make-preview.py <theme-dir>
Needs ImageMagick, rsvg-convert and JetBrainsMono Nerd Font.
"""
import re
import subprocess
import sys
import tempfile
from html import escape
from pathlib import Path

W, H = 1800, 1012
X0, Y0, X1, Y1 = 1170, 500, 1760, 950
FONT = "JetBrainsMono Nerd Font"

theme = Path(sys.argv[1]).resolve()
text = (theme / "colors.toml").read_text()
c = {k: f"#{v}" for k, v in re.findall(r'^(\w+) = "#([0-9a-fA-F]{6})"', text, re.M)}
border = re.search(r'hyprland_active_border = "rgba\((\w{6})', text)
edge = f"#{border.group(1)}" if border else c["accent"]
wallpaper = sorted((theme / "backgrounds").iterdir())[0]

lines = [
    [("~/themes", "blue"), (" on ", "foreground"), ("main", "magenta"), (" ❯ ", "green"), ("omarchy theme current", "foreground")],
    [(theme.name, "accent")],
    [],
    [("~/themes", "blue"), (" ❯ ", "green"), ("ls", "foreground")],
    [("backgrounds/  ", "blue"), ("colors.toml  ", "foreground"), ("screensaver.txt", "foreground")],
    [],
    [("error", "red"), ("  warning", "orange"), ("  ok", "green"), ("  info", "cyan"), ("  muted", "muted")],
]
swatches = ["red", "orange", "yellow", "green", "cyan", "blue", "magenta", "brown"]

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}">',
       '<defs><filter id="s" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="18"/></filter></defs>',
       f'<rect x="{X0+6}" y="{Y0+16}" width="{X1-X0}" height="{Y1-Y0}" rx="14" fill="#000" opacity="0.45" filter="url(#s)"/>',
       f'<rect x="{X0}" y="{Y0}" width="{X1-X0}" height="{Y1-Y0}" rx="12" fill="{c["background"]}" stroke="{edge}" stroke-width="3"/>',
       f'<path d="M{X0+1.5},{Y0+44} V{Y0+13} a11.5,11.5 0 0 1 11.5,-11.5 H{X1-13} a11.5,11.5 0 0 1 11.5,11.5 V{Y0+44} Z" fill="{c["darker_background"]}"/>',
       f'<text x="{X0+24}" y="{Y0+29}" font-family="{FONT}" font-weight="bold" font-size="17" fill="{c["dark_foreground"]}">{escape(theme.name)}</text>']
y = Y0 + 96
for line in lines:
    spans = "".join(f'<tspan fill="{c[color]}">{escape(s)}</tspan>' for s, color in line)
    svg.append(f'<text x="{X0+32}" y="{y}" font-family="{FONT}" font-size="20" xml:space="preserve">{spans}</text>')
    y += 38
sw = (X1 - X0 - 64) // len(swatches)
for i, name in enumerate(swatches):
    svg.append(f'<rect x="{X0+32+i*sw}" y="{Y1-80}" width="{sw-8}" height="40" rx="4" fill="{c[name]}"/>')
svg.append("</svg>")

with tempfile.TemporaryDirectory() as tmp:
    overlay = Path(tmp) / "overlay.png"
    subprocess.run(["rsvg-convert", "-o", str(overlay)], input="\n".join(svg).encode(), check=True)
    subprocess.run(["magick", str(wallpaper), "-resize", f"{W}x{H}^", "-gravity", "center", "-extent", f"{W}x{H}",
                    str(overlay), "-composite", "-strip", str(theme / "preview.png")], check=True)
print(theme / "preview.png")
