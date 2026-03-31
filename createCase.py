
import os
import shutil
import json

#新增用例，填这里的测试用例路径就可以了,格式是：模块名/用例名
testCasePath = "Example/Example"

"""
复制 testcases/Example/Example 文件夹 到 testcases/{test_module_path}/
重命名文件夹，命名为{testCaseName}
文件夹内有 Example.json 和 Example.py 文件，将这两个文件重命名为 {testCaseName}.json 和 {testCaseName}.py
将{testCaseName}.py 文件内容进行字符串替换，将“Example”替换成 {testCaseName}
{testCaseName}.json 文件数据是 json 格式，将driver.py_file[0]的值替换成 {test_module_path}/{test_module_path}/{testCaseName}.py
"""

parts = testCasePath.split("/")
test_module_path = parts[-2]
testCaseName = parts[-1]

src_dir = "testcases/Example/Example"
dst_dir = f"testcases/{test_module_path}/{testCaseName}"

# 判断目标文件夹是否存在
if os.path.exists(dst_dir):
    print("用例文件夹已存在")
else:
    # 1. 复制文件夹
    shutil.copytree(src_dir, dst_dir)

    # 2. 重命名文件
    old_json = os.path.join(dst_dir, "Example.json")
    old_py = os.path.join(dst_dir, "Example.py")
    new_json = os.path.join(dst_dir, f"{testCaseName}.json")
    new_py = os.path.join(dst_dir, f"{testCaseName}.py")
    os.rename(old_json, new_json)
    os.rename(old_py, new_py)

    # 3. 替换 py 文件内容
    with open(new_py, "r", encoding="utf-8") as f:
        py_content = f.read()
    py_content = py_content.replace("Example", testCaseName)
    with open(new_py, "w", encoding="utf-8") as f:
        f.write(py_content)

    # 4. 修改 json 文件内容
    with open(new_json, "r", encoding="utf-8") as f:
        json_data = json.load(f)
    json_data["driver"]["py_file"][0] = f"{test_module_path}/{testCaseName}/{testCaseName}.py"
    with open(new_json, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

    print("处理完成！")