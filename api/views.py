from django.shortcuts import render
from rest_framework.views import View
from .serializers import ClassroomSerializer
from .repository import ClassroomRepository
from .forms import ClassroomForm

# Create your views here.
class ClassroomInsert(View):
    def get(self, request):
        classroom_form = ClassroomForm()
        return render(request, "post_classroom.html", { "form": classroom_form})
     
    def post(self, request):
        classroom_form = ClassroomForm(request.POST)
        if classroom_form.is_valid():
            serializer = ClassroomSerializer(data=classroom_form.data)
            if serializer.is_valid():
                repository = ClassroomRepository('classroom_reservations_ACL')
                repository.insert(serializer.data)
                return render(request, "classrooms.html", {"classrooms": [serializer.data]})
            else:
                return render(request, "classrooms.html", {"error" : serializer.errors})
        else: 
            return render(request, "classrooms.html", {"error" : classroom_form.errors})
        
class ClassroomView(View):
    def get(self, request):
        try:
            repository = ClassroomRepository('classroom_reservations_ACL')
            documents = list(repository.list()) 
            serializer = ClassroomSerializer(data=documents, many=True)
            if serializer.is_valid():
                classrooms = serializer.save()
                return render(request, "classrooms.html", {"classrooms": classrooms})
            else: 
                return render(request, "classrooms.html", {"error" : serializer.errors})
        except ValueError as e:
            return render(request, "classrooms.html", {"error" : e})
        except Exception as e:
            return render(request, "classrooms.html", {"error" : e})
    
    def getById(request, document_id):
        try:
            repository = ClassroomRepository('classroom_reservations_ACL')
            documents = list(repository.getById(document_id))
            serializer = ClassroomSerializer(data=documents, many=True)
            if serializer.is_valid():
                classrooms = serializer.save()
                print(classrooms)
                return render(request, "classrooms.html", {"classrooms": classrooms})
            else: 
                return render(request, "classrooms.html", {"error" : serializer.errors})
        except ValueError as e:
            return render(request, "classrooms.html", {"error" : e})
        except Exception as e:
            return render(request, "classrooms.html", {"error" : e})

    def deleteById(request, document_id):
        repository = ClassroomRepository('classroom_reservations_ACL')
        repository.delete(document_id)
        return render(request, "classrooms.html")
    
           
class ClassroomUpdate(View):
    def get(self, request, document_id):
        classroom_form = ClassroomForm()
        return render(request, "update.html", { "form": classroom_form, "document_id": document_id})

    
    def post(self, request, document_id):
        classroom_form = ClassroomForm(request.POST)
        if classroom_form.is_valid():
            serializer = ClassroomSerializer(data=classroom_form.data)
            if serializer.is_valid():
                repository = ClassroomRepository('classroom_reservations_ACL')
                print(document_id)
                repository.update(document_id, serializer.data)
                return render(request, "classrooms.html", {"classrooms": [serializer.data]})
            else:
                return render(request, "classrooms.html", {"error" : serializer.errors})
        else: 
            return render(request, "classrooms.html", {"error" : classroom_form.errors})