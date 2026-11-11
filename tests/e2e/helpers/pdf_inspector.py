"""
tests/e2e/helpers/pdf_inspector.py
Inspection utilities for Brochure PDF verification using PyMuPDF (fitz) and PIL.
"""
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, Union
import fitz  # PyMuPDF
from PIL import Image

UnionPath = Union[Path, str]

def open_brochure_pdf(pdf_path: UnionPath) -> fitz.Document:
    """Opens a PDF document from the given path."""
    p = Path(pdf_path)
    if not p.exists():
        raise FileNotFoundError(f"PDF file not found at: {p}")
    return fitz.open(str(p))

def get_white_background_boxes(page: fitz.Page) -> List[Dict[str, Any]]:
    """
    Returns all vector drawing shapes that have a solid or near-white fill
    (all rgb channels > 0.95), excluding the full-page outer canvas rectangle.
    """
    white_boxes = []
    page_rect = page.rect
    drawings = page.get_drawings()
    for d in drawings:
        fill = d.get("fill")
        if fill and isinstance(fill, (list, tuple)) and len(fill) >= 3:
            # Check for near-white fill
            if all(c > 0.95 for c in fill[:3]):
                rect = d.get("rect")
                if rect is not None:
                    # Ignore the full-page canvas background
                    # Tolerating minor floating point margin
                    is_canvas = (
                        abs(rect.x0 - page_rect.x0) < 2.0
                        and abs(rect.y0 - page_rect.y0) < 2.0
                        and abs(rect.x1 - page_rect.x1) < 2.0
                        and abs(rect.y1 - page_rect.y1) < 2.0
                    )
                    if not is_canvas:
                        white_boxes.append({
                            "rect": rect,
                            "fill": fill,
                            "items": d.get("items", [])
                        })
    return white_boxes

def extract_vector_text(page: fitz.Page) -> str:
    """Extracts searchable vector text from the page."""
    return page.get_text()

def get_embedded_fonts(page: fitz.Page) -> List[Tuple[Any, ...]]:
    """Returns list of embedded font metadata tuples."""
    return page.get_fonts()

def find_embedded_images(page: fitz.Page) -> List[Dict[str, Any]]:
    """Returns all embedded images with their bounding rect and dimensions."""
    images = []
    image_list = page.get_images(full=True)
    for img_info in image_list:
        xref = img_info[0]
        # find image rects on the page
        rects = page.get_image_rects(xref)
        pix = page.parent.extract_image(xref)
        for r in rects:
            images.append({
                "xref": xref,
                "bbox": r,
                "width": pix.get("width", 0),
                "height": pix.get("height", 0),
                "format": pix.get("ext", ""),
                "size": len(pix.get("image", b""))
            })
    return images

def sample_pixel_color(page: fitz.Page, x: float, y: float, dpi: int = 150) -> Tuple[int, int, int]:
    """Renders page at specified DPI and samples RGB pixel at normalized page coordinates."""
    pix = page.get_pixmap(dpi=dpi)
    scale = dpi / 72.0
    px = int(x * scale)
    py = int(y * scale)
    px = max(0, min(px, pix.width - 1))
    py = max(0, min(py, pix.height - 1))
    color = pix.pixel(px, py)
    return color[:3]

def get_page_redactions(page: fitz.Page) -> List[Any]:
    """Returns any unapplied or active redaction annotations."""
    annots = list(page.annots()) if page.annots() else []
    return [a for a in annots if a.type[0] == fitz.PDF_ANNOT_REDACT]
