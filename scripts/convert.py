import xmltodict
import json
infile = "x_481373_applicati/update/sys_script_include_e4a04cf3dbc01010ea4053184b96193d.xml" 
outfile = "myMath.js"
module_exports_line = "\nmodule.exports = myMath;"

with open(infile) as in_file:
    xml = in_file.read()
    with open(outfile, 'w') as out_file:
        myString = xmltodict.parse(xml)["record_update"]["sys_script_include"]["script"]
	out_file.write(myString)
	out_file.write(module_exports_line)
