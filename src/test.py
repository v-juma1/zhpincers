# -*- coding: utf-8 -*-
import pandas as pd
from pincers import BasePincer


def run():

    example = pd.read_csv("tests/addr_example.csv")

    p = BasePincer()
    p.load_jieba_dict()
    example["jieba_split"] = example["orginal"].map(lambda x: p.jieba_split(x))
    example["re_split"] = example["orginal"].map(lambda x: p.re_split(x))

    example.to_csv("tests/addr_example_split.csv")


if __name__ == "__main__":
    run()
