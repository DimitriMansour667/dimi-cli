import os


def do_in(self, line):
    # like cd
    try:
        if os.path.exists(line):
            os.chdir(line)
            self.dirprefix = os.getcwd()
            self.prompt = f"{self.dirprefix} (DIMI_CLI)> "
        else:
            print(f"Directory does not exist: {line}")
    except Exception as e:
        print(e)
        

def do_out(self, line):
    # go up one directory
    try:
        os.chdir("..")
        self.dirprefix = os.getcwd()
        self.prompt = f"{self.dirprefix} (DIMI_CLI)> "
    except Exception as e:
        print(e)

def do_create(self, line):
    try:
        if not os.path.exists(line):
            if '.' in line:
                open(line, 'w').close()
                print("created file: %s" % line)
            else:
                os.mkdir(line)
                print("created directory: %s" % line)
        else:
            print("file/directory already exists")
    except Exception as e:
        print(e)


def do_delete(self, line):
    import shutil
    try:
        if os.path.exists(line):
            if os.path.isfile(line):
                os.remove(line)
                print("removed file: %s" % line)
            elif os.path.isdir(line):
                shutil.rmtree(line)
                print("removed directory: %s" % line)
    except Exception as e:
        print(e)

def do_clean(self, line):
    import shutil
    inp = input("Are you sure you want to clean the current directory? (y/n)")
    if inp.lower() == 'y' or inp.lower() == 'yes':
        try:
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
            print("cleaned current directory")
        except Exception as e:
            print(e)

def do_list(self, line):
    #list files in current directory but not subdirectories
    for file in os.listdir(os.getcwd()):
        if os.path.isfile(file):
            print(f"📄 - {file}")
        else:
            print(f"📁 - {file}")

def do_size(self, line):
    def convert_size(size_bytes):
        from math import log2, floor
        if size_bytes == 0:
            return "0 B"
            
        size_names = ('B', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB')
        power = floor(log2(size_bytes) / 10)
        power = min(power, len(size_names) - 1)
        size = size_bytes / (1024 ** power)
        
        return f"{size:.2f} {size_names[power]}"

    try:
        if line == "":
            total_size = 0
            for root, dirs, files in os.walk(os.getcwd()):
                for file in files:
                    total_size += os.path.getsize(os.path.join(root, file))
            print(f"Total size of current directory: {convert_size(total_size)}")
        else:
            if os.path.exists(line):
                if os.path.isfile(line):
                    size = os.path.getsize(line)
                    print(f"Size of {line}: {convert_size(size)}")
                elif os.path.isdir(line):
                    total_size = 0
                    for root, dirs, files in os.walk(line):
                        for file in files:
                            total_size += os.path.getsize(os.path.join(root, file))
                    print(f"Total size of {line}: {convert_size(total_size)}")
            else:
                print(f"Path does not exist: {line}")
    except Exception as e:
        print(e)


def do_unzip(self, line):
    import zipfile
    try:
        zipfile.ZipFile(line).extractall()
        print(f"Unzipped {line}")
    except Exception as e:
        print(e)

def do_zip(self, line):
    import zipfile
    try:
        zipfile.ZipFile(line, 'w').write(os.getcwd())
        print(f"Zipped {line}")
    except Exception as e:
        print(e)

