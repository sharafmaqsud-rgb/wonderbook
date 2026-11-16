#!/usr/bin/env python3
"""Builds the standalone site in docs/ from index.html (the app source, written as page content)."""
import pathlib, shutil
root = pathlib.Path(__file__).parent
body = (root / "index.html").read_text()
head = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#FF2A85">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Wonderbook">
<meta name="robots" content="noindex">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="icon.svg">
<style>:root{color-scheme:light;padding:env(safe-area-inset-top,0px) 0 env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head><body>
"""
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(head + body + "\n</body></html>\n")
shutil.copy(root / "countries-110m.json", root / "docs" / "countries-110m.json")
print("built docs/index.html")
