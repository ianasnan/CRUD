from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from django.db import connection,connections
from books.config import *

def index(request):
	with connection.cursor() as cursor:
		cursor.execute("select * from public.data_buku")
		hasil = dictfetchall(cursor)
	data = {
		'hasil':hasil,
	}
	return render(request, 'base/index.html', data)
def simpanbuku(request):
	data = request.POST
	idnya = data['id']
	judul = data['judul']
	deskripsi = data['deskripsi']
	kategori = data['kategori']
	keyword = data['keyword']
	harga = data['harga']
	penerbit = data['penerbit']
	try:
		with connection.cursor() as cursor:
			cursor.execute("insert into public.data_buku (id_buku,judulbuku,deskripsi,kategori,keyword,harga,penerbit) values (%s,%s,%s,%s,%s,%s,%s)",
				[idnya,judul,deskripsi,kategori,keyword,harga,penerbit])
			hasil = 'Data Berhasil Disimpan'
	except Exception as e:
		print(e)
		hasil = 'eror'
	return HttpResponseRedirect('../')

def ambilbuku(request):
	data = request.GET.get('id_user')
	with connection.cursor() as cursor:
		cursor.execute("select * from public.data_buku where id_buku=%s",[data])
		hasil = dictfetchall(cursor)
	for x in hasil:
		id_buku = x['id_buku']
		judulbuku = x['judulbuku']
		deskripsi = x['deskripsi']
		kategori = x['kategori']
		keyword = x['keyword']
		harga = x['harga']
		penerbit = x['penerbit']
	data = {
		'id_buku':id_buku,
		'judulbuku':judulbuku,
		'deskripsi':deskripsi,
		'kategori':kategori,
		'keyword':keyword,
		'harga':int(harga),
		'penerbit':penerbit,
	}
	return JsonResponse(data)


def editbuku(request):
	data = request.POST
	idnya = data['id']
	judul = data['judul']
	deskripsi = data['deskripsi']
	kategori = data['kategori']
	keyword = data['keyword']
	harga = data['harga']
	penerbit = data['penerbit']
	try:
		with connection.cursor() as cursor:
			cursor.execute("update public.data_buku set judulbuku=%s, deskripsi=%s, kategori=%s, keyword=%s, penerbit=%s, harga=%s where id_buku=%s",
				[judul,deskripsi,kategori,keyword,penerbit,harga,idnya])
			hasil = 'berhasil edit'
	except Exception as e:
		print(e)
		hasil = 'eror'
	
	return HttpResponseRedirect('../')

def deletebuku(request):
	data = request.GET
	id_buku = data['id']
	with connection.cursor() as cursor:
		cursor.execute("delete from public.data_buku where id_buku=%s",[id_buku])
		data = "Data Berhasil Dihapus"

	return HttpResponse(data)