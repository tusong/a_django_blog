from django.shortcuts import render,render_to_response
from django import template
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Article

# Create your views here.


