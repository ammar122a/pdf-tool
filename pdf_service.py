from pathlib import Path
from pypdf import PdfWriter



def merge_pdfs(input_paths: list[Path], output_path: Path) -> Path:
    """Merge PDFs in the given order and return the output path."""

    if len(input_paths) < 2:
        raise ValueError("You need at least two PDFs to merge.")
    for path in input_paths:
        if not path.is_file():
            raise FileNotFoundError(f"Input file not found: {path}")
    if output_path.exists():
        raise FileExistsError(f"Output file already exists: {output_path}")

    writer = PdfWriter()

    try:
        for path in input_paths:
            writer.append(str(path))

        writer.write(str(output_path))
    finally:
        writer.close()

    return output_path