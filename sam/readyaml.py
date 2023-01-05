import yaml
with open("data1.yml", "r") as f:
    data = yaml.safe_load(f)
print(data)
