import xmltodict
import json
import os

RECORD_UPDATE = "record_update"
SYS_SCRIPT_INCLUDE = "sys_script_include"
SCRIPT = "script"
NAME = "name"
MODULE_EXPORTS_LINE = "\nmodule.exports = "


def write_script(filename):
    with open(filename) as in_file:
        xml_full_script = in_file.read()
        json_full_script =  xmltodict.parse(xml_full_script)
        script_include_name = json_full_script[RECORD_UPDATE][SYS_SCRIPT_INCLUDE][NAME] 
        script_contents = json_full_script[RECORD_UPDATE][SYS_SCRIPT_INCLUDE][SCRIPT]
        script_include_file_name = script_include_name + ".js"
        module_exports_line = MODULE_EXPORTS_LINE + script_include_name + ";"

        with open(script_include_file_name, 'w') as out_file:
	        out_file.write(script_contents)
	        out_file.write(module_exports_line)


if __name__ == "__main__":
    for root, dirs, files in os.walk("."):
        for file in files:
            if "sys_script_include_" in file:
                full_filename = os.path.join(root, file)
                print(full_filename)
                write_script(full_filename)