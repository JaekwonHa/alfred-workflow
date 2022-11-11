user_home=/Users/user
script_path=$user_home/workspace/personal/alfred-workflow/open_website/search_script.py
website_list_path="/Users/user/Google 드라이브/1.workspace/1.Naver/website-list"
icon_path="$user_home/workspace/personal/alfred-workflow/open_website/icon"

query=$1

python3 $script_path --query "$query" --website_list_path "$website_list_path" --icon_path "$icon_path"
