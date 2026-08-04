path = "config/settings.py"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
if "'clinico'" not in content:
    content = content.replace("INSTALLED_APPS = [", "INSTALLED_APPS = [\n    'clinico',", 1)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("agregado")
else:
    print("ya estaba")
