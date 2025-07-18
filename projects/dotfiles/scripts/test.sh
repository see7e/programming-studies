# if [ ! -e ~/.local/fonts ]; then
#     echo "The fonts-pack.zip is not installed"
# else
#     echo "The fonts-pack.zip is already installed"
# fi

# current_timestamp=$(date +%s)
# echo "Current Unix timestamp: $current_timestamp"

# non_existing_paths="" # Initialize a variable to store non-existing paths
# while IFS= read -r path; do
#     if [ ! -e "$path" ]; then
#         non_existing_paths+="$path\n"  # Append the non-existing path to the list
#     fi
# done < "/mnt/g/O meu disco/DRIVE/GAB/Estudos-Trabalhos/PROGRAMAÇÃO/programming-studies/othr/resources/dotlist.txt"
# # Echo the non-existing paths
# if [ -n "$non_existing_paths" ]; then
#     echo "The following paths do not exist:"
#     echo -e "$non_existing_paths"
# else
#     echo "All paths exist."
# fi