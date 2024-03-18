import urllib.parse

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
import csv



def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = 1
    bus_stations_info = []
    with open(settings.BUS_STATION_CSV, encoding='cp1251') as text:
        reader = csv.DictReader(text)
        for row in reader:
            bus_stations_info.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    bus_stations_pagi = Paginator(bus_stations_info, 10)
    page_number = int(request.GET.get('page', 1))
    page = bus_stations_pagi.get_page(page_number)
    next_page_url = f'{reverse(bus_stations)}?{urllib.parse.urlencode({"page": page_number + 1})}'
    return render(request, 'index.html', context={
            'bus_stations': page,
            'current_page': current_page,
            'prev_page_url': None,
            'next_page_url': next_page_url,
        })

