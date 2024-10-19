# MPA

非常好 PJSK 小助手，爱来自 MAA Framework。

## Development

### Requirements

- [Poetry](https://python-poetry.org/docs/#installation)

### Setup

1. Clone the repository with submodules

    ```bash
    git clone https://github.com/Dounx/MPA.git --recursive
    ```

2. Install dependencies

    ```bash
    poetry install
    ```

3. Configure OCR models

    ```bash
    python configure.py
    ```

4. Run the application

    ```bash
    python main.py
    ```

## Tools

Screenshots and OCR are provided by the following tools:

- [MFATools](https://github.com/SweetSmellFox/MFATools.git)

Note: copy zh_cn det.onnx and ja_jp rec.onnx & keys.txt to the tool, 
please refer to configure.py for more details.
