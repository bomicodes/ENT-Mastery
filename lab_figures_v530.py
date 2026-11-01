"""v53.0: draw the studies the Interpretation Atlas asks learners to read.

Audiograms, tympanograms, vHIT traces, caloric butterfly charts and ABR
waveforms are drawn as inline SVG from the numbers each case already states,
so the picture and the "Study data" text always agree.
"""
import math
from markupsafe import Markup, escape

FREQS = [250, 500, 1000, 2000, 4000, 8000]
FLAB = ["250", "500", "1k", "2k", "4k", "8k"]
RED, BLUE, INK, MUTED, GRID = "#c0392b", "#1f5fa8", "#16302f", "#6b7f80", "#dfe7e8"


def _svg(w, h, body, label):
    return Markup(
        f'<svg class="lab-fig" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(label)}" '
        f'xmlns="http://www.w3.org/2000/svg" font-family="Inter,system-ui,sans-serif">{body}</svg>'
    )


def audiogram(right_ac=None, left_ac=None, right_bc=None, left_bc=None, title="Audiogram"):
    """Thresholds in dB HL. AC lists follow 250-8k; BC lists follow 250-4k."""
    W, H, L, T, R, B = 380, 300, 46, 34, 14, 30
    pw, ph = W - L - R, H - T - B
    x = lambda i: L + pw * i / (len(FREQS) - 1)
    y = lambda db: T + ph * (db + 10) / 130
    g = [f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="#fff" stroke="{GRID}"/>']
    for db in range(-10, 121, 10):
        g.append(f'<line x1="{L}" y1="{y(db):.1f}" x2="{L+pw}" y2="{y(db):.1f}" stroke="{GRID}" stroke-width="{1.4 if db in (20, 40, 70, 90) else .8}"/>')
        g.append(f'<text x="{L-6}" y="{y(db)+3.5:.1f}" font-size="9.5" fill="{MUTED}" text-anchor="end">{db}</text>')
    for i, f in enumerate(FLAB):
        g.append(f'<line x1="{x(i):.1f}" y1="{T}" x2="{x(i):.1f}" y2="{T+ph}" stroke="{GRID}" stroke-width=".8"/>')
        g.append(f'<text x="{x(i):.1f}" y="{T-8}" font-size="10" fill="{MUTED}" text-anchor="middle">{f}</text>')
    g.append(f'<text x="4" y="{T-8}" font-size="9" fill="{MUTED}">Hz</text>')
    g.append(f'<text x="12" y="{T+ph/2}" font-size="10" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 12 {T+ph/2})">Hearing level (dB HL)</text>')

    def line(vals, color, dash=""):
        pts = [(x(i), y(v)) for i, v in enumerate(vals) if v is not None]
        if len(pts) > 1:
            d = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
            g.append(f'<polyline points="{d}" fill="none" stroke="{color}" stroke-width="1.6" {dash}/>')
        return pts

    for px, py in line(right_ac or [], RED):
        g.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="5" fill="#fff" stroke="{RED}" stroke-width="1.8"/>')
    for px, py in line(left_ac or [], BLUE):
        g.append(f'<path d="M{px-4.5:.1f},{py-4.5:.1f}l9,9M{px+4.5:.1f},{py-4.5:.1f}l-9,9" stroke="{BLUE}" stroke-width="1.8"/>')
    for i, v in enumerate(right_bc or []):
        if v is None:
            continue
        px, py = x(i) - 7, y(v)
        g.append(f'<path d="M{px+4:.1f},{py-5:.1f}L{px-3:.1f},{py:.1f}L{px+4:.1f},{py+5:.1f}" fill="none" stroke="{RED}" stroke-width="1.8"/>')
    for i, v in enumerate(left_bc or []):
        if v is None:
            continue
        px, py = x(i) + 7, y(v)
        g.append(f'<path d="M{px-4:.1f},{py-5:.1f}L{px+3:.1f},{py:.1f}L{px-4:.1f},{py+5:.1f}" fill="none" stroke="{BLUE}" stroke-width="1.8"/>')
    legend = (f'<g font-size="9.5" fill="{INK}"><circle cx="{L+8}" cy="{H-10}" r="4" fill="#fff" stroke="{RED}" stroke-width="1.6"/>'
              f'<text x="{L+16}" y="{H-7}">R air</text>'
              f'<path d="M{L+52},{H-14}l7,7M{L+59},{H-14}l-7,7" stroke="{BLUE}" stroke-width="1.6"/><text x="{L+64}" y="{H-7}">L air</text>'
              f'<text x="{L+98}" y="{H-7}" fill="{RED}">&lt; R bone</text><text x="{L+146}" y="{H-7}" fill="{BLUE}">&gt; L bone</text></g>')
    g.append(legend)
    return _svg(W, H, "".join(g), title)


def tympanogram(ears, title="Tympanogram"):
    """ears: list of (label, type, ecv_text). Types: A, As, Ad, B, C."""
    W, H, L, T, R, B = 380, 200, 40, 22, 14, 34
    pw, ph = W - L - R, H - T - B
    x = lambda p: L + pw * (p + 400) / 600
    yv = lambda c: T + ph * (1 - c / 2.0)
    g = [f'<rect x="{L}" y="{T}" width="{pw}" height="{ph}" fill="#fff" stroke="{GRID}"/>']
    for p in (-400, -300, -200, -100, 0, 100, 200):
        g.append(f'<line x1="{x(p):.1f}" y1="{T}" x2="{x(p):.1f}" y2="{T+ph}" stroke="{GRID}" stroke-width=".8"/>'
                 f'<text x="{x(p):.1f}" y="{T+ph+12}" font-size="9" fill="{MUTED}" text-anchor="middle">{p}</text>')
    for c in (0, .5, 1, 1.5, 2):
        g.append(f'<text x="{L-5}" y="{yv(c)+3:.1f}" font-size="9" fill="{MUTED}" text-anchor="end">{c:g}</text>')
    g.append(f'<rect x="{x(-100):.1f}" y="{yv(1.75):.1f}" width="{x(50)-x(-100):.1f}" height="{yv(0.3)-yv(1.75):.1f}" fill="#e7f3f1" opacity=".7"/>')
    g.append(f'<text x="{L+pw/2}" y="{H-6}" font-size="9.5" fill="{MUTED}" text-anchor="middle">Ear-canal pressure (daPa) · shaded box = normal Type A range</text>')
    g.append(f'<text x="10" y="{T+ph/2}" font-size="9.5" fill="{MUTED}" text-anchor="middle" transform="rotate(-90 10 {T+ph/2})">mL</text>')
    shapes = {"A": (0, 0.9, 70), "As": (0, 0.25, 70), "Ad": (0, 1.95, 60), "C": (-250, 0.8, 70), "B": (0, 0.06, 400)}
    colors = [RED, BLUE]
    for k, (label, typ, ecv) in enumerate(ears):
        peak_p, peak_c, width = shapes.get(typ, shapes["A"])
        if k:  # keep two identical curves from hiding each other
            peak_p, peak_c = peak_p + 12, peak_c * 0.9
        pts = []
        for p in range(-400, 201, 10):
            c = 0.12 + peak_c * math.exp(-((p - peak_p) / width) ** 2) if typ != "B" else 0.12 + 0.03 * (1 - abs(p + 100) / 300)
            pts.append(f"{x(p):.1f},{yv(min(c, 2)):.1f}")
        col = colors[k % 2]
        g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>')
        g.append(f'<text x="{L+pw-6}" y="{T+14+14*k}" font-size="10" fill="{col}" text-anchor="end" font-weight="700">{escape(label)}: Type {escape(typ)}{" · ECV " + escape(ecv) if ecv else ""}</text>')
    return _svg(W, H, "".join(g), title)


def vhit(right_gain, left_gain, left_saccade=False, right_saccade=False, title="vHIT, horizontal canals"):
    W, H = 380, 190
    g = []
    for k, (side, gain, sac, col) in enumerate((("Right", right_gain, right_saccade, RED), ("Left", left_gain, left_saccade, BLUE))):
        ox, T, pw, ph = 14 + k * 186, 26, 170, 120
        base = T + ph - 14
        g.append(f'<rect x="{ox}" y="{T}" width="{pw}" height="{ph}" fill="#fff" stroke="{GRID}"/>')
        g.append(f'<text x="{ox+pw/2}" y="{T-8}" font-size="11" font-weight="700" fill="{col}" text-anchor="middle">{side} horizontal · gain {gain:.2f}</text>')
        head, eye = [], []
        for t in range(0, 301, 6):
            v = math.exp(-((t - 90) / 38) ** 2)
            head.append(f"{ox+6+t*0.52:.1f},{base - v*88:.1f}")
            e = v * gain
            if sac:
                e += 0.55 * math.exp(-((t - 150) / 11) ** 2)
            eye.append(f"{ox+6+t*0.52:.1f},{base - e*88:.1f}")
        g.append(f'<polyline points="{" ".join(head)}" fill="none" stroke="{MUTED}" stroke-width="1.6" stroke-dasharray="4 3"/>')
        g.append(f'<polyline points="{" ".join(eye)}" fill="none" stroke="{col}" stroke-width="2"/>')
        if sac:
            g.append(f'<text x="{ox+6+150*0.52+6:.1f}" y="{base-60:.1f}" font-size="9.5" fill="{col}">overt saccade</text>')
    g.append(f'<text x="14" y="{H-10}" font-size="9.5" fill="{MUTED}">Dashed = head velocity · solid = eye velocity (inverted)</text>')
    return _svg(W, H, "".join(g), title)


def caloric(rw, rc, lw, lc, title="Bithermal calorics"):
    W, H, mid = 380, 200, 190
    mx = max(rw, rc, lw, lc, 30)
    s = 120 / mx
    g = [f'<line x1="{mid}" y1="20" x2="{mid}" y2="160" stroke="{GRID}" stroke-width="1.2"/>']
    rows = (("Right warm", rw, RED), ("Right cool", rc, RED), ("Left warm", lw, BLUE), ("Left cool", lc, BLUE))
    for i, (lab, v, col) in enumerate(rows):
        yy = 28 + i * 33
        right = lab in ("Right warm", "Left cool")  # COWS: these beat right; the other two beat left
        x0 = mid if right else mid - v * s
        g.append(f'<rect x="{x0:.1f}" y="{yy}" width="{v*s:.1f}" height="20" rx="3" fill="{col}" opacity="{.9 if lab.startswith("Right") else .75}"/>')
        tx = mid + v * s + 6 if right else mid - v * s - 6
        g.append(f'<text x="{tx:.1f}" y="{yy+14}" font-size="10" fill="{INK}" text-anchor="{"start" if right else "end"}">{lab} {v:g}°/s</text>')
    uw = round(abs((rw + rc) - (lw + lc)) / (rw + rc + lw + lc) * 100)
    weak = "left" if (lw + lc) < (rw + rc) else "right"
    g.append(f'<text x="{mid-6}" y="14" font-size="9.5" fill="{MUTED}" text-anchor="end">← left-beating</text><text x="{mid+6}" y="14" font-size="9.5" fill="{MUTED}">right-beating →</text>')
    g.append(f'<text x="{mid}" y="{H-14}" font-size="10" fill="{MUTED}" text-anchor="middle">Peak slow-phase velocity · unilateral weakness ≈ {uw}% {weak} (Jongkees)</text>')
    return _svg(W, H, "".join(g), title)


def abr(right, left, title="Click ABR"):
    """right/left: (I, III, V) latencies in ms."""
    W, H, L = 380, 210, 40
    x = lambda ms: L + (W - L - 14) * ms / 10
    g = []
    for ms in range(0, 11, 2):
        g.append(f'<line x1="{x(ms):.1f}" y1="20" x2="{x(ms):.1f}" y2="{H-36}" stroke="{GRID}" stroke-width=".8"/>'
                 f'<text x="{x(ms):.1f}" y="{H-24}" font-size="9.5" fill="{MUTED}" text-anchor="middle">{ms}</text>')
    g.append(f'<text x="{(W+L)/2}" y="{H-8}" font-size="9.5" fill="{MUTED}" text-anchor="middle">Latency (ms)</text>')
    for k, (side, lat, col) in enumerate((("R", right, RED), ("L", left, BLUE))):
        base = 70 + k * 72
        pts = []
        for i in range(0, 301):
            t = i / 30
            v = 0.15 * math.sin(t * 7.3) * math.exp(-t / 6)
            for amp, p in zip((0.55, 0.45, 0.95), lat):
                v += amp * math.exp(-((t - p) / 0.18) ** 2)
            v -= 0.5 * math.exp(-((t - lat[2] - 0.55) / 0.3) ** 2)
            pts.append(f"{x(t):.1f},{base - v*34:.1f}")
        g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="1.8"/>')
        g.append(f'<text x="{L-8}" y="{base+4}" font-size="11" font-weight="700" fill="{col}" text-anchor="end">{side}</text>')
        for name, p in zip(("I", "III", "V"), lat):
            g.append(f'<text x="{x(p):.1f}" y="{base-38}" font-size="9.5" fill="{col}" text-anchor="middle">{name} {p:g}</text>')
    return _svg(W, H, "".join(g), title)


def enog(normal_mv, affected_mv, day, title="Electroneurography (ENoG)"):
    """Supramaximal CMAPs, normal vs affected side; degeneration = 1 - affected/normal."""
    W, H, L = 380, 210, 40
    x = lambda ms: L + (W - L - 14) * ms / 20
    g = []
    for ms in range(0, 21, 5):
        g.append(f'<line x1="{x(ms):.1f}" y1="20" x2="{x(ms):.1f}" y2="{H-40}" stroke="{GRID}" stroke-width=".8"/>'
                 f'<text x="{x(ms):.1f}" y="{H-28}" font-size="9.5" fill="{MUTED}" text-anchor="middle">{ms}</text>')
    g.append(f'<text x="{(W+L)/2}" y="{H-14}" font-size="9.5" fill="{MUTED}" text-anchor="middle">ms after stimulus · day {day} after onset</text>')
    scale = 34 / max(normal_mv, affected_mv, 0.1)
    for k, (side, amp, col) in enumerate((("Normal", normal_mv, BLUE), ("Affected", affected_mv, RED))):
        base = 62 + k * 74
        pts = []
        for i in range(0, 401):
            t = i / 20
            v = amp * (math.exp(-((t - 5.2) / 1.1) ** 2) - 0.6 * math.exp(-((t - 7.6) / 1.5) ** 2))
            pts.append(f"{x(t):.1f},{base - v*scale:.1f}")
        g.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="{col}" stroke-width="2"/>')
        g.append(f'<text x="{L-6}" y="{base+4}" font-size="10" font-weight="700" fill="{col}" text-anchor="end">{side[0]}</text>')
        g.append(f'<text x="{W-14}" y="{base-20}" font-size="10" fill="{col}" text-anchor="end">{side}: {amp:g} mV</text>')
    deg = round(100 * (1 - affected_mv / normal_mv)) if normal_mv else 0
    g.append(f'<text x="{L}" y="14" font-size="10.5" font-weight="700" fill="{INK}">Degeneration ≈ {deg}%</text>')
    return _svg(W, H, "".join(g), title)


# Figures for existing cases, built from the values each case already states.
FIGURES = {
    "aud1": [lambda: audiogram([5, 5, 10, 5, 10, 10], [10, 5, 5, 10, 5, 15], [5, 5, 5, 5, 10], [5, 5, 5, 10, 5], "Normal audiogram"),
             lambda: tympanogram([("R", "A", ""), ("L", "A", "")])],
    "aud2": [lambda: audiogram([45, 50, 45, 40, 35, 30], [10, 10, 10, 10, 10, 10], [5, 5, 10, 10, 10], [10, 10, 10, 10, 10], "Right conductive loss"),
             lambda: tympanogram([("R", "B", "normal"), ("L", "A", "")])],
    "aud3": [lambda: audiogram([10, 15, 20, 35, 55, 65], [10, 15, 20, 35, 55, 60], [10, 15, 20, 35, 55], [10, 15, 20, 35, 55], "Symmetric downsloping SNHL")],
    "aud4": [lambda: audiogram([10, 10, 15, 20, 25, 30], [15, 20, 35, 55, 70, 75], [10, 10, 15, 20, 25], [15, 20, 35, 55, 70], "Asymmetric left SNHL")],
    "audnew1": [lambda: audiogram([10, 10, 15, 20, 45, 20], [10, 15, 15, 20, 50, 25], [10, 10, 15, 20, 45], [10, 15, 15, 20, 50], "Bilateral 4-kHz notch")],
    "audnew2": [lambda: audiogram([35, 30, 30, 30, 35, 35], [35, 35, 30, 30, 35, 35], [5, 10, 10, 5, 10], [10, 5, 10, 10, 10], "Bilateral mild conductive loss"),
                lambda: tympanogram([("R", "B", "normal"), ("L", "B", "normal")])],
    "a11": [lambda: tympanogram([("Ear", "B", "large (e.g., 3.5 mL)")], "Flat tympanogram, large ear-canal volume")],
    "a12": [lambda: tympanogram([("Ear", "B", "normal (e.g., 0.8 mL)")], "Flat tympanogram, normal ear-canal volume")],
    "vestnew2": [lambda: audiogram([40, 35, 30, 15, 15, 10], None, [40, 35, 30, 15, 15], None, "Right low-frequency SNHL")],
    "vest1": [lambda: caloric(25, 20, 10, 8)],
    "vest2": [lambda: vhit(0.95, 0.55, left_saccade=True)],
    "vestnew1": [lambda: vhit(0.95, 0.45, left_saccade=True)],
    "fn_enog92_v532": [lambda: enog(4.0, 0.3, 6, "ENoG day 6: 92% degeneration")],
    "fn_enog60_v532": [lambda: enog(3.6, 1.45, 5, "ENoG day 5: 60% degeneration")],
    "fn_tbfx_v532": [lambda: enog(3.8, 0.2, 4, "ENoG day 4 after temporal bone fracture")],
    "ae2": [lambda: abr((1.7, 4.1, 6.3), (1.6, 3.7, 5.4), "Click ABR: right I-V 4.6 ms, left 3.8 ms")],
}


def figures_for(case_id):
    return [f() for f in FIGURES.get(case_id, [])]
