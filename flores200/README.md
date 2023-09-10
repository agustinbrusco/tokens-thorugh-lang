# FLORES-200 Dataset
The purpouse of this dataset is to be used as an Evaluation Benchmark for Low-Resource and Multilingual Machine Translation. Information on this dataset can be found at the [flores200 repository](https://github.com/facebookresearch/flores/tree/main/flores200). To download the dataset and exctract it here, run the following command from this directory:
```bash
wget --trust-server-names https://tinyurl.com/flores200dataset && tar -xzvf flores200_dataset.tar.gz && rm flores200_dataset.tar.gz
```
Then, to generate two .tsv files containing the flores200 dataset, run the following command from this directory:
```bash
python generate_flores200_files.py
```
This will create the files `flores200_dataset/dev/flores200_dev.tsv` & `flores200_dataset/devtest/flores200_devtest.tsv` containing the flores200 dataset sentences as rows and languages as columns.

---
Note: There is a `nan` value at the line 245 of the Central Kurdish .dev file (`datasets/flores/flores200_dataset/dev/ckb_Arab.dev`) which is then present at the line 246 of the generated `flores200_dataset/dev/flores200_dev.tsv`.