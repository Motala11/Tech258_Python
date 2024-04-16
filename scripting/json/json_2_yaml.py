import sys, os, json, yaml

if len(sys.argv) > 1: # Do we have more than 1 argument?
    if os.path.exists(sys.argv[1]): # Is the file name passed through actually present?
        with open(sys.argv[1], "r") as file:
            json_data = json.load(file)
            yaml_data = yaml.dump(json_data)
            with open("output.yaml", "w") as output_file:
                output_file.write(yaml_data)
                print("YAML output saved to output.yaml")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: python check_json.py <file>")

# if len(sys.argv) > 1:  # do we have more than 1 argument?
#     if os.path.exists(sys.argv[1]):  # is the filename passed actually present?
#         file = open(sys.argv[1], "r")
#         json.load(file)
#         file.close()
#         print("JSON is valid!")
#         with open(sys.argv[1], 'r') as file:
#             configuration = json.load(file)
#     else:
#         print(sys.argv[1] + "not found")
# else:
#     print("Usage: python check_json.py <file>")
#
# with open('output.yaml', 'w') as yaml_file:
#     yaml.dump(configuration, yaml_file)
#
# with open('output.yaml', 'r') as yaml_file:
#     print(yaml_file.read())