#!/bin/bash

# Check if the required command is available
check_command() {
    command=$1
    if ! command -v "$command" &> /dev/null; then
        echo "Error: $command is not installed."
        exit 1
    fi
}

# Check if the Python version meets the minimum requirement
check_python_version() {
    required_version="3.6.0"  # Minimum required Python version

    python_version=$(python3 --version 2>&1 | awk '{print $2}')

    if [[ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]]; then
        echo "Error: Python $required_version or later is required, but found $python_version."
        exit 1
    fi
}

# Check if the required Python packages are installed
check_python_packages() {
    required_packages=("ssl" "subprocess")

    for package in "${required_packages[@]}"; do
        if ! python3 -c "import $package" &> /dev/null; then
            echo "Error: $package Python package is not installed."
            exit 1
        fi
    done
}

# Main script

# Check if Python is installed
check_command "python3"

# Check the Python version
check_python_version

# Check if the required Python packages are installed
check_python_packages

# If all requirements are met, continue with executing the script
echo "System meets the requirements. Proceeding with the script execution."

# Add the command to run the Python script
python3 your_script_name.py
