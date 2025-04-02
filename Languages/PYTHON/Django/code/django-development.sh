#!/bin/sh


get_input() {
  local input
  read -r input
  echo "$input"
}

echo "Type GH name:"
gh_name=$(get_input)

# Get Django
cd
git clone https://github.com/$gh_name/django.git
cd django

# Create env
python3 -m venv ~/.virtualenvs/djangodev
source ~/.virtualenvs/djangodev/bin/activate

# Install Django locally
python -m pip install -e ~/django/

