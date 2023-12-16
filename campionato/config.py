
from os import path


"[test]"
test_mode = True
test_main = 2

source = 'resources/players.txt'

output_dir = 'resources/output/'
ftest = {
    'out' : 'players_out.txt',
    'age' : 'players_age.txt',
    'att' : 'players_top_attendance.txt'
}
# append file paths to data_dir
for fname in ftest:
    ftest[fname] = path.join(output_dir, ftest[fname])
