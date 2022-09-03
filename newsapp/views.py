from unittest import result
from django.shortcuts import render
from django.shortcuts import redirect
from .models import News, NewsUrls, Sentences, Words, Apis, data_NewsApi
from .forms import ApiForm, NewsAPIForm,DeepLForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .apifiles import NewsApipy
import urllib.request
import requests
from bs4 import BeautifulSoup
from django.contrib import messages

class Create(CreateView):
    template_name = 'home.html'
    model = News
    fields = ('url',)
    success_url = reverse_lazy('list')

def listfunc(request):
    for post in News.objects.all():
        url = post.url
    list = []
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "html.parser")
    elems = bs.find_all(class_="teaser__link")
    for elem in elems:
        title = elem.h3.text
        url2 = elem.get('href')
        list.append([title, url2])
        newsurls = NewsUrls(title=title, url=url2)  # --- 3
        newsurls.save()  # --- 4
    articles=NewsUrls.objects.all()
    params = {
        'articles': articles,
    }
    return render(request, 'list.html', params)

def wordlistfunc(request ,article_id):
    article = NewsUrls.objects.get(id=article_id) # --- 2
    url=article.url
    requeste=request
    from urllib import request #urllibはURLを取得する。
    response = request.urlopen(url)
    soup = BeautifulSoup(response)
    response.close()
    #URLを指定して、テキストを抽出
    toctext = soup.find_all("p", class_='m-ten')
    text=""
    for a in toctext:
        text+= a.get_text()
    import re
    str1 = re.sub('[\n]', '', text)  
    #文章のリスト作成
    sentencelist = str1.split(".") 
    str2 = re.sub('[.]', '', text)  
    #単語のリスト作成
    wordlist = str2.split()  # スペースで区切って単語ごとのリストを作成
    #sentence wordのリストを登録
    for sentence in sentencelist:
        sentencedata = Sentences(sentence_de=sentence, url_id=article_id,sentence_jp=sentence_jp)  
        sentencedata.save()
    for word in wordlist:
        worddata = Words(word_de=word)
        worddata.save
    API_KEY:str = '5d3d2725-201d-aa58-7c7e-9f4bca0eee2b:fx'
    params = {
        "auth_key": API_KEY,
        "text": sentencelist,
        "source_lang": 'DE',
        "target_lang": 'JA'
    }
    request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
    sentence_jps = request.json()
    sentence_jps
    sentencelist=Sentences.objects.filter(url_id=article_id)
    wordlist=Words.objects.filter(url_id=article_id)
    context = {'sentencelist': sentencelist,'wordlist':wordlist,'sentence_jps':sentence_jps}
    return render(requeste, 'wordlist.html', context)
        
def apihomeview(request):
    if request.method == 'POST':
        name = request.POST['name']      # --- 2
        describe = request.POST['describe'] 
        url = request.POST['url'] 
        usrname = request.POST['usrname'] 
        apikey = request.POST['apikey'] 
        form = name+"Form(forms.Form)"
        form = form.replace(' ', '')
        api = Apis(name=name,describe=describe,url=url,usrname=usrname,apikey=apikey,form=form)  # --- 3
        api.save()
        api = Apis.objects.all()
        params = {    
            'api': api,
        }
    else:
        apis=Apis.objects.all()
        params = {
            'apis': apis,
        }
    return render(request, 'apihomeview.html', params)

def apiregiview(request):
    params = { 
        'form': ApiForm(),
    }
    return render(request, 'apiregiview.html', params)

def apiregi(request):
    name = request.POST['name']      # --- 2
    describe = request.POST['describe'] 
    url = request.POST['url'] 
    usrname = request.POST['usrname'] 
    apikey = request.POST['apikey'] 
    form = name+"Form(forms.Form)"
    form = form.replace(' ', '')
    api = Apis(name=name,describe=describe,url=url,usrname=usrname,apikey=apikey,form=form)  # --- 3
    api.save()
    return redirect('home_api') 

def api_delete(request, api_id):
    api = Apis.objects.get(id=api_id)
    api.delete()
    return redirect('home_api')

def apiroom(request, api_id):
    api=Apis.objects.get(id=api_id)
    datas=data_NewsApi.objects.all()
    formlist={
        6:NewsAPIForm,
        11:DeepLForm,
    }
    form=formlist[api_id]
    params = {    
        'api_id': api_id,
        'api':api,
        'form': form,
    }
    return render(request, 'forms.html',params)

def apidatacreate(request, api_id):
    if api_id==6:
        api_key = Apis.objects.get(id=api_id).apikey
        api_url = Apis.objects.get(id=api_id).url
        keyword = request.POST['keyword']
        pageSize=request.POST['pageSize']
        headers = {'X-Api-Key': api_key}
        params = {
            'q': keyword,
            'pageSize' :pageSize,
        }
        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()
        status = data["status"]
        title=data['articles'][1]['title']
        descripriotn=data['articles'][1]['description']
        url=data['articles'][1]['url']
        publishedAt=data['articles'][1]['publishedAt']
        content=data['articles'][1]['content']
        data_NewsApi(                  
            title=title,
            descripriotn=descripriotn,
            url=url,
            publishedAt=publishedAt,
            content=content,
            api_id=api_id,
            ).save
        api = data_NewsApi.objects.all()
        params={
            'api':api,
        }
        messages.add_message(request, messages.SUCCESS, "ブログを作成しました")    # 追加
        return redirect('api_room')
    elif api_id==11:
        api_key = Apis.objects.get(id=api_id).apikey
        api_url = Apis.objects.get(id=api_id).url
        text = request.POST['text']
        source_lang = request.POST['source_lang']
        target_lang = request.POST['target_lang']
        API_KEY:str = '5d3d2725-201d-aa58-7c7e-9f4bca0eee2b:fx'
        params = {
                    "auth_key": API_KEY,
                    "text": text,
                    "source_lang": source_lang,
                    "target_lang": target_lang
                }
        request = requests.post("https://api-free.deepl.com/v2/translate", data=params)
        result = request.json()
        jp=result["translations"][0]["text"]
        params={
            'jp':jp,
            'text':text,
        }
        messages.add_message(request, messages.SUCCESS, "ブログを作成しました")    # 追加
        return redirect('api_room',params=params )


