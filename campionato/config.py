import os


"[test]"
test_mode = True
test_main = 2

source = 'resources/players.txt'

# git doesn't like empty folders, so if it's not populated I have to make it here
output_dir = 'resources/output/'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

ftest = {
    'out' : 'players_out.txt',
    'age' : 'players_age.txt',
    'att' : 'players_top_attendance.txt'
}
# append file paths to data_dir
for fname in ftest:
    ftest[fname] = os.path.join(output_dir, ftest[fname])
