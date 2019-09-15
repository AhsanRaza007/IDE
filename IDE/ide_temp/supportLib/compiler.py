
import subprocess

stdin = 'stdin.txt'
stdout = 'stdout.txt'
stderr = 'stderr.txt'


def init():
    return open('stdin.txt', 'r'), open('stdout.txt', 'w'), open('stderr.txt', 'w')


def compile(lang='python', path=''):
    if lang == 'java':
        cmd = 'javac ' + path
        stdin, stdout, stderr = init()
        result = subprocess.call(cmd, shell=True, stdout=stdout, stderr=stderr)
        return result


def run(lang='python', path=''):
    if lang == 'java':
        cmd = 'java ' + path
        stdin, stdout, stderr = init()
        result = subprocess.call(cmd, shell=True, stdin=stdin, stdout=stdout, stderr=stderr)
        print(result)
        return result


if __name__ == '__main__':
    if compile('java', r'.\Java.java') == 0:
        run('java', r'Java')
