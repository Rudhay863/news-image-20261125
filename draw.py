#!/usr/bin/env python3
"""Draw the 25 November 2026 world-news summary image (1024x1024).

Fresh work for make.fun bounty news-image-20261125. All drawing is done
with Pillow primitives; no network, no timestamps, fully deterministic.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

PAPER = (247, 243, 234)
INK = (20, 24, 34)
NAVY = (18, 36, 62)
NAVY2 = (28, 54, 92)
CARD = (255, 255, 255)
MUTED = (90, 96, 110)
RED = (178, 34, 34)
GOLD = (201, 162, 39)
TEAL = (15, 118, 110)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Wrap text into lines that fit max_w pixels."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_rocket(d, x, y, s):
    """Simple rocket lifting off, in a sky-blue rounded square."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(23, 94, 158))
    # stars
    for sx, sy, r in [(0.18, 0.2, 3), (0.82, 0.16, 4), (0.78, 0.75, 3),
                      (0.14, 0.72, 3), (0.55, 0.1, 3)]:
        d.ellipse([x + s * sx - r, y + s * sy - r,
                   x + s * sx + r, y + s * sy + r], fill=(255, 255, 255))
    cx = x + s * 0.5
    # flame
    d.polygon([(cx - 13, y + s * 0.78), (cx + 13, y + s * 0.78),
               (cx, y + s * 0.97)], fill=(255, 140, 0))
    d.polygon([(cx - 7, y + s * 0.78), (cx + 7, y + s * 0.78),
               (cx, y + s * 0.9)], fill=(255, 220, 60))
    # body
    d.rounded_rectangle([cx - 18, y + s * 0.28, cx + 18, y + s * 0.78],
                        radius=12, fill=(240, 240, 240))
    d.polygon([(cx - 18, y + s * 0.38), (cx + 18, y + s * 0.38),
               (cx, y + s * 0.18)], fill=(200, 40, 40))
    d.ellipse([cx - 9, y + s * 0.42, cx + 9, y + s * 0.58],
              fill=(120, 200, 240), outline=(30, 60, 90), width=2)
    # fins
    d.polygon([(cx - 18, y + s * 0.62), (cx - 34, y + s * 0.8),
               (cx - 18, y + s * 0.78)], fill=(200, 40, 40))
    d.polygon([(cx + 18, y + s * 0.62), (cx + 34, y + s * 0.8),
               (cx + 18, y + s * 0.78)], fill=(200, 40, 40))


def draw_chart(d, x, y, s):
    """Falling market chart with a big red down arrow."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(245, 235, 225))
    # axes
    d.line([x + s * 0.14, y + s * 0.16, x + s * 0.14, y + s * 0.84],
           fill=(120, 120, 120), width=3)
    d.line([x + s * 0.14, y + s * 0.84, x + s * 0.88, y + s * 0.84],
           fill=(120, 120, 120), width=3)
    pts = [(0.18, 0.28), (0.34, 0.36), (0.46, 0.32), (0.60, 0.52),
           (0.72, 0.62), (0.84, 0.76)]
    coords = [(x + s * px, y + s * py) for px, py in pts]
    d.line(coords, fill=(178, 34, 34), width=6, joint="curve")
    for cx, cy in coords:
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=(178, 34, 34))
    # down arrow
    ax, ay = x + s * 0.72, y + s * 0.14
    d.polygon([(ax - 14, ay), (ax + 14, ay), (ax + 14, ay + 26),
               (ax + 26, ay + 26), (ax, ay + 52), (ax - 26, ay + 26),
               (ax - 14, ay + 26)], fill=(178, 34, 34))


def draw_lock(d, x, y, s):
    """Laptop with a padlock: a cyber breach."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(28, 42, 66))
    # laptop
    lx, ly, lw, lh = x + s * 0.2, y + s * 0.24, s * 0.6, s * 0.42
    d.rounded_rectangle([lx, ly, lx + lw, ly + lh], radius=8,
                        fill=(180, 210, 235))
    d.polygon([(lx - 10, ly + lh + 12), (lx + lw + 10, ly + lh + 12),
               (lx + lw, ly + lh), (lx, ly + lh)], fill=(140, 160, 185))
    # padlock on screen
    cx = lx + lw / 2
    d.arc([cx - 16, ly + 12, cx + 16, ly + 44], 180, 360,
          fill=(178, 34, 34), width=6)
    d.rounded_rectangle([cx - 22, ly + 34, cx + 22, ly + 62], radius=6,
                        fill=(178, 34, 34))
    d.ellipse([cx - 4, ly + 42, cx + 4, ly + 50], fill=(255, 255, 255))
    d.line([cx, ly + 48, cx, ly + 56], fill=(255, 255, 255), width=3)
    # warning zigzag
    d.line([(x + s * 0.12, y + s * 0.84), (x + s * 0.3, y + s * 0.72),
            (x + s * 0.48, y + s * 0.84), (x + s * 0.66, y + s * 0.72),
            (x + s * 0.88, y + s * 0.84)], fill=(255, 200, 40), width=4)


