#!/usr/bin/env python3
import sys
import os
from tempfile import TemporaryDirectory
import json

def resolv(data_array):
    #print(data_array)
    result = {
        "files" : []
    }
    for line in data_array:
        line = line.replace("\r", "")
        line = line.replace("\n", "")
        tag = line.split(":")[0]
        val = line.split(":")[1]
    
        if tag == "file":
            result["files"].append({"file" : val, "lines" : [], "functions" : []})
        elif tag == "function":
            func = val.split(",")[2]
            fdata = {
                    "blocks": 0,
                    "end_column": 0,
                    "start_line": int(val.split(",")[0]),
                    "name": val.split(",")[2],
                    "blocks_executed": 0,
                    "execution_count": int(val.split(",")[1]),
                    "demangled_name": val.split(",")[2],
                    "start_column": 0,
                    "end_line": 0
                }
            file_id = len(result["files"]) - 1
            result["files"][file_id]["functions"].append(fdata)
        elif tag == "lcount":
            ldata = {
                    "branches": [],
                    "count": int(val.split(",")[1]),
                    "line_number": int(val.split(",")[0]),
                    "unexecuted_block": False,
                    "function_name": func
                }
            file_id = len(result["files"]) - 1
            result["files"][file_id]["lines"].append(ldata)
    
    print(json.dumps(result))
            

    return 0

def main():
    root = os.path.expanduser("~/.cache")
    os.makedirs(root, exist_ok=True)

    file = open(os.path.join(root, "gcov7-json.log"), "w")
    file.write(os.getcwd() + "\n")
    file.write(" ".join(sys.argv) + "\n")
    file.close()
    if len(sys.argv) <= 1:
        print("Bad Parameter Num.")
        exit(1)

    option = sys.argv[1]
    if option == "--help":
        print("Fake Info: --json-format --stdout")
        exit(0)
    
    if len(sys.argv) <= 3:
        print("")
        exit(1)

    if option != "--stdout" or sys.argv[2] != "--json-format":
        print("")
        exit(1)

    file_list = sys.argv[3:]
    file_list = [ os.path.realpath(a) for a in file_list ]
    file_para = " ".join(file_list)
    with TemporaryDirectory() as dirname:
        f = os.popen("cd {} && gcov -b -c -x -i -l {}".format(dirname, file_para))
        result = f.readlines()
        #print(result)
        f = os.popen("cat {}/*.gcov".format(dirname, file_para))
        result = f.readlines()
        #print(result)
        resolv(result)
        #print('{"gcc_version": "9.3.1 20200406 [revision 6db837a5288ee3ca5ec504fbd5a765817e556ac2]", "files": [{"lines": [{"branches": [], "count": 1, "line_number": 5, "unexecuted_block": false, "function_name": "main"}, {"branches": [], "count": 1, "line_number": 6, "unexecuted_block": false, "function_name": "main"}, {"branches": [], "count": 1, "line_number": 7, "unexecuted_block": false, "function_name": "main"}], "functions": [{"blocks": 3, "end_column": 1, "start_line": 5, "name": "main", "blocks_executed": 3, "execution_count": 1, "demangled_name": "main", "start_column": 5, "end_line": 8}], "file": "/root/gcov7-json/main.c"}], "format_version": "1", "current_working_directory": "/root/gcov7-json/build_gcc9", "data_file": "/root/gcov7-json/build_gcc9/CMakeFiles/main.dir/main.c.gcda"}')


if __name__ == '__main__':
    main()