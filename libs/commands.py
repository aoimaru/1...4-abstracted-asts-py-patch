import subprocess
import json
import datetime
import shlex
import os

class ScriptRunningError(Exception):
    pass

class Command(object):
    # @staticmethod
    # def test(file_sha):
    #     subprocess.run(
    #         "cat ./binnacle-icse2020/datasets/4-abstracted-asts/github.jsonl.xz | xz -cd | grep '{}}' | jq".format(file_sha),
    #         shell=True
    #     )

    
    @staticmethod
    def create_4_abstract_ast_github_jsonl(file_sha):
        dt_now = datetime.datetime.now().strftime('%Y:%m:%d:%H:%M:%S:')
        # file_name = "{}:{}.json".format(dt_now, file_sha)
        file_name = "{}.json".format(file_sha)
        file_path = "./self-made-datasets/4-abstracted-asts:github:jsonl:xz/"
        script = "cat ./binnacle-icse2020/datasets/4-abstracted-asts/github.jsonl.xz | xz -cd | grep '{}' | jq".format(file_sha),
        with open(file_path+file_name, mode="w") as f:
            proc = subprocess.Popen(
                script,
                env=os.environ,
                stdout=f, 
                stderr=subprocess.PIPE,
                shell=True
            )
            stdout, stderr = proc.communicate()
            retcode = proc.returncode
            del proc
            if retcode == 1:
                raise ScriptRunningError('This script could not run $ %s\n%s' %(str(script), str(stderr)))
            






def main():
    with open("./self-made-metadata/created/2022:05:21:22:32:53:0b-deduplicated-dockerfile-sources-sha") as f:
        data = json.load(f)
    file_shas = data["file_shas"]
    for file_sha in file_shas[:4]:
        # Command.test(file_sha)
        print(file_sha)
        Command.create_4_abstract_ast_github_jsonl(file_sha)


if __name__ == "__main__":
    main()