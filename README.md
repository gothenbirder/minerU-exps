This Python project is uv managed, therefore use 'uv sync' to fetch necessary
packages. Also, be aware of the use of LFS to make sure to get the actual .pdf
files if needed.


ocr_documents.sh:
  takes the .pdf documents in the `documents/` folder and writes MinerU OCR
  results to different directories

prepare-data.py:
  assembles OCR results for all documents into a csv file, doing some cleaning
  on the way; further cleaning and sanitation is done in the Jupyter notebook

data.csv:
  the resulting csv file

find_contract.ipynb:
  Jupyter notebook: tf-idf including further cleaning (lower-casing, remove
  'accents', ...), followed by construction of a Naive Bayes classifier and
  cross-validation / visualization
