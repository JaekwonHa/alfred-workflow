task_name=$1

exec_command1="/Users/user/workspace/personal/alfred-workflow/make_task_dir/make_new_task.py --root_path '/Users/user/Google 드라이브/1.workspace/1.Naver/task' --task_name '$task_name'"

exec_command2="/Users/user/workspace/personal/alfred-workflow/make_task_dir/make_new_task.py --root_path '/Users/user/Google 드라이브/1.workspace/2.study-2022' --task_name '$task_name'"

echo \{\"items\": \[\{\"uid\": 0, \"arg\": \"$exec_command1\", \"title\": \"1.workspace \> 1.Naver \> task\"\}, \{\"uid\": 0, \"arg\": \"$exec_command2\", \"title\": \"1.workspace \> 2.study-2022\"\}\]\}