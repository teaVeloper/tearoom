#!/bin/bash
# Qtile Configuration Rollback Script
# This will restore your original working configuration

set -euo pipefail  # Exit on error, undefined vars, pipe failures

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
DRY_RUN=false
FORCE=false
YES=false

# Help function
show_help() {
    cat << EOF
Usage: $0 [OPTIONS]

Qtile Configuration Rollback Script
This will restore your original working configuration from backup.

OPTIONS:
    -y, --yes           Skip confirmation prompts
    -f, --force         Force rollback even if backup is incomplete
    --dry-run           Show what would be done without doing it
    -h, --help          Show this help message

EXAMPLES:
    $0                    # Interactive rollback with confirmation
    $0 --dry-run         # Show what would be done
    $0 -y                # Rollback without confirmation
    $0 --force --dry-run # Force rollback dry-run

SAFETY FEATURES:
    - Always shows what will be done before doing it
    - Requires confirmation unless -y/--yes is used
    - --dry-run option for safe testing
    - Validates backup integrity before proceeding
EOF
}

# Parse command line arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        -y|--yes)
            YES=true
            shift
            ;;
        -f|--force)
            FORCE=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        -h|--help)
            show_help
            exit 0
            ;;
        *)
            echo -e "${RED}Error: Unknown option $1${NC}"
            show_help
            exit 1
            ;;
    esac
done

# Function to print colored output
print_status() {
    local color=$1
    local message=$2
    echo -e "${color}${message}${NC}"
}

# Function to print commands (for dry-run)
print_command() {
    local cmd="$*"
    if [[ "$DRY_RUN" == true ]]; then
        echo -e "${BLUE}[DRY-RUN] Would run:${NC} $cmd"
    else
        echo -e "${BLUE}Running:${NC} $cmd"
    fi
}

# Function to execute commands safely
safe_execute() {
    local cmd="$*"
    print_command "$cmd"
    
    if [[ "$DRY_RUN" == false ]]; then
        eval "$cmd"
    fi
}

# Main rollback function
main() {
    print_status "$BLUE" "🔄 Qtile Configuration Rollback Script"
    print_status "$BLUE" "=========================================="
    echo

    # Check if backup exists
    if [[ ! -d "backup" ]]; then
        print_status "$RED" "❌ No backup directory found! Cannot rollback."
        print_status "$YELLOW" "💡 Make sure you're in the correct directory."
        exit 1
    fi

    # Validate backup integrity
    print_status "$BLUE" "🔍 Validating backup integrity..."
    local required_files=("config.py" "keys.py" "groups.py" "layouts.py" "screens.py" "hooks.py")
    local missing_files=()
    
    for file in "${required_files[@]}"; do
        if [[ ! -f "backup/$file" ]]; then
            missing_files+=("$file")
        fi
    done
    
    if [[ ${#missing_files[@]} -gt 0 ]]; then
        print_status "$RED" "❌ Backup is incomplete! Missing files:"
        for file in "${missing_files[@]}"; do
            echo "   - $file"
        done
        
        if [[ "$FORCE" == false ]]; then
            print_status "$YELLOW" "💡 Use --force to proceed anyway (not recommended)"
            exit 1
        else
            print_status "$YELLOW" "⚠️  Proceeding with incomplete backup (--force used)"
        fi
    else
        print_status "$GREEN" "✅ Backup validation passed"
    fi
    
    echo

    # Show what will be restored
    print_status "$BLUE" "📁 Files to be restored:"
    for file in "${required_files[@]}"; do
        if [[ -f "backup/$file" ]]; then
            local size=$(stat -c%s "backup/$file" 2>/dev/null || echo "unknown")
            echo "   ✅ $file ($size bytes)"
        else
            echo "   ❌ $file (missing)"
        fi
    done
    
    echo
    print_status "$BLUE" "🗑️  New modular files to be removed:"
    local modular_files=("modules/" "pyproject.toml" "qtile_check.py" "Makefile" "README.md")
    for file in "${modular_files[@]}"; do
        if [[ -e "$file" ]]; then
            echo "   🗑️  $file"
        else
            echo "   ⚪ $file (not present)"
        fi
    done
    
    echo

    # Confirmation prompt
    if [[ "$YES" == false ]]; then
        print_status "$YELLOW" "⚠️  This will completely replace your current Qtile configuration!"
        print_status "$YELLOW" "💡 Your current setup will be lost unless you have other backups."
        echo
        read -p "Are you sure you want to proceed? (yes/no): " -r
        if [[ ! $REPLY =~ ^[Yy][Ee][Ss]$ ]]; then
            print_status "$BLUE" "🛑 Rollback cancelled by user"
            exit 0
        fi
        echo
    fi

    # Execute rollback
    print_status "$GREEN" "🚀 Starting rollback process..."
    echo

    # Restore original files
    print_status "$BLUE" "📁 Restoring original files..."
    for file in "${required_files[@]}"; do
        if [[ -f "backup/$file" ]]; then
            safe_execute "cp 'backup/$file' '.'"
        fi
    done
    
    echo

    # Remove new modular files
    print_status "$BLUE" "🗑️  Removing new modular files..."
    for file in "${modular_files[@]}"; do
        if [[ -e "$file" ]]; then
            if [[ -d "$file" ]]; then
                safe_execute "rm -rf '$file'"
            else
                safe_execute "rm '$file'"
            fi
        fi
    done
    
    echo

    if [[ "$DRY_RUN" == true ]]; then
        print_status "$BLUE" "✅ Dry run completed - no changes were made"
        print_status "$YELLOW" "💡 Run without --dry-run to actually perform the rollback"
    else
        print_status "$GREEN" "✅ Rollback completed successfully!"
        print_status "$GREEN" "💡 Your original Qtile configuration has been restored."
        print_status "$GREEN" "🔄 You can now reload Qtile with: Super+Ctrl+r"
        echo
        print_status "$BLUE" "📝 To reapply the new configuration later, just run the setup again."
        print_status "$BLUE" "🛡️  Your backup files are still available in the 'backup/' directory."
    fi
}

# Run main function
main "$@"
