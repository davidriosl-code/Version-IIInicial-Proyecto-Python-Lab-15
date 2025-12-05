En src/app.py:

import os
import configparser

def cargar_configuracion():
env = os.getenv("APP_ENV", "dev")

if env == "test":
config_file = "config_test.ini" elif env == "prod":
config_file = "config_prod.ini" else:
 
Despliegue.

config_file = "config_dev.ini" env = "dev"

config = configparser.ConfigParser() 
config.read(config_file, encoding="utf-8")
return env, config 
def main():
env, config = cargar_configuracion()

app_name = config["app"]["name"] 
message = config["app"]["message"] 
debug = config["app"].getboolean("debug")

version = config["app"]["version"] 
log_level = config["app"]["log_level"]

print("==============================")
print(f"Aplicación : {app_name}") 
print(f"Entorno	: {env}") print(f"Mensaje : {message}") 
print(f"Debug	 : {debug}")
print(f"Versión	: {version}") 
print(f"Log level : {log_level}")
print("==============================")

if  name == " main "
: main()
