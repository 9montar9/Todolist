from django.shortcuts import render
def index(request):
	name="Silvester"
	return render(request,"index.html", {"name":name})
def main(request):
	path=request.path.replace("/","")
	if path=="":
		path = "index"
	age="1000"
	surname="stalone"
	names = [ "Понедельник", "Вторник"]
	return render(request,path+".html", {"age":age, "surname":surname,"names":names})

# Create your views here.
