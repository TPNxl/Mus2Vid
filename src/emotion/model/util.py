import joblib
import pandas as pd


ROOT = "./../../.."
ANNOTATIONS_PATH = f"{ROOT}/data/processed/annotations/static_annotations_averaged_songs_1_2000.csv"
FEATURES_DIR = f"{ROOT}/data/interim/features"
TARGETS_DIR = f"{ROOT}/data/interim/targets"
MODEL_DIR = f"{ROOT}/models/emotion"
FEATURES_EXT = "features"
TARGETS_EXT = "targets"
MODEL_EXT = "model"



def get_features(filename):
    return joblib.load(f"{FEATURES_DIR}/{filename}.{FEATURES_EXT}")


def get_valence_targets():
    return pd.read_csv(ANNOTATIONS_PATH)["valence_mean"]


def get_arousal_targets():
    return pd.read_csv(ANNOTATIONS_PATH)["arousal_mean"]


if __name__ == "__main__":
    pass