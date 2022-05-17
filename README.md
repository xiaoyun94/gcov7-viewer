# GCOV7-JSON

## Background
- Compatiable for plugin [Gcov Viewer](https://github.com/JacquesLucke/gcov-viewer) in VSCode
- Transfers gcov-7 line format to gcov-9 json format

## Limitation
- Only valid for absolute path project temporarily now
- ✔️Tested build suite: CMake + Makefiles 
- ❌Failed test build suite: CMake + Ninja
- You must install Python 3

## Usage
- 1. Install Tool
```bash
#install py to executable path
chmod 755 ./gcov7-json.py
cp ./gcov7-json.py /usr/bin/
```
- 2. Open VSCode config, add this item in JSON config file
```json
{
    "gcovViewer.gcovBinary": "gcov7-json.py",
}
```
- 3. Start using plugin [Gcov Viewer] in VSCode
