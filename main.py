import subprocess
import sys
import time
from typing import List


class ContentResult(object):
    type: str
    name: str
    cc_complexity: str


class FileResult(object):
    file: str
    mi_complexity: str
    content_results: List[ContentResult]


def write_report(data: List[FileResult]) -> None:
    f = open(f'report_{time.time()}.md', 'w')
    f.write('| File | MI | Type | Name | CC |\n')
    f.write('--- | --- | --- | --- | ---\n')
    for entry in data:
        f.write(f'| {entry.file} | <b>{entry.mi_complexity}</b> | | | |\n')
        for detail in entry.content_results:
            f.write(f'| {entry.file} | | {detail.type} | {detail.name} | <b>{detail.cc_complexity}</b> |\n')
    f.close()


def convert_results(path: str, mi_results: str, cc_results: str) -> List[FileResult]:
    to_return = []
    contents = []
    file_content: FileResult = None
    for cc_line in cc_results.split('\\r\\n'):
        if cc_line.startswith(path):
            if file_content is not None:
                file_content.content_results = contents
                to_return.append(file_content)
            mi_line = next((mi for mi in mi_results.split('\\r\\n') if mi.startswith(cc_line)), None)
            mi_content = mi_line.split(' - ')
            file_content = FileResult()
            file_content.file = mi_content[0].removeprefix(path + '\\\\')
            file_content.mi_complexity = mi_content[1]
            contents = []
        else:
            cc_content = cc_line.split(' ')
            if len(cc_content) == 9:
                content = ContentResult()
                content.type = cc_content[4]
                content.name = cc_content[6]
                content.cc_complexity = cc_content[8]
                contents.append(content)

    file_content.content_results = contents
    to_return.append(file_content)

    return to_return


def harvest(path: str) -> None:
    escaped_path = path.replace('\\', '\\\\')
    mi_results = subprocess.Popen(['radon', 'mi', path], shell=False, stdout=subprocess.PIPE).stdout.read()
    cc_results = subprocess.Popen(['radon', 'cc', path], shell=True, stdout=subprocess.PIPE).stdout.read()

    objectified_results = convert_results(escaped_path, str(mi_results).removeprefix('b\''),
                                          str(cc_results).removeprefix('b\''))

    write_report(objectified_results)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python main.py <path_to_harvest>')
        exit(0)

    harvest(path=sys.argv[1])
