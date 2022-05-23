import os
import datetime
import pprint
import json

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
SELF_MADE_PATH = "./self-made-metadata/"
ORIGINAL = "original/"
CREATED = "created/"
TO_JSON_FILE_SHA_FILE_NAME = "0b-deduplicated-dockerfile-sources-sha"
ZERO_B_DEDUPLICATED_DOCKERFILE_SOURCES = "0b-deduplicated-dockerfile-sources.github.tar.xz.log"


class DD(object):
    @staticmethod
    def get_file_sha(self_made_path):
        file_shas = list()

        BASE_INDEX = 1
        def handle(contents):
            file_path = contents.split()[BASE_INDEX]
            base_name = os.path.basename(file_path)
            return base_name.replace(".Dockerfile", "")

        with open(self_made_path, mode="r") as f:
            for line in f:
                file_sha = handle(line)
                if not file_sha:
                    continue
                file_shas.append(file_sha)
        return file_shas

    @staticmethod
    def to_json_file(to_file_path, to_json_data):
        dt_now = datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S:')
        to_file_path = dt_now+to_file_path
        with open(SELF_MADE_PATH+CREATED+to_file_path, mode="w") as f:
            json.dump(to_json_data, f, ensure_ascii=False, indent=4)

def test():
    # SELF_MADE_PATH = "./self-made-metadata/"
    # ORIGINAL = "original/"
    # ZERO_B_DEDUPLICATED_DOCKERFILE_SOURCES = "0b-deduplicated-dockerfile-sources.github.tar.xz.log"
    file_shas = DD.get_file_sha(SELF_MADE_PATH+ORIGINAL+ZERO_B_DEDUPLICATED_DOCKERFILE_SOURCES)
    to_json_data = {
        "file_shas": file_shas
    }
    DD.to_json_file(TO_JSON_FILE_SHA_FILE_NAME, to_json_data)

    # TO_JSON_FILE_SHA_FILE_NAME = "0b-deduplicated-dockerfile-sources-sha.json"
    # pprint.pprint(to_json_data)

def main():
    # TO_JSON_FILE_SHA_FILE_NAME = "0b-deduplicated-dockerfile-sources-sha"
    # DD.to_json_file(TO_JSON_FILE_SHA_FILE_NAME, {"hello": "world"})
    test()


if __name__ == "__main__":
    main()