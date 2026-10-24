from pathlib import Path
from pdf_service import merge_pdfs

def main():
    project_dir = Path(__file__).resolve().parent

    input_paths = [
        project_dir / "samples" / "dokument1.pdf",
        project_dir / "samples" / "dokument2.pdf",
    ]
    output_path = project_dir / "merged.pdf"

    result = merge_pdfs(input_paths, output_path)
    print(f"PDF gespeichert: {result}")

if __name__ == "__main__":
    main()