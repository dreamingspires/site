
env_out: dict[str, str] = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            pass
        else:
            key, value = line.split("=", 1)
            value = value.strip().strip('"').strip("'")
            env_out[key.strip()] = value

with open('config.template.toml', 'r') as f:
    config = f.read()

for k, v in env_out.items():
    config = config.replace("${" + k + "}", env_out[k])

with open('config.toml', 'w') as f:
    f.write(config)