def draw_tower(d, x, y, s):
    """Skyscraper hit by a drone, with an impact burst."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(250, 238, 210))
    # tower
    tx, tw = x + s * 0.38, s * 0.3
    d.rectangle([tx, y + s * 0.22, tx + tw, y + s * 0.9],
                fill=(70, 90, 120))
    for row in range(6):
        for col in range(2):
            ww = (tw - 20) / 2
            wx = tx + 10 + col * ww
            wy = y + s * 0.28 + row * s * 0.1
            d.rectangle([wx, wy, wx + ww - 6, wy + s * 0.05],
                        fill=(255, 220, 120))
    d.polygon([(tx, y + s * 0.22), (tx + tw, y + s * 0.22),
               (tx + tw / 2, y + s * 0.12)], fill=(50, 65, 90))
    # impact burst
    bx, by = tx + tw * 0.75, y + s * 0.3
    for ang in range(0, 360, 30):
        import math
        r1, r2 = 10, 26
        a = math.radians(ang)
        d.line([bx + r1 * math.cos(a), by + r1 * math.sin(a),
                bx + r2 * math.cos(a), by + r2 * math.sin(a)],
               fill=(255, 140, 0), width=5)
    d.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=(255, 200, 40))
    # drone
    dx, dy = x + s * 0.12, y + s * 0.18
    d.ellipse([dx - 6, dy - 6, dx + 6, dy + 6], fill=(30, 30, 30))
    d.line([dx - 22, dy - 8, dx + 22, dy - 8], fill=(30, 30, 30), width=3)
    d.ellipse([dx - 28, dy - 12, dx - 16, dy - 4], fill=(90, 90, 90))
    d.ellipse([dx + 16, dy - 12, dx + 28, dy - 4], fill=(90, 90, 90))
    d.line([dx - 22, dy + 8, dx + 22, dy + 8], fill=(30, 30, 30), width=3)


def draw_blast(d, x, y, s):
    """Explosion over a city skyline: war in Ukraine."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(32, 32, 40))
    # skyline
    base = y + s * 0.9
    for bx, bw, bh in [(0.06, 0.16, 0.30), (0.26, 0.12, 0.42),
                       (0.42, 0.18, 0.24), (0.64, 0.14, 0.36),
                       (0.82, 0.12, 0.28)]:
        d.rectangle([x + s * bx, base - s * bh, x + s * (bx + bw), base],
                    fill=(70, 72, 90))
    # blast starburst
    cx, cy = x + s * 0.5, y + s * 0.42
    import math
    for ang in range(0, 360, 20):
        a = math.radians(ang)
        r = 46 if ang % 40 == 0 else 30
        d.line([cx, cy, cx + r * math.cos(a), cy + r * math.sin(a)],
               fill=(255, 170, 0), width=7)
    d.ellipse([cx - 24, cy - 24, cx + 24, cy + 24], fill=(255, 220, 60))
    d.ellipse([cx - 12, cy - 12, cx + 12, cy + 12], fill=(255, 120, 0))
    # smoke
    for sx, sy, r in [(0.3, 0.22, 10), (0.7, 0.18, 12), (0.62, 0.3, 8)]:
        d.ellipse([x + s * sx - r, y + s * sy - r,
                   x + s * sx + r, y + s * sy + r], fill=(150, 150, 160))


def draw_flags(d, x, y, s):
    """Two flags on poles: Australia and Solomon Islands (simplified)."""
    d.rounded_rectangle([x, y, x + s, y + s], radius=18, fill=(232, 244, 238))
    # poles
    d.line([x + s * 0.2, y + s * 0.14, x + s * 0.2, y + s * 0.88],
           fill=(90, 70, 40), width=5)
    d.line([x + s * 0.8, y + s * 0.14, x + s * 0.8, y + s * 0.88],
           fill=(90, 70, 40), width=5)
    # Australia flag (blue, Union Jack hint + stars)
    d.rectangle([x + s * 0.2, y + s * 0.16, x + s * 0.48, y + s * 0.44],
                fill=(0, 40, 120))
    d.line([x + s * 0.2, y + s * 0.16, x + s * 0.48, y + s * 0.44],
           fill=(255, 255, 255), width=4)
    d.line([x + s * 0.48, y + s * 0.16, x + s * 0.2, y + s * 0.44],
           fill=(255, 255, 255), width=4)
    for sx, sy in [(0.40, 0.24), (0.44, 0.36), (0.36, 0.38)]:
        d.ellipse([x + s * sx - 3, y + s * sy - 3,
                   x + s * sx + 3, y + s * sy + 3], fill=(255, 255, 255))
    # Solomon Islands flag (blue top, green bottom, yellow diagonal, stars)
    fx0, fy0, fx1, fy1 = x + s * 0.52, y + s * 0.16, x + s * 0.8, y + s * 0.44
    d.polygon([(fx0, fy0), (fx1, fy0), (fx0, fy1)], fill=(0, 90, 180))
    d.polygon([(fx1, fy1), (fx1, fy0), (fx0, fy1)], fill=(0, 140, 60))
    d.line([fx0, fy1, fx1, fy0], fill=(255, 220, 0), width=5)
    for sx, sy in [(0.58, 0.22), (0.64, 0.28), (0.70, 0.22),
                   (0.58, 0.32), (0.66, 0.36)]:
        d.ellipse([x + s * sx - 3, y + s * sy - 3,
                   x + s * sx + 3, y + s * sy + 3], fill=(255, 255, 255))
    # ribbon below the flags: a small teal shield with a check
    sx, sy = x + s * 0.5, y + s * 0.72
    d.polygon([(sx - 26, sy - 16), (sx + 26, sy - 16), (sx + 26, sy + 2),
               (sx, sy + 20), (sx - 26, sy + 2)], fill=(15, 118, 110))
    d.line([(sx - 12, sy - 2), (sx - 3, sy + 7), (sx + 13, sy - 9)],
           fill=(255, 255, 255), width=5)


