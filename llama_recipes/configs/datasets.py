# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the Llama 2 Community License Agreement.

from dataclasses import dataclass


@dataclass
class samsum_dataset:
    dataset: str = "samsum_dataset"
    train_split: str = "train"
    test_split: str = "validation"


@dataclass
class grammar_dataset:
    dataset: str = "grammar_dataset"
    train_split: str = "src/llama_recipes/datasets/grammar_dataset/gtrain_10k.csv"
    test_split: str = (
        "src/llama_recipes/datasets/grammar_dataset/grammar_validation.csv"
    )


@dataclass
class alpaca_dataset:
    dataset: str = "alpaca_dataset"
    train_split: str = "train"
    test_split: str = "val"
    data_path: str = "src/llama_recipes/datasets/alpaca_data.json"
    max_length: int = 2048


@dataclass
class zalo_math_dataset:
    dataset: str = "zalo_math_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    data_path: str = "datasets/math_train.json"
    max_length: int = 2048


@dataclass
class zalo_math_filter_explanation_dataset:
    dataset: str = "zalo_math_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    data_path: str = "datasets/filter_explanation_math_train.json"
    max_length: int = 2048


@dataclass
class zalo_math_fill_missing_explain_35:
    dataset: str = "zalo_math_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    data_path: str = "datasets/with-missing-explain-3.5.json"
    max_length: int = 2048


@dataclass
class zalo_math_fill_missing_explain_4:
    dataset: str = "zalo_math_dataset"
    train_split: str = "train"
    test_split: str = "validation"
    data_path: str = "datasets/qualified_data.json"
    max_length: int = 2048
