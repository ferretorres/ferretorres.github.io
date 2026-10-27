#!/usr/bin/env python3
"""Generate lightweight Open Graph cards for key Ferre Torres B.V. pages."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets"
WIDTH = 1200
HEIGHT = 630


@dataclass(frozen=True)
class Card:
    filename: str
    eyebrow: str
    title: str
    subtitle: str
    chips: tuple[str, ...]


CARDS = (
    Card(
        "og-ai-consultancy.jpg",
        "Ferre Torres B.V.",
        "AI consultancy for companies",
        "AI-first transformation, Company Brain, RAG, agents, and production AI systems for European businesses.",
        ("AI strategy", "MVP to production", "EU delivery"),
    ),
    Card(
        "og-company-brain.jpg",
        "Company Brain",
        "Central intelligence for company operations",
        "Connect documents, decisions, metrics, tools, and workflows into an AI-ready operational core.",
        ("Private knowledge", "RAG", "Assistants"),
    ),
    Card(
        "og-rag-systems.jpg",
        "RAG implementation",
        "Retrieval systems that can be trusted",
        "Source quality, permissions, evaluation, grounded answers, and production monitoring for enterprise AI.",
        ("Evaluation", "Permissions", "Grounding"),
    ),
    Card(
        "og-ai-mvp-poc.jpg",
        "MVP and PoC",
        "Prove AI value before scaling",
        "Build a narrow workflow, test it with real constraints, and decide whether it deserves production investment.",
        ("30-day signal", "Workflow metrics", "Scale path"),
    ),
    Card(
        "og-ai-security-gdpr.jpg",
        "Security and GDPR",
        "AI systems with governance built in",
        "EU-aware architecture for access control, audit trails, approval gates, and human review.",
        ("GDPR posture", "Audit trails", "Human review"),
    ),
    Card(
        "og-ai-architecture.jpg",
        "AI architecture",
        "Production patterns for company AI",
        "Connectors, permissions, retrieval, orchestration, evaluation, monitoring, and governance.",
        ("CTO-ready", "Reference patterns", "Scale path"),
    ),
    Card(
        "og-finance-intelligence.jpg",
        "Finance intelligence",
        "AI dashboards beyond static BI",
        "Margin movement, cash variance, pricing signals, anomalies, and finance workflow automation.",
        ("CFO-ready", "Dynamic metrics", "No BI lock-in"),
    ),
    Card(
        "og-agentic-workflows.jpg",
        "Agentic workflows",
        "Agents with approval gates",
        "AI agents that retrieve context, draft actions, call tools, escalate exceptions, and leave audit trails.",
        ("Workflow agents", "Human approval", "Tool use"),
    ),
    Card(
        "og-demo-gallery.jpg",
        "Guided demos",
        "AI implementation previews",
        "Company Brain, RAG evaluation, finance intelligence, AI PM, and agentic workflow examples.",
        ("Synthetic demos", "Buyer-ready", "Request walkthrough"),
    ),
    Card(
        "og-proof.jpg",
        "Proof and measurement",
        "AI projects should prove value",
        "Measure MVP speed, retrieval quality, adoption, governance fit, and production readiness.",
        ("MVP metrics", "Adoption", "Readiness"),
    ),
)


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = (
        "Avenir.ttc",
        "Helvetica.ttc",
        "Arial Bold.ttf" if bold else "Arial.ttf",
        "Verdana Bold.ttf" if bold else "Verdana.ttf",
    )
    for candidate in candidates:
        try:
            return ImageFont.truetype(candidate, size)
        except OSError:
            continue
    return ImageFont.load_default()


def cover_image() -> Image.Image:
    return Image.new("RGB", (WIDTH, HEIGHT), (249, 249, 243))


def rounded(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    radius: int,
    fill: tuple[int, int, int] | tuple[int, int, int, int],
) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    max_chars: int,
    line_gap: int,
    font_obj: ImageFont.FreeTypeFont | ImageFont.ImageFont,
    fill: tuple[int, int, int],
) -> int:
    x, y = xy
    for line in wrap(text, width=max_chars):
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y += (bbox[3] - bbox[1]) + line_gap
    return int(y)


def render(card: Card, base: Image.Image) -> None:
    image = base.copy().convert("RGBA")
    draw = ImageDraw.Draw(image)
    ink = (23, 47, 41)
    muted = (78, 101, 74)
    pale = (229, 237, 214)
    draw.ellipse((68, 72, 108, 102), outline=ink, width=4)
    draw.line((88, 60, 88, 114), fill=ink, width=4)
    draw.text((128, 72), "Ferre Torres B.V.", font=font(26), fill=ink)
    draw.text((72, 162), card.eyebrow.upper(), font=font(16), fill=muted)
    title_y = 207
    title_font = font(58)
    line = ""
    for word in card.title.split():
        candidate = f"{line} {word}".strip()
        if draw.textlength(candidate, font=title_font) > 740 and line:
            draw.text((68, title_y), line, font=title_font, fill=ink)
            title_y += 69
            line = word
        else:
            line = candidate
    draw.text((68, title_y), line, font=title_font, fill=ink)
    draw_wrapped(
        draw, card.subtitle, (72, max(title_y + 88, 386)), 64, 14, font(24), muted
    )
    chip_x = 72
    chip_font = font(18)
    for chip in card.chips:
        width = int(draw.textlength(chip, font=chip_font)) + 32
        rounded(draw, (chip_x, 529, chip_x + width, 570), 11, pale)
        draw.text((chip_x + 16, 540), chip, font=chip_font, fill=ink)
        chip_x += width + 10
    draw.ellipse((842, 164, 1164, 486), outline=(212, 223, 198), width=1)
    draw.ellipse((872, 195, 1134, 457), outline=(212, 223, 198), width=1)
    rounded(draw, (912, 246, 1094, 416), 42, pale)
    draw.ellipse((952, 289, 1054, 370), outline=ink, width=7)
    draw.line((1003, 265, 1003, 392), fill=ink, width=7)
    draw.text((945, 549), "ferretorres.eu", font=font(19), fill=muted)
    output = ASSET_DIR / card.filename
    image.convert("RGB").save(
        output, "JPEG", quality=85, optimize=True, progressive=True
    )
    print(output.relative_to(ROOT))


def main() -> None:
    base = cover_image()
    for card in CARDS:
        render(card, base)


if __name__ == "__main__":
    main()
