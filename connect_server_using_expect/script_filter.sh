user_home=/Users/user
script_path=$user_home/workspace/personal/alfred-workflow/connect_server_using_expect/search_script.py
server_list_path=""

query=$1
icon_path="ssh_icon.png"

python3 $script_path --query $query --server_list_path "$server_list_path" --icon_path $icon_path
