"""
更新 localify.json
"""
import json
import os


def main():
    orig_trans_file = input("旧翻译文件路径: ") or "localify.json"
    new_dump_file = input("新 dump 文件路径: ")

    with open(orig_trans_file, "r", encoding="utf8") as f:
        orig_data = json.load(f)

    with open(new_dump_file, "r", encoding="utf8") as f:
        new_data = json.load(f)

    for category in new_data:
        for key in new_data[category]:
            if (category in orig_data) and (key in orig_data[category]):
                new_data[category][key] = orig_data[category][key]

    new_save_name = os.path.join(os.path.split(orig_trans_file)[0], "new_localify.json")
    with open(new_save_name, "w", encoding="utf8") as f:
        json.dump(new_data, f, ensure_ascii=False, indent=4)
    print("执行完成，已保存新文件", new_save_name)


if __name__ == "__main__":
    main()
