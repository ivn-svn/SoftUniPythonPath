# Judge statistics on the last Programing Fundamentals exam were not working correctly, so you have the task of
# taking all the submissions and analyzing them properly.
#
# You should collect all the submissions and print the final
# results and statistics about each language in which the participants submitted their solutions.
#
# You will be receiving lines in the following format: "{username}-{language}-{points}"
# until you receive "exam finished". You should store each username and their submissions and points.
#
# If a student has two or more submissions for the same
# language, save only his maximum points. You can receive a command to ban a user for cheating in the following
# format: "{username}-banned". In that case, you should remove the user from the contest but preserve his submissions
# in the total count of submissions for each language. After receiving "exam finished", print each of the
# participants in the following format: "Results: {username1} | {points} {username2} | {points} … {usernameN} | {
# points}" After that, print each language used in the exam in the following format: "Submissions: {language1} - {
# submissions_count} {language2} - {submissions_count} … {language3} - {submissions_count}"
# class ExamResults:
#     def __init__(self, usr, lang, pts):
#         self.usr = usr
#         self.lang = lang
#         self.pts = pts


username_langs_dict = {}
# username_langs_dict example contents:
# {
# 'username1': {'C#': [50, 40, 60], 'Java': [90, 20, 60]},
# 'username2': {'C++': [0, 10, 20], 'Python': [40, 25, 30]}
# }
lang_pts_dict = {}  # Lang pts dict is going to be emptied on every cycle
submission_count = {}
cmd = input()
while cmd != 'exam finished':
    cmd_split = cmd.split('-')
    if 'banned' in cmd_split:
        username = cmd_split[0]
        username_langs_dict[''] = username_langs_dict.pop(username)
    else:
        username = cmd_split[0]
        language = cmd_split[1]
        points = str(cmd_split[2])
        lang_pts_dict = {}
        if language in submission_count.keys():
            submission_count[language] += 1
        else:
            submission_count[language] = 1
        if username in username_langs_dict.keys():
            lang_pts_dict = username_langs_dict[username]

            if language in lang_pts_dict.keys():
                lang_pts_dict[language].append(points)
            else:
                lang_pts_dict[language] = []
                lang_pts_dict[language].append(points)
        else:
            lang_pts_dict[language] = []
            lang_pts_dict[language].append(points)
            username_langs_dict[username] = lang_pts_dict

    cmd = input()
print('Results:')
occurences = []
for (usr, ptslst) in username_langs_dict.items():
    for (lang, pts) in ptslst.items():
        occurences.append(lang)
        # print(pts)
        lang_pts_dict = ptslst
        curr_max = str(pts[0])
        if len(pts) > 1:
            curr_max = (max(pts))
            print(f'{usr} | {curr_max}')
        else:
            print(f'{usr} | {curr_max}')
print("Submissions:")
# print(submission_count)
for (key, value) in submission_count.items():
    print(f'{key} - {value}')
