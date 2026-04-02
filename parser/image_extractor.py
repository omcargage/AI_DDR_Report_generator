import fitz  # PyMuPDF
import os

def extract_images(pdf_path, output_folder="images"):
    os.makedirs(output_folder, exist_ok=True)

    doc = fitz.open(pdf_path)
    image_paths = []

    for i, page in enumerate(doc):
        images = page.get_images(full=True)

        for j, img in enumerate(images):
            xref = img[0]
            base = doc.extract_image(xref)
            img_bytes = base["image"]

            path = f"{output_folder}/page{i}_img{j}.png"

            with open(path, "wb") as f:
                f.write(img_bytes)

            image_paths.append(path)

    return image_paths