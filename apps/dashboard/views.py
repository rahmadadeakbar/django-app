from django.shortcuts import render
from .models import Data_mahasiswa
# Create your views here.


def index(request):
    hasil = Data_mahasiswa.objects.all()
    print(hasil)  # untuk lihat hasilnya silahkan liat diterminal
    data = {
        'data': hasil,
    }
    return render(request, "index.html", data)


def tambah(request):
    return render(request, "tambahdata.html")
