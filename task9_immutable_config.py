from collections import namedtuple

AppConfig = namedtuple("AppConfig", ["app_name", "version", "supported_environments", "database_host", "database_port"])

config = AppConfig(
    app_name="InventoryApp",
    version="1.0.3",
    supported_environments=("development", "staging", "production"),
    database_host="db.internal",
    database_port=5432,
)

print("Current configuration:")
print(f"  App: {config.app_name} v{config.version}")
print(f"  Environments: {config.supported_environments}")
print(f"  Database: {config.database_host}:{config.database_port}")

print("\nAttempting to modify config.version...")
try:
    config.version = "2.0.0"
except AttributeError as error:
    print(f"  Blocked! Error raised: {error}")
