#!/usr/bin/env python3
"""Generate lightweight Open Graph cards for key Ferre Torres B.V. pages."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "assets"
SOURCE = ASSET_DIR / "company-brain-hero.jpg"
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


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
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
    source = Image.open(SOURCE).convert("RGB")
    src_ratio = source.width / source.height
    target_ratio = WIDTH / HEIGHT
    if src_ratio > target_ratio:
        new_width = int(source.height * target_ratio)
        left = (source.width - new_width) // 2
        source = source.crop((left, 0, left + new_width, source.height))
    else:
        new_height = int(source.width / target_ratio)
        top = (source.height - new_height) // 2
        source = source.crop((0, top, source.width, top + new_height))
    source = source.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS)
    source = ImageEnhance.Contrast(source).enhance(1.08)
    source = ImageEnhance.Color(source).enhance(0.78)
    return source.filter(ImageFilter.GaussianBlur(radius=1.2))


def rounded(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], radius: int, fill: tuple[int, int, int, int]) -> None:
    draw.rounded_rectangle(box, radius=radius, fill=fill)


def draw_wrapped(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[int, int],
    max_chars: int,
    line_gap: int,
    font_obj: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
) -> int:
    x, y = xy
    for line in wrap(text, width=max_chars):
        draw.text((x, y), line, font=font_obj, fill=fill)
        bbox = draw.textbbox((x, y), line, font=font_obj)
        y += (bbox[3] - bbox[1]) + line_gap
    return y


def render(card: Card, base: Image.Image) -> None:
    image = base.copy().convert("RGBA")
    overlay = Image.new("RGBA", (WIDTH, HEIGHT), (7, 14, 13, 148))
    image.alpha_composite(overlay)
    draw = ImageDraw.Draw(image)

    rounded(draw, (72, 70, 1128, 560), 28, (13, 24, 22, 214))
    draw.line((72, 560, 1128, 560), fill=(73, 214, 124, 255), width=6)

    draw.text((108, 104), card.eyebrow.upper(), font=font(24, bold=True), fill=(110, 235, 154))
    draw.text((108, 144), card.title, font=font(62, bold=True), fill=(247, 250, 248))
    y = draw_wrapped(draw, card.subtitle, (108, 300), 63, 12, font(31), (214, 224, 219))

    chip_x = 108
    chip_y = max(y + 28, 430)
    chip_font = font(24, bold=True)
    for chip in card.chips:
        bbox = draw.textbbox((0, 0), chip, font=chip_font)
        width = bbox[2] - bbox[0] + 42
        rounded(draw, (chip_x, chip_y, chip_x + width, chip_y + 48), 24, (31, 75, 51, 235))
        draw.text((chip_x + 21, chip_y + 10), chip, font=chip_font, fill=(220, 250, 230))
        chip_x += width + 14

    draw.text((920, 512), "ferretorres.eu", font=font(25, bold=True), fill=(176, 198, 190))
    output = ASSET_DIR / card.filename
    image.convert("RGB").save(output, "JPEG", quality=82, optimize=True, progressive=True)
    print(output.relative_to(ROOT))


def main() -> None:
    base = cover_image()
    for card in CARDS:
        render(card, base)


if __name__ == "__main__":
    main()
