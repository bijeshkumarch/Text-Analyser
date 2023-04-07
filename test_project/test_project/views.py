# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

import string

def homepage(request):
    return render(request,'remove_punc.html')

    
def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')

    
def removePuncResult(request):

    #get the text from 'text' in html
    text = request.GET.get('text','default')
    remove_punc = request.GET.get('Remove punc','off')
    character_count_with_space = request.GET.get('Character count with space', 'off')
    character_count_without_space = request.GET.get('Character count without space', 'off')
    word_count = request.GET.get('Word count', 'off')
    sentence_count = request.GET.get('Sentence count', 'off')

    param=dict()
    param['analyzed_text'] = text
    param['purpose'] = 'Purpose not selected'
    #param['description'] = ''
    desc = ""

    cw0s = 0
    cw1s = 0
    wc = 1
    sc = 1
    removed = ""
    for i in text:
        cw0s += 1
        if i in string.punctuation:
            continue
        if i != " ":
            cw1s += 1
        if i == " ":
            wc += 1
        if i == ".":
            sc += 1
        removed += i

    num = 1
    if remove_punc == 'on':
        param['analyzed_text'] = removed
        param['purpose'] = 'Remove punctuations'
    if character_count_with_space == 'on':
        desc += str(num) + ". " + "Character count (with space): " + str(cw0s) + "\n"
        num +=1
    if character_count_without_space == 'on':
        desc += str(num) + ". " + "Character count (without space): " + str(cw1s) + "\n"
        num += 1
    if word_count == 'on':
        desc += str(num) + ". " + "Word count: " + str(wc) + "\n"
        num += 1
    if sentence_count == 'on':
        desc += str(num) + ". " + "Sentence count: " + str(sc) + "\n"
        num += 1
    param['desc'] = desc
    return render(request,'removed punctuation.html',param)