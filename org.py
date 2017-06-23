import os, sys

try:
    os.chdir(sys.argv[1])
except FileNotFoundError as e:
    print(e)
    sys.exit()

try:
    os.mkdir('Music')
    os.mkdir('Videos')
    os.mkdir('Images')
    os.mkdir('Docs')
    os.mkdir('Zips')
    os.mkdir('Other')
except FileExistsError as e:
    print(e)
    sys.exit()

list_of_files = os.listdir()
curr_working_dir = os.getcwd()

music_ext_list = ['mp3']
videos_ext_list = ['mkv', 'mp4', 'wmv']
images_ext_list = ['jpg', 'JPG', 'png', 'gif', 'PNG']
docs_ext_list = ['pdf', 'txt', 'xlsx', 'csv']
zips_ext_list = ['zip', 'tgz', 'gz']

for file in list_of_files:

    if os.path.isdir(str(file)):
        continue

    extension = file.split('.')[-1]

    if extension in music_ext_list:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Music/'+str(file))
        print("Moving file '"+ str(file) + "' to Music directory")

    elif extension in images_ext_list:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Images/'+str(file))
        print("Moving file '"+ str(file) + "' to Images directory")

    elif extension in docs_ext_list:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Docs/'+str(file))
        print("Moving file '"+ str(file) + "' to Docs directory")

    elif extension in zips_ext_list:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Zips/'+str(file))
        print("Moving file '"+ str(file) + "' to Zips directory")

    elif extension in videos_ext_list:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Videos/'+str(file))
        print("Moving file '"+ str(file) + "' to Videos directory")

    else:
        os.rename(os.getcwd()+'/'+ str(file), os.getcwd()+'/Other/'+str(file))
        print("Moving file '"+ str(file) + "' to Other directory")

print('Successfully cleaned working directory')
