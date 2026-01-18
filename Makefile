# Qtile Configuration Makefile
# Provides targets for validation, formatting, and development

.PHONY: help validate fmt check clean install

# Default target
help:
	@echo "Qtile Configuration Management"
	@echo "============================="
	@echo ""
	@echo "Available targets:"
	@echo "  validate    - Run full validation (Python + Qtile)"
	@echo "  fmt         - Format code with black and ruff"
	@echo "  check       - Check code quality (ruff + black --check)"
	@echo "  clean       - Remove Python cache files"
	@echo "  install     - Install development dependencies"
	@echo "  help        - Show this help message"

# Validation targets
validate: check
	@echo "🔍 Running Qtile configuration validation..."
	@python3 qtile_check.py
	@echo "🔍 Checking keybindings for duplicates..."
	@python3 check_keybindings.py
	@echo "✅ Validation complete!"

# Code formatting
fmt:
	@echo "🎨 Formatting code with black..."
	@python3 -m black --line-length 88 .
	@echo "🔧 Fixing code with ruff..."
	@python3 -m ruff check --fix .
	@echo "✅ Formatting complete!"

# Code quality checks
check:
	@echo "🔍 Running code quality checks..."
	@echo "📏 Checking black formatting..."
	@python3 -m black --line-length 88 --check --diff .
	@echo "🔧 Running ruff linter..."
	@python3 -m ruff check . --exclude backup/
	@echo "✅ Code quality checks passed!"

# Clean up
clean:
	@echo "🧹 Cleaning Python cache files..."
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "✅ Cleanup complete!"

# Install development dependencies
install:
	@echo "📦 Installing development dependencies..."
	@pip3 install --user black ruff
	@echo "✅ Dependencies installed!"

# Development workflow
dev: fmt check validate
	@echo "🚀 Development workflow complete!"

# Quick validation (just Python imports)
quick-validate:
	@echo "⚡ Quick validation..."
	@python3 qtile_check.py

# Check keybindings only
check-keys:
	@echo "🔍 Checking keybindings for duplicates..."
	@python3 check_keybindings.py
