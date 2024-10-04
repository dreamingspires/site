import os

# Load the .env file
env_out: dict[str, str] = {}
with open(".env") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):
            pass
        else:
            key, value = line.split("=", 1)

            # Remove surrounding quotes from the value, if any
            value = value.strip().strip('"').strip("'")

            # Set the environment variable
            env_out[key.strip()] = value

# Read the config template
with open('config.template.toml', 'r') as f:
    config = f.read()

for k, v in env_out.items():
    # Replace placeholders with actual environment variables
    config = config.replace("${" + k + "}", env_out[k])

# Write the result to the actual config.toml
with open('config.toml', 'w') as f:
    f.write(config)