STORIES = [
    ("SPACE", (23, 94, 158), draw_rocket,
     "CHINA LAUNCHES SHENZHOU-24",
     "First Pakistani astronaut rides to China's Tiangong space station."),
    ("MARKETS", (178, 34, 34), draw_chart,
     "TARIFF THREAT SINKS ASIAN SHARES",
     "US set to unveil new tariffs on China and the EU; Seoul and Taipei fall about 5%."),
    ("CYBER", (28, 42, 66), draw_lock,
     "CIA HIT BY CYBERATTACK",
     "Hack hits an unclassified open-source system; officials say no classified data was taken."),
    ("MIDDLE EAST", (180, 110, 20), draw_tower,
     "DRONE HITS RIYADH TOWER",
     "Houthi drone strikes the PIF Tower, injuring 11 \u2014 the second hit on the tower in a week."),
    ("UKRAINE WAR", (60, 60, 70), draw_blast,
     "RUSSIA STRIKES ODESA",
     "Two killed in Odesa; the US shelves a plan to use business deals to end the war."),
    ("PACIFIC", (15, 118, 110), draw_flags,
     "AUSTRALIA\u2013SOLOMONS PACT",
     "Canberra becomes the islands' security partner of choice, edging out China."),
]


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # ---- Masthead ----
    d.rectangle([0, 0, W, 148], fill=NAVY)
    d.rectangle([0, 148, W, 154], fill=GOLD)
    d.text((W // 2, 26), "THE WORLD IN ONE DAY",
           font=font(SANS_B, 26), fill=(201, 162, 39), anchor="ma")
    d.text((W // 2, 88), "WEDNESDAY  25  NOVEMBER  2026",
           font=font(SERIF_B, 44), fill=(255, 255, 255), anchor="mm")

    # ---- Story grid: 2 cols x 3 rows ----
    gx, gy = 24, 168
    pw, ph = 476, 240
    gap = 18
    for i, (tag, color, draw_icon, headline, caption) in enumerate(STORIES):
        col, row = i % 2, i // 2
        x = gx + col * (pw + gap)
        y = gy + row * (ph + gap)
        # card
        d.rounded_rectangle([x, y, x + pw, y + ph], radius=14,
                            fill=CARD, outline=(200, 196, 184), width=2)
        # tag bar
        d.rounded_rectangle([x, y, x + pw, y + 34], radius=14, fill=color)
        d.rectangle([x, y + 20, x + pw, y + 34], fill=color)
        d.text((x + 16, y + 17), tag, font=font(SANS_B, 19),
               fill=(255, 255, 255), anchor="lm")
        # icon
        draw_icon(d, x + 16, y + 50, 128)
        # headline + caption
        tx = x + 160
        tw = pw - 160 - 16
        lines = wrap(d, headline, font(SANS_B, 24), tw)
        hy = y + 52
        for ln in lines[:3]:
            d.text((tx, hy), ln, font=font(SANS_B, 24), fill=INK)
            hy += 29
        cy = hy + 6
        for ln in wrap(d, caption, font(SANS, 20), tw)[:3]:
            d.text((tx, cy), ln, font=font(SANS, 20), fill=(52, 56, 68))
            cy += 25

    # ---- Footer strip: also today ----
    fy = gy + 3 * ph + 2 * gap + 8
    d.rounded_rectangle([gx, fy, W - gx, fy + 56], radius=12, fill=NAVY2)
    d.text((W // 2, fy + 16),
           "ALSO TODAY:  North Korea expels Swiss envoy  \u2022  Dozens feared trapped in Indonesian mine",
           font=font(SANS_B, 17), fill=(255, 255, 255), anchor="mm")
    d.text((W // 2, fy + 40),
           "Huawei found guilty on 10 counts in US trial  \u2022  Miss Puerto Rico wins Miss Universe",
           font=font(SANS_B, 17), fill=(255, 255, 255), anchor="mm")
    d.text((W // 2, H - 14),
           "Sources: Reuters, CNN, AP, The Hindu, WSJ \u2014 25 November 2026  \u2022  One image, one day.",
           font=font(SANS, 15), fill=MUTED, anchor="mb")
    return img


if __name__ == "__main__":
    render().save("entry.png", optimize=True)
    print("wrote entry.png")
