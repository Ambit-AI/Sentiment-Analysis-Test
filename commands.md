# Create environment folder called env
```powershell
python -m venv env
```

# Activate environment
```powershell
env/Scripts/activate
```

# Deactivate environment
```powershell
deactivate
```

# Install dependencies
```powershell
pip3 install -r requirements.txt
```

# Export dependencies
```powershell
pip3 freeze > ./requirements.txt
```