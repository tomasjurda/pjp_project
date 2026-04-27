# Project for subject Programming Languages and Compilers
Definition of this project: http://behalek.cs.vsb.cz/wiki/index.php/PLC_Project

## HOW TO RUN
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

On Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## How to use updated grammar
```bash
java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor ProjectLexer.g4 ProjectParser.g4
``` 