from pathlib import Path
from pypdf import PdfWriter



def mergePdfs(inputPaths: list[Path], outputPath: Path) -> Path:

    if len(inputPaths) < 2:
        raise ValueError("You need at least two PDFs to merge.")
    for path in inputPaths:
        if not path.is_file():
            raise FileNotFoundError(f"Input file not found: {path}")
    if outputPath.exists():
        raise FileExistsError(f"Output file already exists: {outputPath}")

    writer = PdfWriter()

    try:
        for path in inputPaths:
            writer.append(str(path))

        writer.write(str(outputPath))
    finally:
        writer.close()

    return outputPath