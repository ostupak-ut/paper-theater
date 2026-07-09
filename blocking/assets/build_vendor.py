#!/usr/bin/env python3
"""Build assets/vendor/katex-inline.html — a fully self-contained KaTeX fragment.

Input:  a KaTeX dist directory (katex.min.css, katex.min.js, fonts/*.woff2),
        e.g. from `npm pack katex && tar xzf katex-*.tgz` -> package/dist.
Output: vendor/katex-inline.html = <style> with every font inlined as a
        base64 data: URI (woff2 only; woff/ttf fallbacks dropped) + <script>.
The blocking skill concatenates this fragment into every emitted map, so the
artifact stays offline- and CSP-safe. Re-run only to upgrade KaTeX.

Usage: python3 build_vendor.py /path/to/katex/dist
"""
import base64, pathlib, re, sys

dist = pathlib.Path(sys.argv[1])
here = pathlib.Path(__file__).parent
out = here / "vendor"
out.mkdir(exist_ok=True)

css = (dist / "katex.min.css").read_text()

# Each font family appears as: src:url(fonts/X.woff2) format("woff2"),url(...woff)...,url(...ttf)...
# Keep ONLY the woff2 source, inlined.
def inline(m):
    name = m.group(1)
    data = base64.b64encode((dist / "fonts" / f"{name}.woff2").read_bytes()).decode()
    return f'src:url(data:font/woff2;base64,{data}) format("woff2")'

css = re.sub(
    r'src:url\(fonts/([\w-]+)\.woff2\) format\("woff2"\)[^;}]*',
    inline, css)
assert "url(fonts/" not in css, "unresolved font URL remains"

js = (dist / "katex.min.js").read_text()
version = re.search(r'"version":"([^"]+)"', js)
version = version.group(1) if version else "unknown"

frag = (f"<!-- KaTeX {version} · self-contained (woff2 inlined) · built by build_vendor.py -->\n"
        f"<style>\n{css}\n</style>\n<script>\n{js}\n</script>\n")
(out / "katex-inline.html").write_text(frag)
print(f"vendor/katex-inline.html: {len(frag)/1024:.0f} KB (KaTeX {version})")
