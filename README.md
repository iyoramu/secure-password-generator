# 🔐 Secure Password Generator  

A Python tool to generate cryptographically strong passwords using the `secrets` module.  

## Features  
- ✅ Customizable length (default: 16 chars)  
- ✅ Uppercase, digits, and symbols toggle  
- ❌ No weak `random` module — only `secrets`  

## Usage  
```python
from password_generator import generate_password
print(generate_password(length=12, use_symbols=False))
