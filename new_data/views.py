from django.shortcuts import render, redirect
from django.http import HttpResponse
from bs4 import BeautifulSoup as BS
from tasks.models import *
from tasks.forms import *

def index(request):
    form = VariantForm()
    if request.method == "POST":
        html = request.POST['html']
        return render(request, 'new_data/index.html', {'html': html, 'form': form})
    else:
        return render(request, 'new_data/index.html', {'html': '<h1>Hello</h1>', 'form': form})

def ajax_html(request):
    if request.method == 'POST':
        html = request.POST['html']

        soup = BS(html, "html.parser")
        ### получаем вариант
        variant = soup.find('span', id='news-title').text
        ### получаем ответы
        table = soup.find('table', class_='table_results')
        tr = table.findAll('tr')
        answer = []
        for tr_one in tr:
            td = tr_one.findAll('td')
            if len(td) >= 3:
                if td[0] and td[0] != "" and len(td[0]) == 1 and td[2] and td[2] != "" and int(td[0].text) > 3 and int(td[0].text) < 20:
                    answer.append(td[2].text)
        ### получаем задания
        tasks = soup.find('div', class_='test_tabs_row')
        testings = soup.findAll('div', class_='testings')
        t = []
        for test in testings:
            types = test.find('div', class_='types')
            cont = test.find('div', class_='cont')
            if types and types.text != "" and int(types.text) > 3 and int(types.text) < 20 and cont and cont != "":
                p = cont.div.findAll('p')
                if p and p[0] != "":
                    number = types.text
                    description = p[0].text
                    variables = [str(x) for x in cont.div.contents[1:]]
                    variables = ''.join(variables)
                    t.append([number, description, variables])

        sub = request.POST['sub']
        vr = Variant.objects.create(name=variant, subject_id_id=sub)
        vr.save()
        id_vr = vr.id

        k = 0
        for i in t:
            ts = Tasks.objects.create(number=i[0], description=i[1], variables=i[2], ask=answer[k], variant_id_id=id_vr)
            ts.save()
            k += 1

        return HttpResponse("okay")
    else:
        return redirect('/')
