from typing import Literal
import pandas as pd


def get_language_codes_dict() -> dict:
    """Returns a dictionary of language names to language codes for the Flores-200 \
dataset according to their repo's README at: \
https://github.com/facebookresearch/flores/blob/main/flores200/README.md
(last updated: 24/04/2023)

    Returns:
    --------
        `name_to_code {dict}`: A dictionary of language names to language codes.
    """
    present_languages = pd.read_csv(
        "flores200_lang_codes.tsv",
        sep="\t",
        index_col=None,
    )
    return {lang_name: lang_code for lang_name, lang_code in present_languages.values}


def get_flores_dataframe(
    folder_name: Literal["dev", "devtest"] = "dev",
) -> pd.DataFrame:
    """Returns a dataframe of the sentences from the Flores-200 dataset contained at \
`datasets/flores200/flores200_dataset/{folder_name}`. The columns of the dataframe are \
the language names and the rows are the sentences.

    Parameters:
    -----------
        `folder_name {"dev" or "devtest"}`: The name of the folder containing the \
sentences to be loaded.

    Returns:
    --------
        `flores_df {pd.DataFrame}`: A dataframe of translations of the same sentences \
from the Flores-200.
    """
    name_to_code_dict = get_language_codes_dict()
    flores_df = pd.DataFrame(columns=name_to_code_dict.keys())
    folder_path = f"flores200_dataset/{folder_name}"
    for lang_name, lang_code in name_to_code_dict.items():
        with open(
            f"{folder_path}/{lang_code}.{folder_name}",
            "r",
        ) as devfile:
            flores_df[lang_name] = [line.strip() for line in devfile.readlines()]
    return flores_df


if __name__ == "__main__":
    get_flores_dataframe("dev").to_csv(
        "flores200_dataset/flores200_dev.tsv",
        sep="\t",
        index=False,
    )
    get_flores_dataframe("devtest").to_csv(
        "flores200_dataset/flores200_devtest.tsv",
        sep="\t",
        index=False,
    )
