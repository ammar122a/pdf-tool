from pathlib import Path
from pdf_service import mergePdfs

def main():
    location = Path(__file__).resolve().parent

    inputPaths = []
    for path in Path(location / "samples").glob("*.pdf"):
        inputPaths.append(path)

    outputPath = location / "merged.pdf"

    result = mergePdfs(inputPaths, outputPath)
    print(f"PDF gespeichert: {result}")

if __name__ == "__main__":
    main()