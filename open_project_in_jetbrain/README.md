# 특정 디렉토리들의 내부에 jetbrain IDE project를 찾아주는 script

```shell script
# 직접 실행
python3 search_script.py --idea /usr/local/bin/idea --query alfred --project_paths ~/project1 ~/project2
```

```
# ScriptFilter를 /bin/bash 형태로 실행시키도록 설정

user_home=/Users/jaekwon
script_path=$user_home/workspace/project/alfred-workflow/open_project_in_jetbrain/search_script.py

idea=/usr/local/bin/idea
query=$1
project_paths="$user_home/project1 $user_home/project2"

python3 $script_path --idea $idea --query $query --project_paths $project_paths --icon_path $icon_path
```
