# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def post_list(request):
    return render(request, 'home/index.html')
def single(request):
	return render(request, 'home/single.html')
def gallery(request):
	return render(request, 'home/gallery.html')
def archive(request):
	return render(request, 'home/archive.html')
def contact(request):
	return render(request, 'home/contact.html')