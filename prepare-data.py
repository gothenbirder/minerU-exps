import glob
import json
import os.path
import re


def get_filenames(path, target):
    return [
        filename
        for filename in glob.iglob(path + "**", recursive=True)
        if target in filename
    ]


def quote(s):
    return f'"{s}"'


def write_data(filenames, output):
    with open(output_file, "w") as file_out:
        file_out.write("docid,page,block,type,content" + "\n")
        for path in filenames:
            with open(path, "r") as file_in:
                js = json.loads(file_in.read())

            document_id = os.path.basename(path).split("_")[0]
            block_nr = 0
            for block in js:
                block_nr += 1
                entry_type = block.get("type", "")

                # remove html tags in text
                text = block.get("text", "")
                text = re.sub("<.*?>", "", text)

                # remove html tags in tables
                table_body = block.get("table_body", "")
                table_body = re.sub("<.*?>", "", table_body)
                table_body = re.sub(" +", " ", table_body)

                page_idx = block.get("page_idx", "")

                content = table_body if entry_type == "table" else text
                content = re.sub('"', "", content)
                content = content.strip()

                file_out.write(
                    ",".join(
                        [
                            quote(document_id),
                            str(page_idx),
                            str(block_nr),
                            quote(entry_type),
                            quote(content),
                        ]
                    )
                    + "\n"
                )


if __name__ == "__main__":
    target = "_content_list.json"
    output_file = "data.csv"

    write_data(get_filenames("documents/", target), output_file)
