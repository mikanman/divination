from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from page.forms import InputForm

import openai

openai.api_key="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"

class FrontPageView(TemplateView):
    def __init__(self,):
        self.params={
            'form':InputForm,
            'ans':' ',
        }

    def get(self,request):
        return render(request, "page/frontpage.html", self.params)

    def post(self,request):
        input =  request.POST['input']
        self.params['ans'] = use(input)
        return render(request, "page/frontpage.html",self.params)


def use(prompt):

    response = openai.Completion.create(
        engine='davinci:ft-personal-2022-12-16-06-46-00', 
        prompt=prompt,
        max_tokens= 1500,
        stop = "お疲れさまでした。"
    )

    # print(prompt+"\n________________________________________________________________\n")

    resp =  response['choices'][0]['text'].split('。')
    ans = ''
    for i in resp[:-1]:
        ans += str(i + '。\n')

    return ans
