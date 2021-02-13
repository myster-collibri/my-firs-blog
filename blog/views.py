from django.shortcuts import render
from .models import Article,Categorie
#from gtts import gTTS

# Create your views here.

def home(request):
	#text2speech=gTTS(text="Gerome est amoureux de sandra il me l'a dit hier, fait attention petit ",lang="fr")
	#text2speech.save('audio.mp3')
	list_articles=Article.objects.all()
	context={"liste_articles":list_articles}
	return render(request,"index.html",context)

def detail(request,id_article):
	article=Article.objects.get(id=id_article)
	categorie=article.category
	article_en_relation=Article.objects.filter(category=categorie)[:5]
	return render(request,'detail.html',{'article':article,"en_relation":article_en_relation,"categorie":categorie})

def search(request):
	query=request.GET['article']
	resultat_list=Article.objects.filter(title__icontains=query)
	if len(resultat_list)>=1:

		return render(request,"search.html",{"query":query,"list_res":resultat_list})
	else:
		
		return render(request,"search.html",{"query":query,"no_article":True})

