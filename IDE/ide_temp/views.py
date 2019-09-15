from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
import json
from .supportLib.readFile import writeFile
from .supportLib.compiler import compile, run
import re


# Create your views here.

def home(request):
    return render(request, 'ide_temp/project.html')


def compileView(request):
    pattern = '.*class\\s+(\\w+)'
    if request.POST and request.is_ajax():
        text = request.POST.get('code')
        res = re.findall(pattern, text)
        writeFile(text, res[0])
        stdinput = request.POST.get('stdin')
        stdin = open('stdin.txt', 'w')
        stdin.write(stdinput)
        stdin.close()
        check_compilation = compile(lang='java', path='ide_temp/source/' + res[0] + '.java')
        if check_compilation == 1:
            stderr = open('stderr.txt', 'r')
            error = stderr.read()
            stderr.close()
            data = json.dumps({'output': error})
            print(data)
            return HttpResponse(data, content_type="application/json")
        else:
            check_run = run(lang='java', path=res[0])
            if check_run == 0:
                stdout = open('stdout.txt', 'r')
                output = stdout.read()
                stdout.close()
                data = json.dumps({'output': output})
                print(data)
                return HttpResponse(data, content_type="application/json")
            else:
                stderr = open('stderr.txt', 'r')
                error = stderr.read()
                stderr.close()
                data = json.dumps({'output': error})
                return HttpResponse(data, content_type="application/json")
    else:
        return Http404
