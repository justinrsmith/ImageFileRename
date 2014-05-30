import os

file = open('imaging/EXPORTNEW.txt', 'r')

file_names = []
for line in file:
    fields = line.split('|')
    file_dict = {'new_file_name': fields[0] + '_' + fields[1].replace(
                                  ', ', '$') + '_' + fields[2].replace(
                                  '/', '$') + '.TIF',
                 'old_file_name': fields[3].strip()}
    file_names.append(file_dict)

directory = '/Users/justinsmith/sd54/imaging/Imaging/'
for root, dirs, files in os.walk('Imaging', topdown=True):
    for f in files:
        for fn in file_names:
            if fn['old_file_name'] == f:
                old_file = os.path.join(directory, f)
                new_file = os.path.join(directory, fn['new_file_name'])
                os.rename(old_file, new_file)
