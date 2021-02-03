"""
D:\note\docs
put this scripts above path

install pandoc in github
"""

import os
import pathlib
import re

build_path = 'build/docx'
# for pdf
# build_path = 'build/pdf'

pathlib.Path(build_path).mkdir(parents=True, exist_ok=True)
path_build = pathlib.Path(__file__).resolve().parent
path_root = os.path.join(path_build, 'source')

command = 'pandoc -o {0} -f rst+east_asian_line_breaks -s {1}'
# for pdf
# command = 'pandoc -s -o {0} {1}'


def get_all_rst_files():
    build_files = []
    for dirpath, dirnames, filenames in os.walk(path_root):
        for filename in filenames:
            if filename.endswith('.rst'):
                a = os.path.join(dirpath, filename)
                build_files.append(a)
    return build_files


def get_filename_without_suffix(full_file):
    if full_file:
        file_suffix = re.split('[\\\/]', full_file)[-1]
        return file_suffix.split('.')[0]
    else:
        return 'no-filename'


def build_docx_for_each_rst(build_files):

    for i, f in enumerate(build_files):
        output_file = os.path.join(
            build_path,
            '{0}-{1}.docx'.format(
            # for pdf
            # '{0}-{1}.pdf'.format(
                i,
                get_filename_without_suffix(f)))

        os.system(command.format(output_file, f))
        print('{0} converted successfully'.format(str(f)))


def main():
    build_files = get_all_rst_files()
    build_docx_for_each_rst(build_files)

#     # if serval rst files, code execute correctly below
#     os.system(command.format(
#         os.path.join(
#             build_path,
#             'all-in-one.docx'),
#         ' '.join(build_files)))
#     print('all-in-one converted successfully')


if __name__ == '__main__':
    main()


