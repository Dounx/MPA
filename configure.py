from pathlib import Path
import shutil

assets_dir = Path(__file__).parent / "assets"
external_dir = Path(__file__).parent / "external"


def configure_ocr_model():
    if not (external_dir / "MaaCommonAssets" / "OCR").exists():
        print(
            "Please clone this repository completely, don’t miss \"--recursive\", and don’t download the zip package!")
        print("请完整克隆本仓库，不要漏掉 \"--recursive\"，也不要下载 zip 包！")
        exit(1)

    ocr_dir = assets_dir / "resource" / "model" / "ocr"
    if not ocr_dir.exists():
        ocr_dir.mkdir(parents=True, exist_ok=True)

        zh_cn_source = external_dir / "MaaCommonAssets" / "OCR" / "ppocr_v4" / "zh_cn" / "det.onnx"
        zh_cn_target = ocr_dir / "det.onnx"
        if zh_cn_source.exists():
            shutil.copy(zh_cn_source, zh_cn_target)
            print(f"Copied det.onnx from ppocr_v4/zh_cn to {ocr_dir}")
        else:
            print(f"det.onnx not found in ppocr_v4/zh_cn.")

        ja_jp_source = external_dir / "MaaCommonAssets" / "OCR" / "ppocr_v3" / "ja_jp"
        if ja_jp_source.exists():
            shutil.copytree(ja_jp_source, ocr_dir, dirs_exist_ok=True)
            print(f"Copied all content from ppocr_v3/ja_jp to {ocr_dir}")
        else:
            print(f"ppocr_v3/ja_jp directory not found.")
    else:
        print("Found existing OCR directory, skipping model import.")


if __name__ == "__main__":
    configure_ocr_model()

    print("OCR model configured.")
