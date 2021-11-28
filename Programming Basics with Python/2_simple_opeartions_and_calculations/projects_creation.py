project_time = int(3)
architect_name = str(input())
projects_num = int(input())
estimated_time = project_time * projects_num
#
print(f'The architect {architect_name} ' +
      f'will need {estimated_time}' + f' hours to complete {projects_num} project/s.')
