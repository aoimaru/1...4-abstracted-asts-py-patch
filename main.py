import json
import pprint

"""
定数周り
"""
ZERO_A_ORIGINAL_DOCKERFILE_SOURCES = "binnacle-icse2020/datasets/0a-original-dockerfile-source"
ZERO_B_ORIGINAL_DOCKERFILE_SOURCES = "binnacle-icse2020/datasets/0b-original-dockerfile-source"
FIRST_PHASE_FIRST_DOCKERFILE_ASTS = "binnacle-icse2020/datasets/1-phase-1-dockerfile-asts"
SECONT_PHASE_SECOND_DOCKERFILE_ASTS = "binnacle-icse2020/datasets/2-phase-2-dockerfile-asts"
THIRD_PHASE_THIRD_DOCKERFILE_ASTS = "binnacle-icse2020/datasets/3-phase-3-dockerfile-asts"
FOURTH_ABSTRACTED_ASTS = "binnacle-icse2020/datasets/4-abstracted-asts"
FIFTH_DOCKERFILE_METADATA = "binnacle-icse2020/datasets/5-dockerfile-metadata"
SIXTH_GOLD_RULES = "binnacle-icse2020/datasets/6-gold-rules"


def main():
    with open("./self-made-metadata/created/2022:05:21:22:32:53:0b-deduplicated-dockerfile-sources-sha") as f:
        data = json.load(f)
    file_shas = data["file_shas"]
    for file_sha in file_shas[:10]:
        print(file_sha)


if __name__ == "__main__":
    main()