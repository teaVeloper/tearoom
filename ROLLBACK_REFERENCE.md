# 🚨 Qtile Configuration Rollback Reference

## **Quick Rollback Commands**

### **Option 1: Safe Interactive Rollback (Recommended)**
```bash
./rollback.sh
```

### **Option 2: Dry Run (See what would happen)**
```bash
./rollback.sh --dry-run
```

### **Option 3: Non-Interactive Rollback**
```bash
./rollback.sh -y
```

### **Option 4: Force Rollback (Use with caution)**
```bash
./rollback.sh --force
```

### **Option 5: Manual Git Rollback**
```bash
git checkout -- .
git clean -fd
```

## **Command Line Options**

| Option | Description | Safety Level |
|--------|-------------|--------------|
| `--dry-run` | Show what would be done without doing it | 🟢 Safe |
| `-y, --yes` | Skip confirmation prompts | 🟡 Medium |
| `-f, --force` | Force rollback even if backup incomplete | 🔴 Dangerous |
| `-h, --help` | Show help message | 🟢 Safe |

## **Safety Features**

✅ **Always shows what will be done** before doing it  
✅ **Requires confirmation** unless `-y/--yes` is used  
✅ **--dry-run option** for safe testing  
✅ **Validates backup integrity** before proceeding  
✅ **Color-coded output** for better readability  
✅ **Proper error handling** with exit codes  

## **When to Rollback**

- ❌ Qtile won't start
- ❌ Keybindings don't work as expected
- ❌ Layouts behave strangely
- ❌ You prefer the old setup

## **Rollback Process**

1. **Validation**: Checks backup integrity
2. **Preview**: Shows what will be restored/removed
3. **Confirmation**: Asks for user approval (unless `-y`)
4. **Execution**: Restores files and removes new structure
5. **Cleanup**: Removes modular files and tools

## **After Rollback**

1. **Reload Qtile**: `Super+Ctrl+r`
2. **Test functionality**: Try your usual keybindings
3. **Verify everything works**: Check terminal, rofi, window management

## **Current Backup Status**

✅ **Backup created**: `backup/` directory contains your original files  
✅ **Rollback script**: `rollback.sh` with safety features  
✅ **Git safety**: Original files still in git history  

## **Next Steps After Testing**

1. **If you like the new setup**: Keep it and move to separate repo
2. **If you want changes**: Tell me what to adjust
3. **If you want to rollback**: Run `./rollback.sh`

## **Best Practices**

- **Always test with `--dry-run` first**
- **Use `-y` only in scripts/automation**
- **Avoid `--force` unless absolutely necessary**
- **Keep your backup directory safe**

---

**Remember**: Your original configuration is safely backed up and can be restored at any time!
